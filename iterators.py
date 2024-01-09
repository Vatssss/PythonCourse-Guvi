# iterator is an object which contains a countable number of values that can be iterated
# iterable--> list,tuple, dictionary

tuple1 = ("car", "bike", "train")
myit = iter(tuple1)
print(next(myit))
print(next(myit))
print(next(myit))

tuple2 = "apple"
# for x in tuple2:
#     print(x)
myiter = iter(tuple2)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class Number:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x= self.a
        self.a += 1
        return x


obj = Number()
print(obj.__iter__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())