# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:16:34 2021

@author: William
"""

while True:
    age = input('Enter your age: ')
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
    
while True:
    password = input('Select a new password (letters and numbers only, please): ')
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')