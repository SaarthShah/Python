command= "  "
flag=0
while command.upper()!= "QUIT":
    command= input("> ")
    if command.lower()=="start" and flag==0:
        print("Car Started.......")
        flag=1
    elif command.lower()=="start" and flag==1:
        print("Car already running")
        flag=1
    elif command.lower()=="stop" and flag==1:
        print("Car Stopped")
        flag=0
    elif command.lower()=="stop" and flag==0:
        print("Car already Stopped")
    elif command.lower()=="help":
            print("""Type:
Start to start the car
Stop to stop the car
Quit to exit the game""")
    elif command.lower()=='quit':
        print("Exiting the game")
    else:
        print("Wrong command, try again!")
        
