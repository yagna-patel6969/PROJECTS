                        #end with 
#work==stetment end with () than output is true

str1=input("Enter a statment:")
print(str1.endswith("na"))
print(str1.endswith("na."))

                        #capitaliz
#It changes the string as follows:
# 1>Makes the first character uppercase.
# 2>Makes all other characters lowercase. 

str2=input("Enter a statement:")
print(str2.capitalize())


# capitalize() → First character uppercase, rest lowercase.

# title() → First character of each word uppercase.

# upper() → All letters uppercase.

# lower() → All letters lowercase.

# swapcase() → Converts uppercase → lowercase and lowercase → uppercase.
str3 = input("Enter a statement: ")

print("capitalize():", str3.capitalize())
print("title():", str3.title())
print("upper():", str3.upper())
print("lower():", str3.lower())
print("swapcase():", str3.swapcase())



                        #replace    
#it replece old value to new value
#print(str4.replace("old" , "new"))
str4=input("Enter your name:")
print(str4.replace("a" , "B"))
 


                        #find
#it show's us charactor index
str5=input("Enter a sentance:")
cal1=input("Enter a word you want to find:")
print(str5.find(cal1))

                        #count
#it shows how many times word in sentence
str6=input("Enter a stetment:")
cal2=input("Enter a word")
print(str6.count(cal2))
