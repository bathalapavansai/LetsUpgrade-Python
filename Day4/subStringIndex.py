line=input("line : ")
pattern=input("substring : ")
lengths=line.split(pattern)
nextocc=1
for i in range(0,len(lengths)-1):
    print(nextocc+len(lengths[i]))
    nextocc+=len(lengths[i])+len(pattern)