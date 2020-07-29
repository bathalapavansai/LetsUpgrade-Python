givenList = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
givenList.sort()
a=givenList.copy()
z=givenList.count(0)
Ans=a[z:]
for i in range(z):
    Ans.append(0)
print(Ans)
