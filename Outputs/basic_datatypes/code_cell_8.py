# Program to convert between numeric data types
j = int(3.5) # convert float to int
k = float(4) # convert int to float
l = complex(5, 6) # convert int to float
m = complex(7.8, 9.1) # convert float to complex
n = int(l.real) # get the real part of complex as int
o = float(m.imag) # get the imaginary part of complex as float
print(j, k, l, m, n, o)