#Simple calculator
#Input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
#Selecting operation
operations = input("Choose any operetions (/,*,+,-): ")

#adding conditionals 
#For addition
if operations == '+':
    print("Result:", a + b)

#For substraction
elif operations == '-':
    print ('Result:', a-b)
#For multiplication
elif operations == '':
    print ('Result:', a*b)
#For division
elif operations == '/':
    print ('Result:' , a/b )
else :
    print("You choosed invalid operation!!!!")
