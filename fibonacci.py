def fib(n):
    if n <= 1:
        print("invalid number")
    elif n == 1:
        print("fib is 1")
    else:
        a = 0
        b = 1
        for i in range (2,n):
            c = a + b
            a = b
            b = c
            if c <= 10:
             print(c)
            else:
             break
x = int(input("enter last range for fibnnoci   >>  "))
fib(x)








