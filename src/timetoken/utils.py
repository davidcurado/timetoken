# -*- coding: utf-8 -*-
'''
Created on Mar 7, 2015
@author: José David Fernández Curado
'''

elements = '0123456789abcdefghijklmnopqrstuvwxyz'

def int_to_base36(num):
    parts = []
    if num == 0:
        parts.append(elements[0])
    while num > 0:
        parts.append(elements[num % 36])
        num /= 36
    parts.reverse()
    return ''.join(parts)

def base36_to_int(num):
    val = 0
    for i in range(0, len(num)):
        if num[i] not in elements:
            raise ValueError
        val = elements.index(num[i]) + val * 36
    return val
