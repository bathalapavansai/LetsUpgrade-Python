list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]

a=list1+list2
print(a)
i=0
while i<len(a)-1:
    if  a[i] > a[i+1]  :
        a[i] , a[i+1] = a[i+1], a[i]
        i=-1
    i+=1
    
print("after sort",[i for i in a])    
    
