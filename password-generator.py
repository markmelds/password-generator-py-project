import random

print('Welcome to Your Password Generator')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+,<.>/?;:[{]}\|`~'
number = int(input("Enter the number of passwords to generate:"))
length= input("Enter the length of your password: ")
length = int(length)
print('\n Here are your passwords:')
for pwd in range(number):
    passwords= ''
    for c in range(length):
        passwords+=random.choice(chars)
    print(passwords)