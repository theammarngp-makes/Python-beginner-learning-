#Program to find the Least Common Multiple (LCM) of two numbers
#First taking user inpupt of two numbers

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))

max_val = max(a,b)

#creating a loop until both a and b are divisible

while True :
if max_val % a == 0 and max_val % b ==0 :
lcm = max_val
break
max_val +=1
print('LCM OF' ,a,'and',b, 'is', lcm)