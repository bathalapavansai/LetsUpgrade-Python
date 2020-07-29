NoOfNumbers=int(input("No Of Numbers to add"))
NumberList=[]
for i in range(NoOfNumbers):
    x=int(input("enter sum number"))
    NumberList.append(x)
                      
summ=j=0                      
while (j<NoOfNumbers):
    summ=summ+NumberList[j]
    j+=1
print("sum of numbers",summ)    
