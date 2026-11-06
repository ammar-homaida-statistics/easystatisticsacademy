"""Mocked HTTP checks: distinguish missing content, 404, redirects and healthy deployment."""
import importlib.util
from pathlib import Path
import unittest
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("live_check", ROOT/".github/scripts/check_live_pages.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class FakeResponse:
    def __init__(self, data=b"marker", status=200, url="https://easystatisticsacademy.com/page/"):
        self.status, self.data, self.url = status, data, url
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return False
    def geturl(self):
        return self.url
    def read(self, _):
        return self.data


class LivePagesTests(unittest.TestCase):
    def test_success(self):
        self.assertEqual(module.verify_once(checks=(("/page/", b"marker"),),
            opener=lambda request, timeout: FakeResponse()), [])

    def test_missing_content(self):
        self.assertIn("marker missing", module.verify_once(
            checks=(("/page/", b"required"),),
            opener=lambda request, timeout: FakeResponse())[0])

    def test_http_404(self):
        self.assertIn("HTTP 404", module.verify_once(
            checks=(("/page/", b"marker"),),
            opener=lambda request, timeout: FakeResponse(status=404))[0])

    def test_redirect_elsewhere_rejected(self):
        self.assertIn("redirect", module.verify_once(
            checks=(("/page/", b"marker"),),
            opener=lambda request, timeout: FakeResponse(url="https://example.org/"))[0])

    def test_http_exception_404(self):
        def reject(request, timeout):
            raise HTTPError(request.full_url, 404, "Not found", {}, None)
        self.assertIn("HTTPError", module.verify_once(checks=(("/page/", b"marker"),), opener=reject)[0])

    def test_required_paths(self):
        routes=[r for r,_ in module.CHECKS]
        self.assertEqual(len(routes),len(set(routes)))
        self.assertIn("/ar/probability/random-variables/discrete-random-variables/", routes)
        self.assertIn("/probability/random-variables/continuous-random-variables/",routes)
        for route in (
            "/ar/probability/random-variables/cumulative-distribution-function/",
            "/probability/random-variables/cumulative-distribution-function/",
            "/inference/assumptions-robustness/sensitivity-analysis-and-specification/",
            "/js/cdf-bernoulli-uniform-explorer.js",
            "/js/sensitivity-summary-lab.js",
        ):
            self.assertIn(route,routes)


    def test_revision_matches_exact_new_artifact(self):
        sha="a"*40
        def opener(request,timeout):
            route=request.full_url
            return FakeResponse(data=(sha+chr(10)).encode() if route.endswith("/deployment-revision.txt") else b"marker",
                                url=route)
        self.assertEqual(module.verify_once(checks=(("/page/",b"marker"),),
                        opener=opener,expected_sha=sha),[])

    def test_stale_live_revision_blocks_deployment(self):
        sha="a"*40
        def opener(request,timeout):
            return FakeResponse(data=b"b"*40 if request.full_url.endswith("/deployment-revision.txt") else b"marker",
                                url=request.full_url)
        problems=module.verify_once(checks=(("/page/",b"marker"),),opener=opener,expected_sha=sha)
        self.assertTrue(any("stale deployment revision" in error for error in problems))

    def test_revision_manifest_missing_is_failure(self):
        sha="a"*40
        def opener(request,timeout):
            if request.full_url.endswith("/deployment-revision.txt"):
                return FakeResponse(data=b"404",status=404,url=request.full_url)
            return FakeResponse(url=request.full_url)
        problems=module.verify_once(checks=(("/page/",b"marker"),),opener=opener,expected_sha=sha)
        self.assertTrue(any("deployment-revision" in error for error in problems))

    def test_wrong_route_redirect_rejected(self):
        self.assertIn("redirect",module.verify_once(
            checks=(("/page/",b"marker"),),
            opener=lambda request,timeout:FakeResponse(url="https://easystatisticsacademy.com/other/"))[0])

    def test_approved_batch_83_routes_are_required(self):
        paths=[route for route,_ in module.CHECKS]
        for name in ("ar/probability/random-variables/cumulative-distribution-function",
                     "ar/probability/random-variables/expectation",
                     "js/three-point-moments-lab.js",
                     "inference/power-sample-size/power-curve-and-tradeoffs"):
            self.assertTrue(any(name in path for path in paths))


if __name__ == "__main__":
    unittest.main()
