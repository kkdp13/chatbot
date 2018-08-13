# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#print(len(currencies))
#i = 0
#
#print(currencies[i])
#i = i + 1
#print(currencies[i])
#i = i + 1
#print(currencies[i])
#i = i + 1
#print(currencies[i])
#i = i + 1
#print(currencies[i])
#i = i + 1
#print(currencies[i])
#i = i + 1
#print(i)
#
#for letter in currencies:     # First Example
#   print('Current Letter :', letter)

#a = 'i'
#b = 'j'
#d = 'h'
#f = 'k'
#
#new = a+b
#
#print(new)
#
#new = new+d+f
#
#print(new)
def getnewcurrency(currencies):
    
    newcurrency = ''
    for currency in currencies:
        if currency == '0':
            newcurrency = newcurrency + currency
        elif currency == '1':
            newcurrency = newcurrency + currency
        elif currency == '2':
            newcurrency = newcurrency + currency
        elif currency == '3':
            newcurrency = newcurrency + currency
        elif currency == '4':
            newcurrency = newcurrency + currency
        elif currency == '5':
            newcurrency = newcurrency + currency
        elif currency == '6':
            newcurrency = newcurrency + currency
        elif currency == '7':
            newcurrency = newcurrency + currency
        elif currency == '8':
            newcurrency = newcurrency + currency
        elif currency == '9':
            newcurrency = newcurrency + currency
        elif currency == '0':
            newcurrency = newcurrency + currency
        elif currency == '.':
            newcurrency = newcurrency + currency
    return newcurrency
    
#    print(newcurrency)        



