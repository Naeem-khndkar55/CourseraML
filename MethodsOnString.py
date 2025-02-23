ss="Hello World!"
print(ss.upper())

tt=ss.lower()
print(tt)
print(ss)

els= ss.count('l')
print(els)

print("***"+ss.strip()+"***")#strip method remove unnecesey space from the begining and end
news = ss.replace('o',"***")
print(news)
#string is immutable
#format function
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)

#f string
name = "Rodney Dangerfield"
score = -1
print("Hello {}. Your score is {}.".format(name, score))
print(f"Hello {name}. Your score is {score}.")
