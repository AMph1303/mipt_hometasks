import re
s = input()
print(re.findall(r'(?<=[\"\'\«])[\w \s ]+(?=[\"\'\»])', s))
