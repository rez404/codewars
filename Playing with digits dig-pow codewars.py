# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:48:25 2019
test.assert_equals(dig_pow(89, 1), 1)
test.assert_equals(dig_pow(92, 1), -1)
test.assert_equals(dig_pow(46288, 3), 51)
@author: rez
"""
def dig_pow(n, p):
  s=0
  for i,c in enumerate(str(n)):
     s+= pow(int(c),p+i)
  return s/n if s%n==0 else -1

