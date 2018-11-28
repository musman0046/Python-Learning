
"""
__author__      = Muhammad Usman
__copyright__   = Copyright 2007, Private
__date__        = 10, May 2018
__version__     = 1.0.0
__desc__        = Basic Implementation of python decorater
"""

def decorater(fun):

    def wrap(a,b):

        print("some thing happens before function decorate")
        if b == 0:
            return False
        return fun(a, b)
    return wrap


@decorater
def add(a,b):
    return "divide result is" , int(a/b)


res=add(2,2)
print(res)