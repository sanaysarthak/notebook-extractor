# Program to format a string with placeholders
x = 10
y = 3.14
z = "Python"
print("x is {}, y is {}, and z is {}".format(x, y, z)) # use {} as placeholders
print("x is {0}, y is {1}, and z is {2}".format(x, y, z)) # use {n} as placeholders with index
print("x is {a}, y is {b}, and z is {c}".format(a=x, b=y, c=z)) # use {name} as placeholders with keyword arguments
print(f"x is {x}, y is {y}, and z is {z}") # use f-strings with expressions inside {}