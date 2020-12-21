import re
with open("test_task4.txt", 'r') as f, open('result.txt', 'w') as res:
    line = f.readline()
    while True:
        if re.match(r'шарик', line, flags=re.IGNORECASE):
            line = line[:-2:]
            print(line)
        res.write(line+'\n')
        line = f.readline()
