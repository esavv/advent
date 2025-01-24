# Complexity
# - Time:  O(nlogn)
# - Space: O(n) or O(logn) depending on sort algo
def getDistance(list1, list2):
    list1.sort()
    list2.sort()
    total = 0
    for i in range(len(list1)):
        dist = list1[i] - list2[i]
        if dist < 0:
            dist = -dist
        total += dist
    return total

input_path = '../inputs/2024_day1.txt'
list1, list2 = [], []
for line in open(input_path):
    row = line.split()
    list1.append(int(row[0]))
    list2.append(int(row[1]))
distance = getDistance(list1, list2)
print("The distance between the two lists is: " + str(distance))