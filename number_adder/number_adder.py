with open('/Users/hamish.macdonald/Dev/JackyRepo/number_adder/sample_numbers.txt', 'r') as input_f:
    input_lines = input_f.readlines()

input_numbers = []
for l in input_lines[:]:
    input_numbers.append(int(l.strip()))

print(input_numbers)