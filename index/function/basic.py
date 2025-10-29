# # ask user name
# name=input("Enter a name :")

# # say hellow to user
# print(f"hello {name}")

# #if user gives more spaces in input remove for it
# #name=input("Enter a name :") input-->          ygna
# name1=input("Enter a name with spaces :")
# name1=name1.strip()
# print(f"hello {name1}")

# #capitalize user's name
# #input=patel yagna--->Patel yagna (not capital second name)
# name1=input("Enter a name:")
# name1=name1.capitalize()#first latter is capitalized of input
# print(f"hello {name1}") 

# #capitalized all the alphabets of eacg word in input
# name1=input("Enter a name(first name+second name):")
# name1=name1.title()
# print(f"hello {name1}")  

# # we can also add functions

# # remove whit space also capitalized their name
# name2=input("Enter a name:") 
# name2=name2.strip().title()
# print(f"hello {name2}")

# #second method
# name2=input("Enter a name:").strip().title()
# print(f"Hello {name2}")

# #name divide in to first name and second name 

# name3=input("Enter a name with FN and SN:").strip().title()
# first,last=name3.split(" ")
# print(f"Hello {first}")
# print(f"Hello {last}")
# print(f"Hello {name3}")

# # #round function
# # If fractional part < 0.5 → round down

# # If fractional part > 0.5 → round up

# # If fractional part == 0.5 → rounds to nearest even number

# num1=float(input("Enter a number :"))
# num2=float(input("Enter a second number:"))
# print(f"sum={round(num1+num2):,}")
# print(f"{round(num1/num2):,}")
# print(f"{round(num1/num2,2)}")#it gives 2 digits after point
# print(f"{round(num1/num2,2):.2f}")#it gives 2 digits after point


# defin function 

def hello(to="world"):
    print("hello",to)


hello()
name=input("Entera name:")
hello(name)
