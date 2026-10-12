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
