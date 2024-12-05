reports = [list(map(int, line.split())) for line in file]

length = len(reports)-1
safe = 0
for i, report in enumerate(reversed(reports)):
    increase = decrease = False   
    for l, r in pairwise(report):
        if (0 < l-r < 4) and not increase:
            decrease = True
        elif (0 < r-l < 4) and not decrease:
            increase = True
        else:
            break
    else:
        reports.pop(length-i)
        safe += 1

print(safe) #585

safe_tol = 0
for report in reports:
    length = len(report)
    for kick in range(length):
        rep = report[:kick] + report[kick+1:]
        increase = decrease = False
        for l, r in pairwise(rep):
            if (0 < l-r < 4) and not increase:
                decrease = True
            elif (0 < r-l < 4) and not decrease:
                increase = True
            else:
                break
        else:
            safe_tol += 1
            break
     
print(safe + safe_tol)
