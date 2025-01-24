# Complexity
# - Time:  O(n)
# - Space: O(n) - if the values in list1 are mostly distinct
def getSimilarityScore(list1, list2):
    # Compute the frequency of each distinct val in list1 in list 2
    freq = {}
    for val in list1:
        freq[val] = 0
    for val in list2:
        if val in freq:
            freq[val] += 1

    # Then, iterate through each val in list1 and add its similarity to running total
    score = 0
    for val in list1:
        score += val * freq[val]
    return score

input_path = '../inputs/2024_day1.txt'
list1, list2 = [], []
for line in open(input_path):
    row = line.split()
    list1.append(int(row[0]))
    list2.append(int(row[1]))
score = getSimilarityScore(list1, list2)
print("The similarity score of list1 given list2 is: " + str(score))