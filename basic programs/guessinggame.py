x= 69
t=0
flag=0
i=0
while i<3:
    t= int(input("Guess: "))
    if t==x:
        flag=flag+1
        break
    i=i+1

if flag==0:
    print('You failed try again')
else:
    print("You Won!")

