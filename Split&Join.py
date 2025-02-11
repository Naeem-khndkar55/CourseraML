song = "the rain in Spain...."
wds= song.split() #cut the word based on spaces
print(wds)# list of words
s="leaders and best"
print(s.split('e')) # split the sentence based on e
#join
color =['red', 'green', 'blue']
glue = ';'
jn= glue.join(color)
print(jn)
print(color)

print('***'.join(color))
print("".join(color))

