import re

f = open('Day 3/data.txt', 'r')
dataSet = f.read()
f.close()


mulList = re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", dataSet)

total = 0

for mul in mulList:
    total += (int(mul[0]) * int(mul[1]))
    
print(total)