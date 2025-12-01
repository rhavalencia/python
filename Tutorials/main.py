#print something in the console
print("Hello, welcome to the tutorial!")

#Variables
#Syntax: variable_name = value
print("#Variables")
print("Employee's Information System")

employee_name = input("Enter employee's name: ") #input() will take input from the user
employee_age = int(input("Enter employee's age: ")) #int() converts the input to an integer
employee_salary = float(input("Enter employee's salary: ")) #float() converts the input to a float
gender = input("Enter employee's gender (M/F): ")

print()
print("Employee's Name:", employee_name)
print("Employee's Age:", employee_age)
print("Employee's Salary: PHP {:.2f}".format(employee_salary)) #format() is used to format the float to 2 decimal places
print("Employee's Gender:", gender)