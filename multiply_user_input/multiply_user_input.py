def multiply_int(user_multiplier,other_number):
    return user_multiplier * other_number

with open('/Users/hamish.macdonald/Dev/JackyRepo/multiply_user_input/sample_numbers.txt', 'r') as input_f:
    input_lines = input_f.readlines()

user_number = input('Please enter an integer greater than 0: ')
user_number = int(user_number)
print(f'Your multiplier is: {user_number}')

input_numbers = []
for n in input_lines:
    input_numbers.append(int(n.strip()))

for n in input_numbers:
    print(f'input: {n} output: {multiply_int(user_number,n)}')