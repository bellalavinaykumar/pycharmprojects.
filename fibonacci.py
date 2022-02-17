def fib(n):
    a = 0
    b = 1
    if n==0 or n==1:
        print(0)
    else:
        print(a)
        print(b)
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
        print(c)
fib(4)
