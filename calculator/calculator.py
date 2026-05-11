#Simple calculator
#Input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operetions = input("Choose any operetions (/,*,+,-): ")

#adding conditionals 

if operations == '+':
    print("Result:", a + b)

elif operations == '-':
    print ('Result:', a-b)

elif operations == '':
    print ('Result:', a*b)

elif operations == '/':
    print ('Result:' , a/b )
