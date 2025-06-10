'''def log(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper
@log
def add(a,b):
    return a + b
add(4,5)
        
'''
def log(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    c = a+b
    return c

print(add(a=4,b=14))
