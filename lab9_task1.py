class PrintLength(Exception):
    pass

class PrintAverage(Exception):
    pass

class PrintDispersion(Exception):
    pass

def CoProcess():
    length = 0
    summ = 0
    sqr_sum = 0
    try:
        while True:
            try:
                x = yield
                summ += x
                sqr_sum += x**2
                length += 1
            except PrintLength:
                yield length
            except PrintAverage:
                yield summ/length
            except PrintDispersion:
                yield sqr_sum/length-(summ/length)**2
                              
    finally:
        print("Current Length:", length)
        print("Current Average:", summ/length)
        print("Current Dispersion:", sqr_sum/length-(summ/length)**2)
    
coroutine = CoProcess()
next(coroutine)

##### TEST #####
i = input()
while i:
    if i.isdigit():
        coroutine.send(float(i))
    elif i == 'PrintLength':
        print("Current Length:", coroutine.throw(PrintLength))
        next(coroutine)
    elif i == 'PrintAverage':
        print("Current Average:", coroutine.throw(PrintAverage))
        next(coroutine)
    elif i == 'PrintDispersion':
        print("Current Dispersion:", coroutine.throw(PrintDispersion))
        next(coroutine)
    i = input()
coroutine.close()

