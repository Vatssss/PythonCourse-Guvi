class ABC:
    x = 5
    y = 10.0
    #Python is a runtime, dynamically typed language and hence doesn't require any explicit declaration of data types.
    #Python, determines the data type of variable at runtime rather than compile time, infers the input and assigns the corresponding data type to the variable.
    #This flexibility allows you to assign different types of values to the same variable throughout your code.

h = ABC()
print(h.x)
print(type(h.y))

class Human:
    # parameterized constructor
    def __init__(self, name,age):
        # self is similar to this
        self.name = name
        self.age = age

    def display(self):
        print("Hi, my name is "+self.name)


# object creation
z = Human("Vatsal", 19)
m = Human("Ananya", 20)

z.display()
m.display()

del z
del m

# z.display()

