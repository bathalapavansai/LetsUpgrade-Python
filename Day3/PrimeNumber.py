findAns=int(input("enter number to find prime or not : "))

count=0

for i in range(1,findAns):
        if ((findAns%i)==0):
            count+=1
if(count==1):
    print("Prime")
else:
    print("Not Prime")
