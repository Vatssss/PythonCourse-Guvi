# prime or not

# if n is number
# n should be divided from 2 to n-1
# if n is divisible by any number between 2 to n-1, it is not prime (using % operator)

# loop variable that iterates from 2 to n-1 (or check for n/2)

x = 121
for i in range(2, x):
    if x % i == 0:
        print(x, "is NOT prime")
        break
else:
    print(x, "is prime")




