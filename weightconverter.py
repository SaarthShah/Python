weight= int(input("Enter weight: "))
flag= int(input("Type 1 for kg and 2 for lbs: "))

if flag==1:
    weight=weight/0.45
    print(f'You are {weight} pounds')
elif flag==2:
    weight= weight*0.45
    print(f'You are {weight} kilos')
else:
    print("Choose the correct option and try again")