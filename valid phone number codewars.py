#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:08:45 2019

@author: rez

Instructions
Output
Write a function that accepts a string, and returns true if it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)

Examples:

validPhoneNumber("(123) 456-7890")  =>  returns true
validPhoneNumber("(1111)555 2345")  => returns false
validPhoneNumber("(098) 123 4567")  => returns false
"""

def validPhoneNumber(phoneNumber):
    liste=[]
    for i in phoneNumber:
        if i.isdigit()==True:
            liste.append(i)
        print(liste)
    if ("({}{}{}) {}{}{}-{}{}{}{}".format(*liste))==phoneNumber:
        return True
    else:
        return False

print(validPhoneNumber("(123) 456-7890"))