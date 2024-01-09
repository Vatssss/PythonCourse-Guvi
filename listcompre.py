# new list from an existing list

newfruits=[]
fruits=["apple","banana","kiwi"]
for x in fruits:
    if "a" in x:
        newfruits.append(x)

print(newfruits)

# list comprehension
newfruit = [x for x in fruits if "i" in x]
print(newfruit)

new =[x for x in fruits if x!="banana"]
print(new)

n =[x.upper() for x in fruits]
print(n)

replace = [x if x!="banana" else "orange" for x in fruits]
print(replace)

