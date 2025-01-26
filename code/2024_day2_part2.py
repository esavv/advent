# Complexity
# - Time:  O(m * n)
# - Space: O(1)
# Ugly idea: Check if each report is completely safe. If yes, great. Otherwise, identify the two levels where
#   the first problem was encountered, and build 3 reports where each has one of the three previous levels removed,
#   and check whether they're each completely safe. If one is, great, if not, return False
def getSafeCount(reports):
    safe_count = 0

    def isSafe(report):
        if report[0] == report[1]:
            return False, 1
        increasing = True
        if report[0] > report[1]:
            increasing = False   

        n = len(report)     
        for i in range(1,n):
            if (increasing and report[i] <= report[i-1]) or (not increasing and report[i] >= report[i-1]):
                return False, i
            diff = report[i] - report[i-1]
            if diff > 3 or diff < -3:
                return False, i
        return True, -1

    for report in reports:
        safe, idx = isSafe(report)
        if safe:
            safe_count += 1
        else:
            safe1, _ = isSafe(report[:idx] + report[idx+1:])
            safe2, _ = isSafe(report[:idx-1] + report[idx:])
            safe3 = False
            if idx > 1:
                safe3, _ = isSafe(report[:idx-2] + report[idx-1:])
            if safe1 or safe2 or safe3:
                safe_count += 1
    return safe_count

input_path = '../inputs/2024_day2.txt'
reports = []
for line in open(input_path):
    report = line.split()
    reports.append([int(level) for level in report])
print("The number of reports is: " + str(len(reports)))
count = getSafeCount(reports)
print("The number of safe reports with at most 1 problem is: " + str(count))