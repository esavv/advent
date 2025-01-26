# Complexity
# - Time:  O(n) where n is # chars in memory
# - Space: O(1)
# Since we don't have to worry about nested multiplications, we can avoid stacks & recursion
# The approach here is some version of two pointers. We scan <left> until we find an 'm', and then
#   scan <right> until we find the ')' of a valid instruction or find an invalid character
#   If we find a valid instruction, execute it and add it to the total
# It seems we don't have to worry about leading 0s invalidating our instructions
def getSumProduct(memory):
    sumProduct = 0
    for entry in memory:
        i = 0
        while i < len(entry):
            # find the m
            while i < len(entry) and entry[i] != 'm':
                i += 1

            # we've found the m, now find 'mul('
            j = 0
            instr = 'mul('
            while i < len(entry) and j < 4 and entry[i] == instr[j]:
                i += 1
                j += 1
            if j < 4:
                continue

            # we've found 'mul(', now find num1
            num1Str = ''
            while i < len(entry) and ord('0') <= ord(entry[i]) <= ord('9'):
                num1Str += entry[i]
                i += 1
            if len(num1Str) == 0:
                continue
            
            # make sure the next char is a comma
            if i < len(entry) and entry[i] != ',':
                continue
            i += 1

            # we've found num1 & the comma, now find num2
            num2Str = ''
            while i < len(entry) and ord('0') <= ord(entry[i]) <= ord('9'):
                num2Str += entry[i]
                i += 1
            if len(num2Str) == 0:
                continue

            # make sure the next char is a closed paren
            if i < len(entry) and entry[i] != ')':
                continue

            # phew. if we've made it this far, we can compute a product
            sumProduct += int(num1Str) * int(num2Str)
    return sumProduct

input_path = '../inputs/2024_day3.txt'
memory = []
for line in open(input_path):
    memory.append(line)
# test_memory = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
# print("Test memory is: " + test_memory[0])
# sumProduct = getSumProduct(test_memory)
sumProduct = getSumProduct(memory)
print("The sum product of all instructions in memory is: " + str(sumProduct))