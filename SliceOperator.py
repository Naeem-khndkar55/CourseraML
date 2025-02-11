Sent = "Hi,i am Naeem Khandakar"
print(Sent[0:5]) #Sent[start: end] it cut specific sub String from a string
fruit = "Banana"
print(fruit[:3]) #ending value only startfrom 0 index
print(fruit[3:]) #starting value end in the last index 

a_list = [ 'a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])
#tupples---
julia =("julia", "Roberts",1967, "Duplicity", 2009, "Adress", "Atomic, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))
julia = julia[:3]+ ("Eat Pray Love", 2010)+julia[5:]
print(julia)

#concatenate
print([1,2]+[3,4])
frt= ['aapple', 'orange', 'banana', 'charry']
print(frt+ [6,7,8,9 ])
#repetation of list
print([0]*4)
