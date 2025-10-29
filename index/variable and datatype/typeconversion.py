# two types of conversio 1.conversion(autometicly) 2.casting(manualy)
# we can add str+str , int+int , int+float , float+float
#we can not str+float , str+int
a=20
b=20.56
c="5"
sum=a+b # int+float (int-->float) final ans in float 
sum1=a+c
sum2=b+c
print(sum)
print(sum1)# error int+str
print(sum2)#error str+float

                    #type casting

d=2
f=str(d)
g=int("9")#but we can not convert alphabets into float and int 
h=float("23")
print(type(f))
print(type(g))
print(type(h))
print(d+g)
print(d+h)
    

                   