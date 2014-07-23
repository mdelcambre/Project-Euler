#!/usr/bin/python
sum = 1
d = 1
for i in range(2,1001,2):
    a = d + i
    b = a + i
    c = b + i
    d = c + i
    sum += a + b + c + d
print sum
