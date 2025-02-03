def getSumProduct(memory):
    sumProduct = 0
    _do, _dont = "do()", "don't()"
    apply = True
    for entry in memory:
        i = 0
        while i < len(entry):
            # find the m or d
            while i < len(entry) and entry[i] not in ('m','d'):
                i += 1

            # if it's a d, check if it's a do/don't & apply it if so
            if i < len(entry) and entry[i] == 'd':
                if i < len(entry) - len(_do) and entry[i:i+len(_do)] == _do:
                    apply = True
                    i += len(_do)
                    continue
                if i < len(entry) - len(_dont) and entry[i:i+len(_dont)] == _dont:
                    apply = False
                    i += len(_dont)
                    continue
                i += 1
                continue

            # otherwise, we've found the m, so now find 'mul('
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
            if apply:
                sumProduct += int(num1Str) * int(num2Str)
    return sumProduct

input_path = '../inputs/2024_day3.txt'
memory = []
for line in open(input_path):
    memory.append(line)
# test_memory = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
# print("Test memory is: " + test_memory[0])
# sumProduct = getSumProduct(test_memory)
sumProduct = getSumProduct(memory)
print("The sum product of all instructions in memory is: " + str(sumProduct))