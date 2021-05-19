'''
Function:       Generate random passwords based on of the length given
Date:           02.01.2019
Created By:     Anonymous Systems
'''
import os
import string
import random

def generatePassword(numberofpasswords, length):
    chars = string.ascii_letters +string.digits + '!@#$%^&*()'
    for pwd in range(numberofpasswords):
        password = ''
        for char in range(length):
            password += random.choice(chars)
        print(password)

if __name__ == '__main__':
    numberofpasswords = int(input('How many passwords? '))
    length = int(input('Length of password(s)? '))
    print('Passwords will be printed below:')
    print(25 * '=')
    generatePassword(numberofpasswords, length)
