list=[4,5,6,8,9,6]
pos=0
def search(list,val):
    global pos
    for i in list:
        pos+=1
        if val==i:
            return True
    else:
        return False

result=search(list,9)

if result:
    print("found at ",pos)
else:
    print("not found")

