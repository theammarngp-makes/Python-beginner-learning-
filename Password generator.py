#Random password generator

import random
import string

#These function will call digits punctuations and letters

ch=(string.ascii_letters)+(string.digits)+(string.punctuation)

#Lets make a loop for 12 len password
passlen = int(input('Enter length of your password :'))
#password =' '
#for i in range(passlen):
#      password += random.choice(ch)
x =''.join([random.choice(ch)for i in range (passlen)])
print('Your random password is :',x)