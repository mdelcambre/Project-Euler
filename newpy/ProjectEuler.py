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


def p3():
    'Finds the largest prime factor of 600851475143'
    print "Running Problem 3:"

    a = 2
    num = 600851475143
    largest_factor = 0
    while a < num:
        if num%a == 0:
            num = num/a
            largest_factor = a
            continue
        a += 1
    print largest_factor if num < largest_factor else num

def p4():
    'Finds the largest palandrome product of 3 digit numbers'
    print "Running Problem 4:"
    for i in range(999*999,100*100,-1):
        i_str = str(i)
        sub1 = i_str[0:int(len(i_str)/2)]
        sub2 = i_str[:-int(len(i_str)/2)-1:-1]
        if sub1 == sub2:
            for j in range(999,100,-1):
                if i%j==0 and len(str(i/j))==3:
                    print i
                    return 0

def p5():
    'Finds the smallest common multiple of 1 through 20'
    print "Running Problem 5:"
    """Prime factors of 1-20:
    2
    3
    2*2
    5
    2*3
    7
    2*2*2
    3*3
    2*5
    11
    2*2*3
    13
    2*7
    3*5
    2*2*2*2
    17
    3*3*2
    19
    2*2*5
    Take the minimum number of each prime to get each number, multiply """
    print 2*2*2*2*3*3*5*7*11*13*17*19

def p6():
    ''


if __name__ == "__main__":
    try:
        arg1 = int(sys.argv[1])
    except:
        raise Exception("Script takes a natural number as the only argument")
    eval("p%s()" % (arg1))

