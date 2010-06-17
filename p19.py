#!/usr/bin/python

# number of sundays in a year on the first of a month, given an offset (non leap year)
sun_non_ly = [2, 1, 1, 3, 1, 2, 2]
# number of sundays in a year on the first of a month, given an offset (leap year)
sun_ly = [3, 1, 1, 2, 2, 1, 2]

offset = 5 # number of days from the 1st to sunday
sundays = 0

for year in range(1901,2001):
    leapyr = 1
    # make sure the offset is non negative (wrap it around if it is)
    if offset < 0:
        offset += 7
    # Standard rules for leap years (don't worry about the 100 except 400 rule, doesn't matter)
    if year % 4 == 0:
        leapyr = 0
    if leapyr == 1:
        sundays += sun_non_ly[offset]
        offset -= 1 # move the offset for the next year
    if leapyr == 0:
        sundays += sun_ly[offset]
        offset -= 2 # move the offset for the next year
        leapyr = 1
print sundays
