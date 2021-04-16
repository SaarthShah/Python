list=[2,3,4,5,2,1,3,5,6,69,54,32,32]
uniques=[]
flag=0
for item in list:
    flag=0
    for item1 in uniques:
        if item==item1:
            flag=flag+1
    if flag==0:
        uniques.append(item)

uniques.sort()
print(uniques)
