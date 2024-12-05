import re

f = open('Day 3/data.txt', 'r')
dataSet = f.read()
f.close()

fart = "do()" + dataSet + "don't()"

total = 0

nums_pattern = r'mul\((\d+),(\d+)\)'
section_pattern = r"do\(\)(.*?)don't\(\)"


for match in re.findall(section_pattern, fart, re.DOTALL):
    for nums in re.findall(nums_pattern, match):
        total += int(nums[0]) * int(nums[1])

print(total)