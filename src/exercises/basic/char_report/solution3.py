with open('ex4.py') as f:
    report = {}
    lines = f.readlines()
    for line in lines:
        for c in line:
            if not (c in [' ', '\n', '\r', '\t']):
                if c in report:
                    report[c] += 1
                else:
                    report[c] = 1
with open('ex4.py.report', 'w') as f:
    keys = sorted(report.keys())
    for c in keys:
        f.write(f"{c} : {report[c]}\n")
