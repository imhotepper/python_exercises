import random, smallest

numbers = []
mx = 10000000

for i in range(mx):
    numbers.append(random.randint(1, mx))

print('Numbers:', numbers)
print(f'Smallest is:{smallest.getSmallest(numbers)}')
