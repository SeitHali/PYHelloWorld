def fib(n):
    """Print a fib series some long shit"""
    a,b = 0,1
    result = []
    while (a<n):
        a,b=b,a+b
        result.append(a)
    return result

