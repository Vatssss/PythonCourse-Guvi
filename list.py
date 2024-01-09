#list is used to store multiple items in a single variable #like an array
# square brackets create a list
#values in list are changable.

list = [1,2,3,"apple",7.0,5.34,True]
print(list)
print(list[3])
print(list[2:6]) #for 2 to 5
print(len(list))
print(type(list))

list[2]= "Hi"
print(list)

list[4:6] = ["ate",False]
print(list)

#insertion
list.insert(2,"meow")
print(list)

list.append(False)
print(list)