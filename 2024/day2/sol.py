reports = []

with open("input.txt", "r") as f:
    for line in f:
        report = list(map(int, line.strip().split(" ")))
        reports.append(report)


unsafe = []
for report in reports:
    decreasing = True if report[1] < report[0] else False
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])

        if (
            (decreasing and report[i] > report[i - 1])
            or (not decreasing and report[i] < report[i - 1])
            or (diff < 1 or diff > 3)
        ):
            unsafe.append(report)
            break
        # print(f"diff: {diff}, unsafe: {unsafe}")

print(len(reports) - len(unsafe))


"""
if you have

case 1: 1 2 7 8 9, that is unsafe because 2 and 7 differ by more than 3 remove either 2 or will not make it safe
since diff of numbers before and after are larger still


case 2: 1 2 2 3 4 5, in the case of a difference of 0 (duplicate ) if the next number is increasing or diff <= 3, 
can be made safe

case 3: 1 3 2 4 5. in the case where descending and ascending order can be maintained by removing one, keep a flag
to make sure invariant is maintained by only removing one number

1 3 2 4 5 increasing order but decreasing pair
7 8 6 5 3 decreasin gorder but increasing pair

"""

still_unsafe = []
for report in unsafe:
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    negs, pos, zeros = 0, 0, 0
    for i in range(len(diffs)):
        diff = diffs[i]
        if diff > 0:
            pos += 1
        elif diff < 0:
            negs += 1
        else:
            zeros += 1

        if pos > 1 and negs > 1:
            still_unsafe.append(report)
            break

        if zeros > 1:
            still_unsafe.append(report)
            break

        if abs(diff) > 3:
            still_unsafe.append(report)
            break

print(len(reports) - len(still_unsafe))
