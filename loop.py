
for i in range(5):
    print(i+1)

fruits = ["banana","orange","wtf"]


for fruit in fruits:
    print(fruit)


for i, fruit in enumerate(fruits):
    print(f"{i+1}: {fruit}")



count = 0
while count < 5:
    print(count)
    count += 1

# break and continue
for i in range(10):
    if i == 3:
        continue  # skip 3
    if i == 7:
        break     # stop at 7
    print(i)