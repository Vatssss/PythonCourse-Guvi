# strip()
# split()
# capitalize()


# SQL: # Create a table (if not exists)
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     age INT
# )
# '''


import os

f = open("trial.txt", "r")
num = f.readline()
f.close()
g = open("trial.txt", "a")
for i in num:
    if i == '1':
        g.write("one")
    elif i == '2':
        g.write("two")
    elif i == '3':
        g.write("three")
    elif i == '4':
        g.write("four")
    elif i == '5':
        g.write("five")
    elif i == '6':
        g.write("six")
    elif i == '7':
        g.write("seven")
    elif i == '8':
        g.write("eight")
    elif i == '9':
        g.write("nine")
    else:
        g.write("")


