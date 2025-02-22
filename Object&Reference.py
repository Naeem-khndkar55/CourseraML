a="banana"
b="banana"
print(a is b) #is is use to check weather two variable is pointing to the same object or no
#return boolean value
print(id(a))
print(id(b))
p=[81,82,83]
q=[81,82,83]
print(p is q) # p and q are not object
p=q #point the same reference
print(p==q)
print(p is q)  #now its will return true
print(id(p))
print(id(q))
q[0]=5#affact the whole value
print(p) 