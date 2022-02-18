list=[2,5,9,11,16,21,25]
pos=-1
n=25
def binary_search(list,n):
    l=0
    u=len(list)-1
    for i in range(len(list)):
        mid = (l + u) // 2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
if binary_search(list,n):
    print("found at",pos)
else:
    print("not found")