a = 10
b = 20

if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")

#shorthand
x,y = 21, 3
print("x") if x>y else print("y")

#with AND condition
if x>y and x>b and x>a:
    print("X is max")
