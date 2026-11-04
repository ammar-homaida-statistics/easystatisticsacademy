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


if __name__ == "__main__":
    unittest.main()
