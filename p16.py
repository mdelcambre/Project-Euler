#!/usr/bin/python
sum = 0
num = 2**1000
num_str = str(num)
for digit in num_str:
    sum += int(digit)
print sum
