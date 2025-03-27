# Answer: 4719

# Complexity
# - Time:  O(m + n * k^2)
# - Space: O(m + k)
#
#   m = # of rules
#   j = # of distinct pages mentioned in the rules, where j <= 2*m
#   n = # of lines of pages
#   k = # of pages on a line, where k <= j
#
# Approach: We want to identify the invalid lines, re-order them according to the rules, and sum the middle vales
#           once they've been re-ordered. Identifying the invalid lines and summing their (fixed) middles are easy
#           tasks - we already solved them in part 1.
#
#           Thoughts on how to approach re-ordering:
#
#           Idea 1: We could look up each page in the rule dict and filter its followers by only those values in 
#                   the invalid line. We count the filtered followers for each page. We sort the pages according 
#                   to follower count, and this is the fixed line
#   
#           Idea 2: I like this one better. We examine each pair of pages in each line, as before, but now we
#                   initialize the "index" of each page to 0. Whenever we find a pair that exists as a rule, we
#                   increment the index of the follower. We do this whether the pair is in the correct order or not.
#                   We still notice whether a line is valid or not. If a line is invalid, once we're done examining 
#                   all of the pairs we re-sort the line according to their index ascending. Actually, instead of an 
#                   O(nlogn) resort, we can just iterate through the list until we find the page with the middle index
#                   (this assumes there is a rule for all page pairs)
#
#                   This has the same time complexity as part 1 and needs only a bit more space (the k term)

def sumOfInvalidPages1(rules, pages):
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
        line_tup = [[0, page] for page in line]
        k = len(line)
        valid = True
        for i in range(k-1):
            for j in range(i,k):
                if line[j] in rule_dict and line[i] in rule_dict[line[j]]:
                    valid = False
                    line_tup[i][0] += 1
                elif line[i] in rule_dict and line[j] in rule_dict[line[i]]:
                    line_tup[j][0] += 1
        if not valid:
            # print('line is not valid: ' + str(line))
            for idx, page in line_tup:
                if idx == k//2:
                    total += page
            #         print('  middle element is: ' + str(page))

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

count = sumOfInvalidPages1(rules, pages)
print("\nThe output is: " + str(count))