# Complexity
# - Time:  O(m * n)
# - Space: O(1)
def getSafeCount(reports):
    safe_count = 0

    def isSafe(report):
        if report[0] == report[1]:
            return False
        increasing = True
        if report[0] > report[1]:
            increasing = False   

        n = len(report)     
        for i in range(1,n):
            if (increasing and report[i] <= report[i-1]) or (not increasing and report[i] >= report[i-1]):
                return False
            diff = report[i] - report[i-1]
            if diff > 3 or diff < -3:
                return False
        return True

    for report in reports:
        if isSafe(report):
            safe_count += 1
    return safe_count

input_path = '../inputs/2024_day2.txt'
reports = []
for line in open(input_path):
    report = line.split()
    reports.append([int(level) for level in report])
print("The number of reports is: " + str(len(reports)))
count = getSafeCount(reports)
print("The number of safe reports is: " + str(count))