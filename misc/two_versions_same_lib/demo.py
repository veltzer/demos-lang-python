#!/usr/bin/env python

"""Two versions of `requests` alive in one process at the same time.

Run:  python demo.py
"""

from pathlib import Path

from dual_loader import load_package

HERE = Path(__file__).parent
LIBS = HERE / "libs"


def show(tag, requests_mod):
    # requests stashes its bundled urllib3 under requests.packages.urllib3
    urllib3 = requests_mod.packages.urllib3
    print(f"  [{tag}]")
    print(f"    requests.__version__   = {requests_mod.__version__}")
    print(f"    requests.__file__      = {requests_mod.__file__}")
    print(f"    bundled urllib3        = {urllib3.__version__}")
    print(f"    requests module id     = {id(requests_mod)}")
    print(f"    Session class          = {requests_mod.Session}")
    print(f"    HTTPError exc type     = {requests_mod.exceptions.HTTPError}")


def main():
    print("Loading two versions of `requests` side by side...\n")

    req_old = load_package("requests", LIBS / "requests_v2_28")
    req_new = load_package("requests", LIBS / "requests_v2_31")

    show("OLD", req_old)
    print()
    show("NEW", req_new)

    print("\nSanity checks:")
    print(f"  different module objects?      {req_old is not req_new}")
    print(f"  different Session classes?     {req_old.Session is not req_new.Session}")
    print(f"  different HTTPError types?     "
          f"{req_old.exceptions.HTTPError is not req_new.exceptions.HTTPError}")
    print(f"  different bundled urllib3?     "
          f"{req_old.packages.urllib3.__version__ != req_new.packages.urllib3.__version__}")

    # The big gotcha: exceptions don't cross the boundary.
    print("\nThe gotcha — exception identity does NOT cross versions:")
    try:
        raise req_old.exceptions.HTTPError("boom from the OLD requests")
    except req_new.exceptions.HTTPError:
        print("  caught by NEW's HTTPError  (would mean they're the same type)")
    except req_old.exceptions.HTTPError as e:
        print(f"  NEW's `except` did NOT catch it; OLD's did: {e!r}")

    # Optional: actually use both to make a real request. Commented out so the
    # demo works offline; uncomment if you have network.
    #
    # print("\nLive requests:")
    # for tag, mod in (("OLD", req_old), ("NEW", req_new)):
    #     r = mod.get("https://httpbin.org/get", timeout=10)
    #     print(f"  [{tag}] requests {mod.__version__} -> HTTP {r.status_code}")

    # And the original site-packages `requests`, if any, is untouched:
    try:
        import requests as system_requests
        print(f"\nMeanwhile a plain `import requests` still gives: "
              f"{system_requests.__version__} ({system_requests.__file__})")
    except ImportError:
        print("\n(no `requests` installed in the normal environment — that's fine)")


if __name__ == "__main__":
    main()
