with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines] 

def strictly_increasing(items): 
    return all(itemX < itemY for itemX, itemY in zip(items, items[1:]))

def strictly_decreasing(items):
    return all(itemX > itemY for itemX, itemY in zip(items, items[1:]))


reports_safe = 0 
for line in lines:
    reports = list(map(int, line.split()))
    print(strictly_increasing(reports))
    if strictly_decreasing(reports) or strictly_increasing(reports):
        print(reports)
        diff = [abs(int(i) - int(j)) for i, j in zip(reports, reports[1:])]
        print(diff)
        if max(diff) <= 3:
            reports_safe += 1

print(reports_safe)

