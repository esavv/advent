# Answer: 5964

# Complexity
# - Time:  O(m + n * k^2)
# - Space: O(m)
#
#   m = # of distinct rules, so 2*m is the maximum possible # of distinct pages
#   n = # of lines of pages
#   k = # of pages on a line
#
# Approach: We need to build a function that processes a set of rules, and then reads several lines of input and checks
#           whether each line of input conforms to the rules. If a line of input conforms, then identify its middle element
#           and add its value to a running total. Return the running total.
# 
#           Idea 1: A slow approach. Process the rules into a dictionary, where the keys are the first element of each rule
#                   and the values are sets of second elements. Iterate through each line of input. For every pair of values
#                   in the input - this would take O(k^2) time if k is the length of a line - check whether the pair exists
#                   in the dictionary in the "wrong" order - the second element of the pair is a key and the first is a value.
#                   If so, this is get a "miss"; skip the line and proceed to the next. If we get through the entire line
#                   without a miss, then identify the middle element and add it to the total. Return the total
#
#           Complexity analysis:                  
#               Time: O(m + n * k^2)
#                   O(m) to build the dictionary
#                   O(n) to process each line, and O(k^2) to process each pair of elements
#               Space: O(m)
#                   O(m) to build the dictionary; there are at most 2*m page #s added to the dict, either as keys or values
#                   O(1) space to scan the lines and add to a running total
def sumOfValidPages(rules, pages):
    # rules: a list of length-2 lists of integers
    # pages: a list of lists of integers

    rule_dict = {}
    for first, second in rules:
        if first in rule_dict:
            rule_dict[first].add(second)
        else:
            rule_dict[first] = set([second])

    total = 0

    for line in pages:
        k = len(line)
        valid = True
        for i in range(k-1):
            for j in range(i,k):
                if line[j] in rule_dict and line[i] in rule_dict[line[j]]:
                    valid = False
                    print('INVALID! due to rule ' + str(line[j]) + '|' + str(line[i]))
                    break
            if not valid:
                break
        if valid:
            print('line is valid')
            total += line[k//2]            

    return total

input_rules_path = '../inputs/2024_day5_rules.txt'
input_pages_path = '../inputs/2024_day5_pages.txt'
input_test_rules_path = '../inputs/2024_day5_test_rules.txt'
input_test_pages_path = '../inputs/2024_day5_test_pages.txt'
# input_rules_path, input_pages_path = input_test_rules_path, input_test_pages_path

rules = []
for line in open(input_rules_path):
    line = line.strip()
    rule = [int(x) for x in line.split("|")]
    rules.append(rule)

pages = []
for line in open(input_pages_path):
    line = line.strip()
    page_list = [int(x) for x in line.split(",")]
    pages.append(page_list)

count = sumOfValidPages(rules, pages)
print("\nThe output is: " + str(count))