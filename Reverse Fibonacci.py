def fib(x):
    if x<=1:
        return x
    else:
        return fib(x-1) + fib(x-2)
def revf(x):
    if x<=1:
        print fib(x)
    else:
        print fib(x)
        revf(x-1)
