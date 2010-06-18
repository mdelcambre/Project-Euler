#!/usr/bin/python

amicable = 0
for a in range(2,10001):
    print a
    divisorsA = [1]
    for div in range (2,a):
        if a % div == 0:
            divisorsA.append(div)
    b = 0
    for div in divisorsA:
        b += div
    if b < a:
        continue
    divisorsB = [1]
    for div in range(2,b):
        if b % div == 0:
            divisorsB.append(div)
    b_sum = 0
    for div in divisorsB:
        b_sum += div
    if b_sum == a and a != b:
        amicable += a + b
print amicable
