#!/usr/bin/env python3
"""Verify post-deployment HTTP availability and expected published content.

Run only AFTER actions/deploy-pages succeeds. Retry a bounded number of times for
CDN propagation and fail the workflow if required pages/assets remain unavailable.
"""
import argparse
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE = "https://easystatisticsacademy.com"
CHECKS = (
    ("/", b"EasyStatisticsAcademy"),
    ("/ar/probability/random-variables/what-is-a-random-variable/", b"esa-two-coin-rv"),
    ("/ar/probability/random-variables/discrete-random-variables/", b"esa-three-pmf-lab"),
    ("/probability/random-variables/discrete-random-variables/", b"discrete-random-variables"),
    ("/probability/random-variables/continuous-random-variables/", b"esa-uniform-pdf-lab"),
    ("/inference/confidence-intervals/ci-for-paired-mean-difference/", b"esa-paired-ci-lab"),
    ("/js/three-point-pmf-explorer.js", b"esaThreePointPMFMath"),
    ("/js/uniform-pdf-interval-explorer.js", b"esaUniformPDFMath"),
    ("/ar/probability/random-variables/cumulative-distribution-function/", b"esa-cdf-explorer"),
    ("/probability/random-variables/cumulative-distribution-function/", b"esa-cdf-explorer"),
    ("/inference/assumptions-robustness/sensitivity-analysis-and-specification/", b"esa-sensitivity-lab"),
    ("/js/cdf-bernoulli-uniform-explorer.js", b"esaCdfMath"),
    ("/js/sensitivity-summary-lab.js", b"esaSensitivityMath"),
    ("/ar/probability/random-variables/continuous-random-variables/", b"esa-uniform-pdf-lab"),
    ("/inference/power-sample-size/power-curve-and-tradeoffs/", b"esa-power-curve-lab"),
    ("/ar/probability/random-variables/expectation/", b"esa-moments-lab"),
    ("/probability/random-variables/expectation/", b"Expectation"),
    ("/js/three-point-moments-lab.js", b"esaThreePointMomentsMath"),
)
MAX_BODY = 2_000_000


def verify_once(base=BASE, checks=CHECKS, opener=urlopen, expected_sha=None):
    errors = []
    if expected_sha is not None:
        if len(expected_sha) != 40 or any(c not in "0123456789abcdef" for c in expected_sha):
            raise ValueError("expected_sha must be a lowercase 40-digit Git commit SHA")
        checks = tuple(checks) + (("/deployment-revision.txt", expected_sha.encode("ascii")),)
    for route, marker in checks:
        url = base.rstrip("/") + route
        request = Request(url, headers={"User-Agent": "EasyStatisticsAcademy-Pages-CI/1.0",
                                        "Cache-Control": "no-cache",
                                        "Pragma": "no-cache"})
        try:
            with opener(request, timeout=20) as response:
                status = response.status
                final_url = response.geturl()
                body = response.read(MAX_BODY + 1)
                if status != 200:
                    errors.append(f"{route}: HTTP {status}")
                elif final_url != url:
                    errors.append(f"{route}: unexpected redirect to {final_url}")
                elif len(body) > MAX_BODY:
                    errors.append(f"{route}: response larger than expected limit")
                elif route == "/deployment-revision.txt" and body.strip() != marker:
                    errors.append(f"{route}: stale deployment revision: expected {expected_sha}, got {body[:100]!r}")
                elif marker not in body:
                    errors.append(f"{route}: expected marker missing")
                elif route.endswith("/") and (b"404" in body[:500] and b"page isn" in body[:500].lower()):
                    errors.append(f"{route}: response resembles the site 404 page")
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            errors.append(f"{route}: {type(exc).__name__}: {exc}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempts", type=int, default=9)
    parser.add_argument("--expected-sha", help="Require the live Pages artifact to match the merged main commit")
    parser.add_argument("--interval", type=float, default=15)
    args = parser.parse_args()
    if not (1 <= args.attempts <= 20 and 0 <= args.interval <= 120):
        parser.error("attempts must be 1–20; interval 0–120 seconds")
    for attempt in range(1, args.attempts + 1):
        errors = verify_once(expected_sha=args.expected_sha)
        if not errors:
            print(f"PASS: all {len(CHECKS)} live pages/assets and expected deployment revision verified")
            return
        print(f"Attempt {attempt}/{args.attempts}: {len(errors)} checks not yet available", flush=True)
        for error in errors:
            print("  " + error, flush=True)
        if attempt < args.attempts:
            time.sleep(args.interval)
    raise SystemExit("FAIL: post-deployment live-page verification did not pass")


if __name__ == "__main__":
    main()
