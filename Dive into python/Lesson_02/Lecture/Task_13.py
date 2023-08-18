"""
complex([real[, imag]]) — комплексное число
из действительной real и мнимой imag частей.
"""

a = complex(2, 3) # (2+3j)
b = complex('2+3j') # (2+3j)
print(a, b, a == b, sep='\n') # True

