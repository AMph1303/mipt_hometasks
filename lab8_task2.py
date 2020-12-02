def ConsoleGenerator():
    num = input()
    while len(num):
        yield float(num)
        num = input()
        
total_sum = 0
for number in ConsoleGenerator():
    total_sum += number
print(f'Sum of entered numbers is {total_sum}')
