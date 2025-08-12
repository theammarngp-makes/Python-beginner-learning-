#Lets make a code for guessing random number
import random
num = random.randint(1,100)

attempts = 0

while True :
guess = int(input('guess a random number from 1 to 100'))

 attempts += 1


 if (guess > num):
      print(' Too high for the number ')
 elif guess < num :
      print('Too low for the number')   
 else :
      print('correct  you  guess in' ,attempts , 'tries')
      break