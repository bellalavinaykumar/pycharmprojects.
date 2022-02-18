def genetators():
    i=10
    while i>=1:
        yield i
        i-=1

val=genetators()

for i in val:
    print(i)
