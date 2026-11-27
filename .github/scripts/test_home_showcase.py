"""Homepage Courses and Code Lab showcase: every link resolves to a published
page, the stated counts match the course and Code Lab pages, and the tabs are
progressively enhanced (no tab roles in the static HTML panels)."""
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HOME=(ROOT/"index.html").read_text(encoding="utf-8")

def permalinks():
    out=set()
    for p in ROOT.rglob("index.*"):
        if p.suffix not in (".md",".html") or "_site" in p.parts or "node_modules" in p.parts:continue
        m=re.search(r'^permalink:\s*"?([^"\n]+?)"?\s*$',p.read_text(encoding="utf-8"),re.M)
        if m:out.add(m.group(1))
    return out

def section():
    start=HOME.index('<section class="esa-home-section esa-home-go"');end=HOME.index("<!-- Learning paths -->")
    return HOME[start:end]

class Showcase(unittest.TestCase):
    def test_every_link_is_a_published_page(self):
        links=re.findall(r'href="(/[^"#?]*)"',section());pages=permalinks()
        self.assertEqual(len(links),33)  # 3 + 3 actions, 9 + 6 regression lessons + 12 Code Lab exercises
        for url in links:
            with self.subTest(url=url):self.assertIn(url,pages)

    def test_counts_match_source_pages(self):
        s=section()
        module=(ROOT/"courses/regression/module-1/index.md").read_text(encoding="utf-8")
        lessons=re.findall(r'Status:\s*(Available|In preparation)',module)
        self.assertEqual(len(lessons),9)
        self.assertIn("<strong>%d of %d</strong>"%(lessons.count("Available"),len(lessons)),s)
        course=(ROOT/"courses/regression/index.md").read_text(encoding="utf-8")
        modules=len(re.findall(r'Module \d+:',re.sub(r'<[^>]+>',' ',course).split("Course map",1)[1].split("Learning outcomes",1)[0]))
        self.assertIn("<strong>%d</strong><span>modules</span>"%modules,s)
        self.assertEqual(len(re.findall(r'href="/courses/regression/module-1/[a-z-]+/"><span>1\.\d</span>',s)),lessons.count("Available"))
        module2=(ROOT/"courses/regression/module-2/index.md").read_text(encoding="utf-8")
        lessons2=re.findall(r'Status:\s*(Available|In preparation)',module2)
        self.assertEqual(len(lessons2),12)
        self.assertIn("%d of %d available"%(lessons2.count("Available"),len(lessons2)),s)
        self.assertEqual(len(re.findall(r'href="/courses/regression/module-2/[a-z-]+/"><span>2\.\d+</span>',s)),lessons2.count("Available"))
        beginner=(ROOT/"code-lab/beginner/index.md").read_text(encoding="utf-8")
        available=re.findall(r'Available · (\d+) exercises',beginner)
        self.assertEqual(sum(map(int,available)),len(re.findall(r'href="/code-lab/beginner/[a-z-]+/[a-z-]+/"><span>\d\.\d</span>',s)))

    def test_titles_follow_the_published_pages(self):
        s=section()
        for path,title in (("courses/regression/module-1/what-is-regression","What Is Regression?"),
                           ("courses/regression/module-1/correlation-vs-regression","Correlation versus Regression"),
                           ("courses/regression/module-1/ordinary-least-squares","Ordinary Least Squares Estimation"),
                           ("courses/regression/module-1/ols-properties","Statistical Properties of the OLS Estimators"),
                           ("courses/regression/module-1/interpreting-coefficients","Interpreting the Coefficients"),
                           ("courses/regression/module-1/goodness-of-fit","Goodness of Fit"),
                           ("courses/regression/module-1/inference","Inference for the Regression Parameters"),
                           ("courses/regression/module-1/confidence-and-prediction-intervals","Confidence Intervals for the Mean Response and Prediction Intervals"),
                           ("courses/regression/module-1/case-study","Case Study"),
                           ("courses/regression/module-2/from-one-to-many-predictors","From One Predictor to Many"),
                           ("courses/regression/module-2/matrix-formulation","The Matrix Formulation"),
                           ("courses/regression/module-2/least-squares-matrix-form","Least Squares in Matrix Form"),
                           ("courses/regression/module-2/ols-estimator-properties","Properties of the OLS Estimator"),
                           ("courses/regression/module-2/interpreting-coefficients-multiple","Interpreting Coefficients in Multiple Regression"),
                           ("courses/regression/module-2/inference-coefficients","Inference for Coefficients and Linear Combinations")):
            self.assertIn(title,(ROOT/path/"index.html").read_text(encoding="utf-8"));self.assertIn(title,s)
        self.assertIn("Regression Analysis: From Foundations to Mastery",(ROOT/"courses/regression/index.md").read_text(encoding="utf-8"))

    def test_progressive_enhancement_markup(self):
        s=section()
        self.assertRegex(s,r'<div class="esa-home-tablist" role="tablist" aria-label="[^"]+" hidden>')
        self.assertEqual(s.count('role="tab"'),2)
        self.assertNotIn('role="tabpanel"',s)  # added by JavaScript only
        for key in ("courses","codelab"):
            self.assertIn('aria-controls="esa-home-panel-%s"'%key,s)
            self.assertIn('id="esa-home-panel-%s" aria-labelledby="esa-home-panel-%s-title"'%(key,key),s)
        js=HOME[HOME.index("[data-esa-tabs]"):]
        for needle in ('"ArrowRight"','"ArrowLeft"','"Home"','"End"','setAttribute("role", "tabpanel")',"list.hidden = false"):
            self.assertIn(needle,js)
        self.assertNotIn("innerHTML",HOME)

    def test_arabic_homepage_and_protected_sections_untouched(self):
        css=(ROOT/"css/home.css").read_text(encoding="utf-8")
        self.assertIn(".esa-home-tablist",css);self.assertIn(".esa-home-panel[hidden] { display:none; }",css)
        self.assertNotIn("esa-home-go",(ROOT/"ar/index.md").read_text(encoding="utf-8"))
        self.assertIn('href="/css/home.css?v=2"',(ROOT/"_layouts/default.html").read_text(encoding="utf-8"))

if __name__=="__main__":unittest.main()
