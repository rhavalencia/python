#try Code that may raise an error.
try:
    result = 10 / 0
    print(result)

#try except Handles the error if one occurs.
except ZeroDivisionError:
    print("Cannot divide by 0")

#try except else Runs if no error occurs.
else:
    print("Division successful!")


#try except finally Runs regardless of whether an error occurred (useful for cleanup).
finally:
    print("Execution finished.")
