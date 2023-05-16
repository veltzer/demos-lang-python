from typing import Dict

with open("input.txt") as f:
    report: Dict[str, int] = {}
    for line in f.readlines():
        for c in line:
            if not (c in [" ", "\n", "\r", "\t"]):
                if c in report:
                    report[c] += 1
                else:
                    report[c] = 1
with open("report.txt", "w") as f:
    f.write(str(report))
