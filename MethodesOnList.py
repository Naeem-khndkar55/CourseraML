myList=[]
myList.append(3)#add item in the end
myList.append(6)
myList.append(12)
print(myList)
myList.insert(1,12)#insert item in perticular positon (pos,item)
print(myList)
print(myList.count(12)) #count a specifq value frequency
print(myList.index(3))#print the index of an item
print(myList.count(5))

myList.reverse()#reverse a list
print(myList)
myList.sort()#sort in assending order
print(myList)

myList.remove(12)#remove a specifc item if same multiple item then it remove the first one
print(myList)

lastitem=myList.pop()#remove the last item
print(lastitem)
print(myList) 
#concateate
myList=myList + ["naeem"]
print(myList) 