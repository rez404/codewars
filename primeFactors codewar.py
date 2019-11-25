# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 02:26:57 2019

@author: rez

test.assert_equals(primeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
"""
def primeFactors(n):
    [ i  for i in np.arange(2,n+1)  if 0 not in np.array([i] * (i-2) ) % np.arange(2,i)]
    
    return print(i)
primeFactors(720)