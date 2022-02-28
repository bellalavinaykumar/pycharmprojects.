pos=-1
list=[2,6,8,12,15,21,25,30,33]
def binarysearch(list,n):
    f=0
    l=len(list)-1

    for i in range(len(list)):
        mid = (f + l) // 2
        if list[mid]==n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid]<n:
                f=mid+1
            else:
                l=mid-1
    return False
if binarysearch(list,25):
    print("found at ",pos)
else:
    print("element not found")