#4.	 WAP to find out largest number from given three numbers.

num1=int(input("Given 1st number:"))
num2=int(input("Give me second number:"))
num3=int(input("Give me  3rdnumber:"))

if(num1>num2 and num1>num3):
    print("Number 1st is largest")
elif(num2>num1 and num2>num3):
    print("2nd number is largest")
else:
    print("3rd number is largest")