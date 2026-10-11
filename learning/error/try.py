


try:
    result = 10/0;
except ZeroDivisionError:
    print("Can not be devided by 0 !!")

try:
    number = int(input("Enter a number"))
except ValueError:
    print("That's not a valid number!!")

finally:
    print("This always runs")


"""
Works just try running 

make sure you are in same folder
i dont know if its python or python3
python3 try.py

"""