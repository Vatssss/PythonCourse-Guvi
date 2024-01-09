# Palindrome:
# 1. Find reverse of a number
# 2. Compare reverse of a number with given number
# 3. If both equal then palindrome

# Now for a reverse:
# n = 151, rev = 0
# r = n % 10  -----> 151 % 10 = 1
# rev = rev * 10 + r ----> 0 * 10 + 1 = 1 -----> 1 * 10 + 5 = 15 -----> 15 * 10 + 1 = 151
# n = n//10  ----> 151 // 10 = (15.1) ---> 15
# REPEAT THE ABOVE STEPS TILL n > 0


def check_palindrome(x):
    rev = 0
    temp = x
    while temp > 0:
        r = temp % 10
        rev = rev * 10 + r
        temp = temp//10

    print(rev, "is the reversed number")

    if rev == x:
        print(x," is a palindrome number.")
    else:
        print(x, " is NOT a palindrome number.")


check_palindrome(1221)