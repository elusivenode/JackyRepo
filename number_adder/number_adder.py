def add_to_int(i):
    n = list(range(1,i+1))
    s = sum(n)
    return s

with open('/Users/hamish.macdonald/Dev/JackyRepo/number_adder/sample_numbers.txt', 'r') as input_f:
    input_lines = input_f.readlines()

input_numbers = []
for l in input_lines[:]:
    input_numbers.append(int(l.strip()))

for n in input_numbers:
    print(f'Sum from 1 to {n} is {add_to_int(n)}.')