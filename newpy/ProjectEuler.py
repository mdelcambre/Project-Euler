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
    'Sum square difference'
    print "Running Problem 6:"
    a = 0
    b = 0
    for i in range(1,101):
        a += i**2
        b += i
    print (b**2)-a

def p7():
    'Finds the 10001 prime'
    print "Running Problem 7:"
    primes = [2]
    i = 1
    isprime = True
    while len(primes) < 10001:
        i += 1
        for prime in primes:
            if i%prime == 0:
                isprime = False
                break
        if isprime:
            primes.append(i)
        isprime = True
    print primes.pop()

def p8():
    'Finds the largest product of 13 consecutive digits of a given integer'
    print "Running Problem 8:"
    string = "73167176531330624919225119674426574742355349194934"\
          "96983520312774506326239578318016984801869478851843"\
          "85861560789112949495459501737958331952853208805511"\
          "12540698747158523863050715693290963295227443043557"\
          "66896648950445244523161731856403098711121722383113"\
          "62229893423380308135336276614282806444486645238749"\
          "30358907296290491560440772390713810515859307960866"\
          "70172427121883998797908792274921901699720888093776"\
          "65727333001053367881220235421809751254540594752243"\
          "52584907711670556013604839586446706324415722155397"\
          "53697817977846174064955149290862569321978468622482"\
          "83972241375657056057490261407972968652414535100474"\
          "82166370484403199890008895243450658541227588666881"\
          "16427171479924442928230863465674813919123162824586"\
          "17866458359124566529476545682848912883142607690042"\
          "24219022671055626321111109370544217506941658960408"\
          "07198403850962455444362981230987879927244284909188"\
          "84580156166097919133875499200524063689912560717606"\
          "05886116467109405077541002256983155200055935729725"\
          "71636269561882670428252483600823257530420752963450"
    max_product = 0
    for sub in range(13,len(string)):
        product = reduce(lambda x,y: int(x)*int(y),list(string[sub-13:sub]))
        max_product = product if product > max_product else max_product
    print max_product



if __name__ == "__main__":
    try:
        arg1 = int(sys.argv[1])
    except:
        raise Exception("Script takes a natural number as the only argument")
    eval("p%s()" % (arg1))

