#minitask 7

def deprecated(func):
    def inner(*args, **kwargs):
        print("Call to deprecated function: " + func.__name__)
        print(func(*args, **kwargs))
        return
    return inner


@deprecated
def some_old_function(x, y):
    return x + y

some_old_function(1,2)

# should write:
# Call to deprecated function: some_old_function
# 3
