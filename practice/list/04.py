#pelandrom using input

seq=input("Enter a sequance:")#input
list=list(seq)#list ma convert kari list variablema store kario
list1=list.copy()#list ni copy banavi
list1.reverse()#reverce
if(list1==list):
    print("yes")
else:
    print("no")