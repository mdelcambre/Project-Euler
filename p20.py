#!/usr/bin/python
n = 100
fac = 1
while n > 1:
    fac *= n
    n -= 1
sum = 0
fac_str = str(fac)
for digit in fac_str:
    sum += int(digit)
print sum
