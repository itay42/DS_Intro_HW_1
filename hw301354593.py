# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 01:13:25 2022

@author: Etay
"""
##################### q1 #####################
def my_func(x1, x2, x3):
    try:
        if (type(x1) != float or type(x2) != float or type(x3) != float):
            print('Error: parameters should be float')
        elif(x1 + x2 + x3 == 0):
            print('Not a number – denominator equals zero')
        elif(True):
            return float(((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3))
    except:
        return

##################### q2 #####################
def convert(hours, minutes):
    if (hours < 0 or minutes < 0):
        print("Input error!")
    else:
        return hours * 60 * 60 + minutes * 60

        

   

