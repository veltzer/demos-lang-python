#!/usr/bin/env bash
# Install two versions of `requests` into their own directories under ./libs/.
# Re-run safely; it wipes and reinstalls.
set -euo pipefail
cd "$(dirname "$0")"

rm -rf libs/requests_v2_28 libs/requests_v2_31

# --target installs into the given directory only; it does NOT touch your
# site-packages. (pip may still print "dependency conflicts" warnings comparing
# against your environment — harmless here, ignore them.)
python -m pip install --target ./libs/requests_v2_28 "requests==2.28.2" --no-warn-script-location -q
python -m pip install --target ./libs/requests_v2_31 "requests==2.31.0" --no-warn-script-location -q

echo
echo "Done. Now run:  ./demo.py"
