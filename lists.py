


fruits = ["apple","banana","Orange"]

fruits.append("grape")

print(fruits)

fruits.insert(1,"avocado")

print(fruits)

fruits.pop()

print(fruits)

fruits.pop(0)

print(fruits)

"""
OUTPUT

['apple', 'banana', 'Orange', 'grape']
['apple', 'avocado', 'banana', 'Orange', 'grape']
['apple', 'avocado', 'banana', 'Orange']
['avocado', 'banana', 'Orange']

"""


print(len(fruits))

print(fruits[0])

print(fruits[-1])

print(fruits[1:3]) #slice might me usefull latter

"""
Output of above

3
avocado
Orange
['banana', 'Orange']

"""
squares = [x**2 for x in range(10)]

evens = [x for x in range (20) if x % 2 == 0]

print(squares)

print(evens)

"""
Output

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

"""