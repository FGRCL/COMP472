import random

numbers = []
for i in range(6*3):
    numbers.append(i)

for i in range(3):
    random.shuffle(numbers)
    print(' '.join([str(number) for number in numbers]))