frute= ["banana", "apple", "cherry"]
print(frute)
frute[0]="peer"
frute[-1]="orrange"
print(frute)#list mutable;

alist=['a','b','c','d','e','f']
alist[1:3]=['x','y']
print(alist)

greetigs="Hello World"
print(greetigs) #make a error because assingnin value in existing string is not allowed
#to solve this one of the mathod
newgreetings='j'+greetigs[1:]
print(newgreetings)
print(greetigs) #string is emmutable
