def arrayCheck(nums):
    return set([1,2,3]).issubset(set(nums))


print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))


def stringBits(str):
    return (str[::2])


print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))


def doubleChar(str):
    return ''.join([i * 2 for i in str])


print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))

def count_evens(nums):
    return sum(map(lambda num: num%2, nums))
