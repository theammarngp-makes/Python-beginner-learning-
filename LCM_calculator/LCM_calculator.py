# Program to find the Least Common Multiple (LCM) of two numbers
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

# Start with the higher of the two numbers
max_val = max(a, b)

while True:
    # Check if max_val is divisible by both a and b
    if max_val % a == 0 and max_val % b == 0:
        lcm = max_val
        break
    max_val += 1

print(f'LCM of {a} and {b} is {lcm}')
