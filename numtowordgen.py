num= input('Enter number: ')
word=" "
for item in num:
    if int(item)==1:
        word+="one "
    elif int(item)==2:
        word+="two "
    elif int(item)==3:
        word+="three "
    elif int(item)==4:
        word+="four "    
    elif int(item)==5:
        word+="five "
    elif int(item)==6:
        word+="six "
    elif int(item)==7:
        word+="seven "
    elif int(item)==8:
        word+="eight "
    else:
        word+="nine "

print(word)