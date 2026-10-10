person = {
    "name": "Sanc",
    "age" : "19",
    "city":"Bhaktapur"

}


print(person["name"])

print(person.get("jobs","N / A"))

person["email"] = "alice@example.com"

person["age"] = 26

del person["city"]


for key,value in person.items():
    print(f"{key}:{value}")


squares = {x : x**2 for x in range(5)}

print(squares)