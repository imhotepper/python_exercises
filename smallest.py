
def getSmallest(numbers:list):
    if not numbers:
        return None
    sm = bg = numbers[0]
    for x in numbers:
        if x > bg: bg = x
        if x <= sm: sm = x
    return sm

def getBiggest(numbers:list):
    if len(numbers) == 0:
        return None
    bg = numbers[0]
    for x in numbers:
        if x > bg: bg = x    
    return bg

assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None

