a= "I have had an apple on my desk before"
print(a.count('a')) # count of leter a
print(a.count('ha')) #  count of sub strings
#count also work on list
z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
print(z.count("4"))#0
print(z.count(4))#3
print(z.count("a"))#0
print(z.count("electron"))#2


#index
music = "Pull out your music and dancing can begin"
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]

print(music.index("m"))
print(music.index("your"))

print(bio.index("Metatarsal"))
print(bio.index([]))
print(bio.index(43))
