x = """Apple is
red in
Color."""
y = '''Mangoes are
yellow in
color'''
print(x)
print(y)

a = "Hello, World!"
print(a[7])
print(a[12])
print(a[2:8])

#loop
for x in a:
    print(x)

#to search if a text is present in the string
print("llo" in a)
print("meow" in a)

#to print the length of a string
print(len(a))

#to change in uppercase and lowercase
print(a.upper())
print(a.lower())

#to replace a text with other in a string
print(a.replace("Hello", "Bye"))

#concatenation
b = "Hi"
c = "User"
print(b+" "+c+"!!!")

#escape characters
d = "hello\nhey"
print(d)
e = "\x48\x45\x52\x52\x55"
print(e)