#input() = a function that reads a line from input, converts it into a string (stripping a trailing newline), and returns that.

name = input("Please enter your name: ")  
age = input("Please enter your age: ")   
print(f"Hello, {name}!") 
print(f"You are {age} years old.")
print(f"Next year, you will be {int(age) + 1} years old.")