# functions as arguments
list = ["car", "bike", "scooter", "train"]

def loop(x):
    print(x*3)

# loop(list)

def map_func(y,list):
    for items in list:
        y(items)

map_func(loop, list)
