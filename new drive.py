list=[1,1,2,3,3,4,5,5]

def remove_dupicates(list):
    i=0
    for j in range(0,len(list)-1):
        if list[i]!=list[j+1]:
            i+=1
            list[i]=list[j+1]


remove_dupicates(list)
print(list)