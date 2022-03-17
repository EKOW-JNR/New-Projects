import random

print('Welcome To The Password Generator')

chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#%^.$*,?123456789'

number = input('Enter amount of passwords to generate:')

number = int(number)

length = input('Enter your desired password length:')
length = int(length)

print('\n Here are your passwords:')

for pwd in range (number):
    passwords=''
    for c in range (length):
     passwords +=random.choice(chars)
    print(passwords)