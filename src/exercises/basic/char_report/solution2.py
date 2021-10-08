with open("tmp.txt") as f:
    report = {}
    lines = f.readlines()
    for line in lines:
        for c in line:
            if not (c in [' ', '\n', '\r', '\t']):
                if c in report:
                    report[c] += 1
                else:
                    report[c] = 1
with open("tmp2.txt", "w") as f:
    for c in report.keys():
        f.write(c)
        f.write(' : ')
        f.write(str(report[c]))
        f.write('\n')
