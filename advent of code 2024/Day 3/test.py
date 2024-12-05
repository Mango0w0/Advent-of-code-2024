#kenz's code
import re
f = open("Day 3/data.txt")
input_text = f.read()
f.close()

# part 2
def q2(input_text):
    
    input_text = "do()" + input_text + "don't()" # just nicer to wrap
    
    total = 0
    nums_pattern = r'mul\((\d+),(\d+)\)'
    section_pattern = r"do\(\)(.*?)don't\(\)"
    
    # find all sections that are activated (re.DOTALL does multiline check)
    # and then find mults within that
    for match in re.findall(section_pattern, input_text, re.DOTALL):
        for nums in re.findall(nums_pattern, match):
            total += int(nums[0]) * int(nums[1])
    return total 

print("Solution to q2: ", q2(input_text))