import os
f = open("trial.txt", "r")

# # 10 characters
# print(f.read(10))

# read line
print(f.readline())

f.close()

x = open("trial.txt", "a")
x.write("line10")
x.close()

y = open("trial.txt", "r")
print(y.read())

# "w" for overwriting or create and write if not created

# p = open("new.txt", "x")
y.close()
# p.close()

# os.remove("new.txt")
