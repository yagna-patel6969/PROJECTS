                                #WAP driving licence

#we have to convert str-->int bec we can not compair strint or int in condition
age=int(input("Enter your age"))
if(age>18):
    print("You are eligible ")
elif(age==18):
    print("Wait for 1 year")
else:
    print("You are not eligible")
