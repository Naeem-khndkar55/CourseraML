# a= [81,82,83]
# b= a[:] #copy of a different refence
# print(a==b)
# print(a is b)
# b[0]=5
# print(a)
# print(b)

b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)