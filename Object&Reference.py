a="banana"
b="banana"
print(a is b) #is is use to check weather two variable is pointing to the same object or no
#return boolean value
print(id(a))
print(id(b))
p=[81,82,83]
q=[81,82,83]
print(p is q) # p and q are not object

print(p==q)
print(id(p))
print(id(q))