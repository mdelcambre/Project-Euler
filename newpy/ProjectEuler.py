#!/usr/bin/env python
import sys

def p1():
    'Calculates the sum of the multiples of 3 and 5 from 0 to 1000'
    print "Running Problem 1:"
    sum_mult = 0
    for i in range(1,1000):
        if i%5 == 0 or i%3 == 0:
            sum_mult += i
    print sum_mult

def p2():
    'Calculates the sum of even fibinocci numbers <4,000,000'

    print "Running Problem 2:"
    a,b = (1,0)
    sum_fib = 0
    while a < 4000000:
        if a%2 == 0:
            sum_fib += a
        (a,b) = (a+b,a)
    print sum_fib






if __name__ == "__main__":
    try:
        arg1 = int(sys.argv[1])
    except:
        raise Exception("Script takes a natural number as the only argument")
    eval("p%s()" % (arg1))

