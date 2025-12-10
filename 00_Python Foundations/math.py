#Some built-in math functions
from sys import maxunicode
import math

x = 3.14
y = -4
z = 5

#round x to the nearest whole integer
result = round(x)
print(result)

#get the absolute value of y
result = abs(y)
print(result)

#power function
#pow(base, exponent)
result = pow(4, 3)
print(result)

#find min and max
minValue = min(x, y, z)
maxValue = max(x, y, z)

print(f"{minValue}, {maxValue}")

#Math constant from Math module
print(math.pi)
print(math.e)

#Square Root
print(math.sqrt(4))

#Ceiling and Flooring
print(math.ceil(3.14))
print(math.floor(3.14))