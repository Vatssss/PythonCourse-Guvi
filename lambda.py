# lamda can take multiple arguments but can have only one expression

x = lambda a: a ** 2

print(x(4))

y = lambda a, b, c, d: (a + b) * (c - d) + 10
print(y(1, 2, 3, 4))


# lambda funtion inside a function
def func(n):
    return lambda m, l: m * n + l


z = func(20)
print(z(2, 10))


# filter function: returns boolean in a list
# stores all the values which return true (boolean) in the filter.
def prime(x):
    for n in range(2, x):
        if x % n == 0:
            return False
    else:
        return True


filtered = filter(prime, range(100))
print("Prime numbers are", list(filtered))


# map
def squares(p):
    return p * p


l = [1, 2, 3, 4, 5, 6, 7]
listsquares = map(squares, l)
print(list(listsquares))
