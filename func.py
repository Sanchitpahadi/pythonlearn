def greet(name, greetin = "hello"):
    print(f"{greetin} {name} How are you mf???")

def askname():
    return input("whats yout name???")

def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 5])
print(low, high) 
     

name = askname()
greet(name)

name2 = askname()
greet(name2,"suppp")

name3 = askname()
greet(name3,"buddy")

