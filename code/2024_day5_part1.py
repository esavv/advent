# Answer: 5964

# Complexity
# - Time:  O(m + n * k^2)
# - Space: O(m)
#
#   m = # of rules
#   j = # of distinct pages mentioned in the rules, where j <= 2*m
#   n = # of lines of pages
#   k = # of pages on a line, where k <= j
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
#           
#           Idea 2: It might be faster if we could combine all of the rules into a single rule. For example, the 21 test rules
#                   imply this "fully expressed" rule string:
#
#                       97, 75, 47, 61, 53, 29, 13
#
#                   Then, we could iterate through each element in each line of pages and look for it in the rule string starting
#                   at a given index. That index starts at 0 but is incremented to the position of the last found element. If we
#                   fail to find an element in the rule string starting from the given index, then the line violates the rules and
#                   can be discarded. If we find all elements then the rule is valid and we can add its middle element to the total
#       
#                   Not sure if this is actually faster, though. It probably depends. If j is the # of distinct pages (and thus the
#                   length of the single rule string) then - without considering the cost of the generating the rule string -
#                   validating the pages takes O(n * (k + j)) = O(n * k + n * j). We have the (k + j) term here because in a given
#                   line we process all k pages in the line and also iterate through all j pages in the rule string, but we only do
#                   each iteration once - we don't do a full rule string iteration k times. In the worst case j == k, so we have
#                   O(n * (k + k)) = O(n * k), which is a definite improvement from idea 1, provided that we can somehow generate
#                   the rule string in O(m) time... which I'm guessing we can't, as a new rule could require us to rescan 
#                   the current rule string and move some elements around. I'm guessing that we could probably generate the rule
#                   string in O(mlogm) time though, in which case our overall time complexity becomes O(mlogm + n * k) and thus it's
#                   unclear if this is preferable to idea 1. Forced to pick, I'd guess this *is* better because you'd think / hope
#                   that the # of rules is small compared to the # of different type of manuals proposed that might or might not
#                   conform to the rules, in which case you'd prefer to minimize the time complexity of the 2nd term (i.e. it's
#                   preferable to speed up processing of page lines over processing of rules)
#
#                   After some more thought, I think I *can* create the single rule in O(m) time using a bi-drectional linked
#                   list and a hash table to index into the list in O(1) time
#                   
#                   After building & testing this... this doesn't work, because you * can't * compress the rules - they have cycles
#                   where if you try to apply all of the rules at once there are contradictions. I think the rules work because
#                   for any given input only some of the rules apply in such a way that cyles are... avoided? I think?
class ListNode:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

def compressRules(rules):
    head = tail = None
    rule_dict = {}
    for first, second in rules:
        # print("Compressing rule: " + str(first) + "|" + str(second))
        if not rule_dict:
            # create the nodes
            rule_dict[first] = ListNode(first)
            rule_dict[second] = ListNode(second)
            # attach them to each other
            rule_dict[first].next = rule_dict[second]
            rule_dict[second].prev = rule_dict[first]
            # assign head & tail for the first time
            head = rule_dict[first]
            tail = rule_dict[second]
        elif first not in rule_dict and second not in rule_dict:
            # create the nodes
            rule_dict[first] = ListNode(first)
            rule_dict[second] = ListNode(second)
            # attach them to each other
            rule_dict[first].next = rule_dict[second]
            rule_dict[second].prev = rule_dict[first]
            # attach them to the end of the list
            tail.next = rule_dict[first]
            rule_dict[first].prev = tail
            # update tail
            tail = rule_dict[second]
        elif first in rule_dict and second not in rule_dict:
            # create the node
            rule_dict[second] = ListNode(second)
            # attach it to the end of the list
            tail.next = rule_dict[second]
            rule_dict[second].prev = tail
            # update tail
            tail = rule_dict[second]
        elif first not in rule_dict and second in rule_dict:
            # create the node
            rule_dict[first] = ListNode(first)
            # attach first to the second, forward direction
            rule_dict[first].next = rule_dict[second]
            # check if second is the head. if yes, update the head
            if head == rule_dict[second]:
                head = rule_dict[first]
            # if not the head, point second's prev's next to first, and second's prev to first
            else:
                rule_dict[first].prev = rule_dict[second].prev
                rule_dict[second].prev.next = rule_dict[first]
            rule_dict[second].prev = rule_dict[first]
        else:
        # elif first in rule_dict and second in rule_dict:
            inorder = False
            curr = rule_dict[first]
            while curr:
                if curr == rule_dict[second]:
                    inorder = True
                curr = curr.next
            if not inorder:
                # move first immediately ahead of second
                # handle case where first is the tail
                if tail == rule_dict[first]:
                    rule_dict[first].prev.next = None
                    tail = rule_dict[first].prev
                else:
                    # extract first: point first's prev and next to one another
                    rule_dict[first].prev.next = rule_dict[first].next
                    rule_dict[first].next.prev = rule_dict[first].prev

                # attach first to the second, forward direction
                rule_dict[first].next = rule_dict[second]

                # handle case where second is the head
                if head == rule_dict[second]:
                    head = rule_dict[first]
                # if not the head, point second's prev's next to first, and second's prev to first
                else:
                    rule_dict[first].prev = rule_dict[second].prev
                    rule_dict[second].prev.next = rule_dict[first]
                rule_dict[second].prev = rule_dict[first]

    compressed_rules = []
    while head:
        compressed_rules.append(head.val)
        head = head.next
    return compressed_rules

def sumOfValidPages2(rules, pages):
    # rules: a list of length-2 lists of integers
    # pages: a list of lists of integers

    compressed = compressRules(rules)
    print("\nThe compressed rules are: " + str(compressed))

    total = 0

    for line in pages:
        k = len(line)
        valid = True

        idx = 0
        for page in line:
            while idx < len(compressed) and compressed[idx] != page:
                idx += 1
            if idx >= len(compressed):
                valid = False
                print('INVALID! because page ' + str(page) + ' incorrectly appears ahead of at least one preceding page')
                break

        if valid:
            print('line is valid')
            total += line[k//2]            

    return total

def sumOfValidPages1(rules, pages):
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
    step += 1

count = sumOfValidPages2(rules, pages)
print("\nThe output is: " + str(count))