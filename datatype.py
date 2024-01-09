#This is a single line comment
"""
This is
a
Multi-line String
"""

#but if we assign a variable to the above string:
a = """This is
also
a Multi-line String 
but ASSIGNED to variable a"""

print(a)

#Now let's look at some datatypes for numbers --> int, float, complex defined as
x = 1
y = 1.0
z = 1j    #j is used for imaginary part of a complex number.

print(type(x))
print(x)

print(type(y))
print(y)

print(type(z))
print(z)

#typecasting
#converting datatypes (from int to float)
a = float(x)
print(a)
print(type(a))

#from int to complex
b = complex(x)
print(b)
print(type(b))


