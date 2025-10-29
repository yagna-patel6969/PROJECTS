#Data type-->stores multiple values
#it can store diffrent types of data type variable
# list is mutable

marks=[100 , 90 , 98 , 87 , "karan" , 90]
print(marks)
print(type(marks))
print(marks[0])
print(marks[3])
print(marks[-1])
print(str(marks[4])+ "-->" + str(marks[5]))  #we have to convert int-->str bec. we cannot add str+int
print(len(marks))


#list is mutable(We can change it)
student=["karan","yagna"]
student[0]="parma"
print(student[0])
print(student)