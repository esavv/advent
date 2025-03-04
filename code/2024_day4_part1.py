# Complexity
# - Time:  ?
# - Space: ?
# Approach:
def countXmas(wordsearch):
    rows = len(wordsearch)
    cols = len(wordsearch[0])
    term = "XMAS"

    def checkHorizontalForward(i, j):
        if j > cols - 4:
            return 0

        window = []
        for k in range(j, j+4):
            window.append(wordsearch[i][k])

        if ''.join(window) == term:
            # print('Found a horizontal forward starting at ' + str(i) + ', ' + str(j))
            return 1
        return 0

    def checkHorizontalBackward(i, j):
        if j < 3:
            return 0

        window = []
        for k in range(j, j-4, -1):
            window.append(wordsearch[i][k])

        if ''.join(window) == term:
            # print('Found a horizontal backward starting at ' + str(i) + ', ' + str(j))
            return 1
        return 0
    
    def checkVerticalDown(i, j):
        if i > rows - 4:
            return 0
        
        window = []
        for k in range(i, i+4):
            window.append(wordsearch[k][j])

        if ''.join(window) == term:
            # print('Found a vertical down starting at ' + str(i) + ', ' + str(j))
            return 1
        return 0
    
    def checkVerticalUp(i, j):
        if i < 3:
            return 0
        
        window = []
        for k in range(i, i-4, -1):
            window.append(wordsearch[k][j])

        if ''.join(window) == term:
            # print('Found a vertical up starting at ' + str(i) + ', ' + str(j))
            return 1
        return 0    
    
    def checkDiagonalSE(i, j):
        return 0
    def checkDiagonalSW(i, j):
        return 0
    def checkDiagonalNW(i, j):
        return 0
    def checkDiagonalNE(i, j):
        return 0

    count = 0
    for i in range(rows):
        for j in range(cols):
            if wordsearch[i][j] == 'X':
                count += checkHorizontalForward(i, j)
                count += checkHorizontalBackward(i, j)
                count += checkVerticalDown(i, j)
                count += checkVerticalUp(i, j)
                count += checkDiagonalSE(i, j)
                count += checkDiagonalSW(i, j)
                count += checkDiagonalNW(i, j)
                count += checkDiagonalNE(i, j)
                pass
    return count

# input_path = '../inputs/2024_day4.txt'
input_path = '../inputs/2024_day4_test.txt'
wordsearch = []
for line in open(input_path):
    row = []
    for char in line:
        if char in ['X', 'M', 'A', 'S']:
            row.append(char)
    wordsearch.append(row)
count = countXmas(wordsearch)
print("The # of times \"XMAS\" shows up in the wordsearch is: " + str(count))