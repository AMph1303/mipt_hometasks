def PipelineGenerator1(numbers):
    for i in numbers:
        if i >= 0:
            yield i**2
        
def PipelineGenerator2(numbers):
    for i in numbers:
        yield i%3
        

numbers = PipelineGenerator1([1, -2, 4, 3])

for i in PipelineGenerator2(numbers):
    print(i, end = " ")
