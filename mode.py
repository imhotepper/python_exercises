def mode(numbers:list):
    if not numbers: return None

    numbers_dict = {}
    for n in numbers:
        numbers_dict[n] = 1 if n not in numbers_dict.keys() else numbers_dict[n] + 1
   
    mx = 0
    med = 0
    for k,v in numbers_dict.items():
        if v > mx: 
            mx = v
            med = k
    return med

        
assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4