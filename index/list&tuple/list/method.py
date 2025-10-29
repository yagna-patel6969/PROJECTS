                        #append method
#add one element in the end
print("append method")
list=[11,2,3,4,11]
list.append(7)
print(list)
print(type(list))
print(list.count(11))#HOW MANY TIMES 11 


                        #sort method
#also work in strings (sort according to alphabets)
#sorts in ascending order
print("short method(asending)")
list1=[1,2,3]
list1.sort()
print(list1)
list2=[1,2,3]
list2.sort(reverse=False)
print(list2)
print(type(list1))

#sorts in decending order
print("short method(disending)")
list3=[1,2,3,4]
list3.sort(reverse=True)
print(list3)

                            #reverce method
#values sort in revers
#also work in strings (sort according to alphabets)
print("reverce method")
list4=[1,2,3,5,4]
list4.reverse()
print(list4)


                            #insert method
#add value at specific index
# starts from 0
#syntex=list.insert(index,value)
print("Insert method")
list5=[1,2,3,4,5]
list5.insert(2,"g")
print(list5)

                            #remove
#remove first occurance of element
# starts from 1
print("remove method")
list6=[1,2,3,1]
list6.remove(1)
print(list6)

                            #pop method
#remove element at specific index
# starts from 0
print("pop method")
list7=[1,2,3,4,5]
list7.pop(2)
print(list7)