from typing import Dict

with open("data.txt") as f:
    report: Dict[str, int] = {}
    lines = f.readlines()
    for line in lines:
        for c in line:
            if not (c in [' ', '\n', '\r', '\t']):
                if c in report:
                    report[c] += 1
                else:
                    report[c] = 1
with open('c:/tmp2.txt', 'w') as f:
    keys = sorted(report.keys())
    for c in keys:
        f.write(f"{c} : {report[c]}\n")
