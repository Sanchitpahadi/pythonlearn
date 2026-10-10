


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

