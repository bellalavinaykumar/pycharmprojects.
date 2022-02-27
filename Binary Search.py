pos=-1
list=[2,6,8,12,15,21,25,30,33]
def binarysearch(list,n):

    f=0
    l=len(list)-1
    mid=(f+l)//2
    for i in range(len(list)):
        if n==list[mid]:
            globals()['pos'] = mid
            return True
        else:
            if n>mid:
                f=mid+1
            else:
                l=mid-1
    return False

if binarysearch(list,2):
    print("found at ",pos)
else:
    print("element not found")