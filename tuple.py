#tuple uses round brackets
#values of tuple are unchangable

t =("car",2,3, 9.0, True)
print(t)
print(type(t))

print(t[0])
print(t[1:4])

# tuple.append("hi")
# doesn't work as tuples are unchangable

x = list(t)
x[1]="bike"
y = tuple(x)
print(x)
