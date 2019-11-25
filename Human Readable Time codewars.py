#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")
"""

def make_readable(seconds):

    if len(str(seconds//3600))==1:
        a="0"+str(seconds//3600)
        
    if len(str(int((seconds%3600)/60)))==1:
        b="0" + str(int((seconds%3600)/60))
        
    if len(str(seconds%60))==1:
        c="0"+str((seconds%60))
    else:
        return "{}:{}:{}".format(seconds//3600,int((seconds%3600)/60),seconds%60)
    return "{}:{}:{}".format(a,b,c)

print(make_readable(86399))

#%%

# integer numbers with minimum width
print("{:5d}".format(12))

# width doesn't work for numbers longer than padding
print("{:7d}".format(1234))

# padding for float numbers
print("{:8.3f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))





