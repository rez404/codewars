#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 23:34:31 2019

@author: rez,

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""

def create_phone_number(n):
    return "({}) {}-{}".format("".join(map(str,n[0:3])),"".join(map(str,n[3:6])),"".join(map(str,n[6:11])))
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))