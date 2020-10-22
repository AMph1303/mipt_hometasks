def author(decorator_arg1):
    def decorator(func):
        func._author = decorator_arg1
        return func
    return decorator

NAME = input()
@author(NAME)
def add2(num: int) -> int: 
     return num + 2

add2(2)
print(add2._author)

