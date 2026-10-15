# Exercise the actual Liquid template independently of Jekyll page ordering.
# Run with: bundle exec ruby .github/scripts/test_search_template.rb
require "jekyll"
require "json"

Liquid::Template.register_filter(Jekyll::Filters)
# __dir__ is .github/scripts; the repository root is two directories above it.
source = File.read(File.expand_path("../../search.json", __dir__))
source = source.sub(/\A---\r?\n.*?\r?\n---\r?\n/m, "")
lesson = { "title" => "Bayes' theorem: \"β\" & probability", "url" => "/probability/conditional/bayes-theorem/",
           "content" => "<p>Probability\n and statistics.</p><script>not_searchable()</script>" }
untitled = { "url" => "/untitled.html" }
[
  [], [untitled], [lesson], [lesson, untitled], [untitled, lesson],
  [untitled, lesson, untitled, lesson.merge("url" => "/second/"), untitled]
].each do |pages|
  output = Liquid::Template.parse(source).render!("site" => { "pages" => pages })
  records = JSON.parse(output)
  expected = pages.select { |page| page["title"] && page["url"] }
  raise "Wrong emitted records" unless records.map { |page| page["url"] } == expected.map { |page| page["url"] }
  records.each do |page|
    raise "Title escaping changed" unless page["title"] == lesson["title"]
    raise "Script leaked into index" if page["content"].include?("not_searchable")
    raise "Whitespace joined words" unless page["content"].include?("Probability and statistics.")
  end
end
puts "PASS: six Liquid/JSON cases, including trailing untitled pages, escaping, and script filtering."


# Benchmark against the exact search template used on main at fc68a0e.
# Use real page-source fixtures (all titled/permalink Markdown pages) so the
# before/after index-size comparison is reproducible in GitHub Actions.
require "yaml"
require "date"
legacy_source = <<~LIQUID
[
{% assign first = true %}
{% for page in site.pages %}
  {% if page.title and page.url and page.url != '/404.html' %}
  {% unless first %},{% endunless %}
  {
    "title": {{ page.title | jsonify }},
    "url": {{ page.url | jsonify }},
    "content": {{ page.content | strip_html | normalize_whitespace | jsonify }}
  }
  {% assign first = false %}
  {% endif %}
{% endfor %}
]
LIQUID

repo_root = File.expand_path("../..", __dir__)
real_pages = Dir.glob(File.join(repo_root, "**", "*.md")).filter_map do |path|
  relative = path.delete_prefix("#{repo_root}/")
  next if relative.start_with?(".github/", "_site/", "vendor/", "node_modules/")
  text = File.read(path)
  front = text.match(/\A---\s*\r?\n(.*?)\r?\n---\s*\r?\n/m)
  next unless front
  begin
    meta = YAML.safe_load(front[1], permitted_classes: [Date, Time], aliases: true)
  rescue Psych::Exception
    next
  end
  next unless meta.is_a?(Hash) && meta["title"] && meta["permalink"]
  {"title" => meta["title"].to_s,
   "url" => meta["permalink"].to_s,
   "content" => text[front.end(0)..]}
end
raise "Insufficient real search fixtures: #{real_pages.size}" unless real_pages.size >= 100

render = lambda do |text|
  JSON.parse(Liquid::Template.parse(text).render!("site" => {"pages" => real_pages}))
end
old_index = render.call(legacy_source)
new_index = render.call(source)
raise "Index routes changed" unless old_index.map { |p| p["url"] } == new_index.map { |p| p["url"] }
raise "Title ranking input changed" unless old_index.map { |p| p["title"] } == new_index.map { |p| p["title"] }

old_bytes = JSON.generate(old_index).bytesize
new_bytes = JSON.generate(new_index).bytesize
reduction = 100.0 * (old_bytes - new_bytes) / old_bytes
puts "SEARCH BENCHMARK (#{real_pages.size} real Markdown source pages; source-template proxy; not deployed byte count)"
puts "  main fc68a0e template: #{old_bytes} UTF-8 JSON bytes"
puts "  proposed template: #{new_bytes} UTF-8 JSON bytes"
puts "  reduction: #{format('%.1f', reduction)}%"
raise "Search index did not shrink" unless new_bytes < old_bytes

queries = ["variance", "standard deviation", "bayes", "two sample t test",
           "chi square", "hypothesis testing", "logistic regression", "fisher information"]
# Approximate the browser's current title-first ranking on the same indexed
# document titles/contents. Preserve exact-title and title-prefix leadership.
normalize = ->(text) { text.downcase.gsub(/\s+/, " ").strip }
rank = lambda do |records, query|
  q = normalize.call(query)
  terms = q.split.uniq
  records.filter_map do |page|
    title = normalize.call(page["title"])
    content = normalize.call(page["content"])
    priority = if title == q then 0
    elsif title.start_with?(q) then 1
    elsif title.include?(q) then 2
    elsif content.include?(q) then 3
    elsif terms.size > 1 && terms.all? { |t| title.include?(t) } then 4
    elsif terms.size > 1 && terms.all? { |t| title.include?(t) || content.include?(t) } then 5
    else 6 end
    [priority, page["url"]] if priority < 6
  end.sort_by(&:first).first(8).map(&:last)
end
queries.each do |query|
  old_top = rank.call(old_index, query)
  new_top = rank.call(new_index, query)
  raise "Search query lost all results: #{query}" if new_top.empty?
  if old_top.any?
    # A high-relevance title match must remain discoverable; long content
    # matches are expected to change when boilerplate is removed.
    prominent = old_index.find { |p| p["url"] == old_top.first }
    title = normalize.call(prominent["title"])
    if title.include?(normalize.call(query))
      raise "Lost title-ranked result: #{query}" unless new_top.include?(old_top.first)
    end
  end
  puts "  #{query.inspect}: main #{old_top.first.inspect} -> proposed #{new_top.first.inspect}"
end

# Exercise markers and exclusion directly. Raw navigation progress code
# should not enter snippets when a proper lesson body is available.
illustrative = [{"title"=>"Example", "url"=>"/example/",
  "content"=>"<script>progress_label_noise()</script><!-- HERO --><h1>Example</h1><!-- LESSON --><p>Meaningful inference text.</p><!-- NAVIGATION --><p>previous next links</p>"}]
case_record = JSON.parse(Liquid::Template.parse(source).render!("site"=>{"pages"=>illustrative})).first
raise "Progress code entered search text" if case_record["content"].include?("progress_label_noise")
raise "Navigation entered search text" if case_record["content"].include?("previous next")
raise "Lesson body not searchable" unless case_record["content"].include?("Meaningful inference text")
puts "PASS: search-index source benchmark, preserved routes/title ranking, representative queries and content isolation."
