import re
s = input()
print(re.findall(r'\d+(?=[₽])|\d+(?= ₽)|(?<=[$€])\d*', s))
