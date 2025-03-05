# Answer: 1945

# Complexity
# - Time:  O(n * m) where n = # of rows, m = # of cols. Each countCrosses() call takes O(1) time
# - Space: O(1), just constant space needed for rows, cols, and count
# Approach: Examine each char of input except in first/last row and first/last col. If the char is A, it's a candidate for having 2
#           crossed "MAS" terms. Check each of 4 possible orientations (Ms on left/right/top/bottom, Ss opposing)
def countCrossMAS(wordsearch):
    def countCrosses(i, j):
        # M on the left, S on the right
        if wordsearch[i-1][j-1] == wordsearch[i+1][j-1] == 'M' and wordsearch[i+1][j+1] == wordsearch[i-1][j+1] == 'S':
            # print('Found Ms on left, Ss on right at ' + str(i) + ', ' + str(j))
            return 1

        # M on the right, S on the left
        if wordsearch[i-1][j-1] == wordsearch[i+1][j-1] == 'S' and wordsearch[i+1][j+1] == wordsearch[i-1][j+1] == 'M':
            # print('Found Ms on right, Ss on left at ' + str(i) + ', ' + str(j))
            return 1

        # M on top, S on bottom
        if wordsearch[i-1][j-1] == wordsearch[i-1][j+1] == 'M' and wordsearch[i+1][j-1] == wordsearch[i+1][j+1] == 'S':
            # print('Found Ms on top, Ss on bottom at ' + str(i) + ', ' + str(j))
            return 1

        # M on bottom, S on top
        if wordsearch[i-1][j-1] == wordsearch[i-1][j+1] == 'S' and wordsearch[i+1][j-1] == wordsearch[i+1][j+1] == 'M':
            # print('Found Ms on bottom, Ss on top at ' + str(i) + ', ' + str(j))
            return 1

        return 0

    rows = len(wordsearch)
    cols = len(wordsearch[0])
    count = 0
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if wordsearch[i][j] == 'A':
                count += countCrosses(i,j)
                pass
    return count

input_path = '../inputs/2024_day4.txt'
# input_path = '../inputs/2024_day4_test.txt'
wordsearch = []
for line in open(input_path):
    row = []
    for char in line:
        if char in ['X', 'M', 'A', 'S']:
            row.append(char)
    wordsearch.append(row)
count = countCrossMAS(wordsearch)
print("The # of times \"MAS\" is crossed in the wordsearch is: " + str(count))