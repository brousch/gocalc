#!/usr/bin/env python

def iz(x):
    '''
    :param x: string with integer, integer, or None
    :return: Value of x as integer or 0
    '''
    try:
        return int(x)
    except:
        return 0

def fz(x):
    '''
    :param x: string with float, float, or None
    :return: Value of x as float or 0
    '''
    try:
        return float(x)
    except:
        return 0