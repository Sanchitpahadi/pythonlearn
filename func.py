def greet(name, greetin = "hello"):
    print(f"{greetin} {name} How are you mf???")

def askname():
    return input("whats yout name???")

def min_max(numbers):
    return min(numbers), max(numbers)

def sum_all(*args):
    return sum(args)

def describe(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


low, high = min_max([3, 1, 9, 5])
print(low, high) 
     

name = askname()
greet(name)

name2 = askname()
greet(name2,"suppp")

name3 = askname()
greet(name3,"buddy")

print(sum_all(1, 2, 3, 4))
describe(name="Alice", age=25, city="Kathmandu")