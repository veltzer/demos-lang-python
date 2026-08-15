"""
Solution1
"""

with open("input.txt") as f:
    report: dict[str, int] = {}
    for line in f:
        for c in line:
            if c not in [" ", "\n", "\r", "\t"]:
                if c in report:
                    report[c] += 1
                else:
                    report[c] = 1
with open("report.txt", "w") as f:
    f.write(str(report))
