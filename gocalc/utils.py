#!/usr/bin/env python

def iz(x):
    '''
    :param x: Integer or None
    :return: Value of x as integer 0
    '''
    try:
        return int(x)
    except:
        return 0

def fz(x):
    '''
    :param x: Float or None
    :return: Value of x as float or 0
    '''
    try:
        return float(x)
    except:
        return 0