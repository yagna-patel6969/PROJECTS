name=input("Enter your name:")
print("welcome",name)

age=input("Emter you age:")
print("your age is:",age)

                    #result of input is always str
                    #input int-->str
                    #input float-->str
val=input("Enter anything:")
print(type(val),val)
                    
                    
                    #type casting in input
name=int(input("Enter a number:")) #alphabets not convert into int or float
print(type(name),name)

name=float(input("Enter a number:"))
print(type(name),name)          