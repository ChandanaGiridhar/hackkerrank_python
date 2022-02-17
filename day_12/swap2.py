'''write a python program to swap 2 variables'''
a = int(input('enter value of a'))
b = int(input("enter value of b"))
print('Before swap: a = {} and b = {}'.format(a,b))
temp = a
a = b
b = temp
print('After swap: a = {} and b = {}'.format(a,b))
