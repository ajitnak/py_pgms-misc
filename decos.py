from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        print("args = {}".format(args))
        print("kw = {}".format(kwargs))
        return func(*args, **kwargs)

    print(func.__name__ + " return logging")
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

print(f.__name__)  # prints 'f'
print(f.__doc__)   # prints 'does some math'

f(5)

