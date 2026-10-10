

with open("file.txt","r") as f:
    content = f.read()
    print(content)


# line by line reading
with open("file.txt","r") as f:
    for line in f:
        print(line.strip())


#Write to a file


with open("file.txt" , "w") as f:
    f.write("Hello , file \n")
    f.write("Another line")

with open("output.txt", "a") as f:
    f.write("New Line Added \n")


