#logical and, or, not

a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False
print(not b)    # True

x = 5
print(x > 0 and x < 10)  # True
print(x < 0 or x > 10)   # False
print(not (x == 5))      # False

y = 15
print(y >= 10 and y <= 20)  # True
print(y < 10 or y > 20)     # False
print(not (y != 15))        # True

if x > 0 and y > 10:
    print("Both conditions are true.")
    
if x < 0 or y > 10:
    print("At least one condition is true.")

if not (x < 0):
    print("x is not negative.")
    