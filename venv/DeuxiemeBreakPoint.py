#Question 6
temp = str(input("Saisir une chaine de caractères"))
boolA = False
boolB = False

for i in range(len(temp)):
    if temp[i] == "@":
        boolA = True

if boolA and temp.endswith(".com"):
    print("Email valide")
else:
    print("Email invalide")

#Question 7
for i in range(10):
    print("Message")

#Question 8
for l in "String":
    print(l)

#Question 9
a = 0
b = 10
for i in range(b - 1):
    a = a+1
    print("a = " + str(a))

#Question 10
for i in range(10):
    print(b-i)

#Question 11
temp = int(-1)
print(temp)
while temp > 10 or temp < 0:
    temp = int(input("Saisir un chiffre"))

#Question 12
for c in "bonjour" :
    print(c)

for item in ["ok", "nok", "rip"]:
    print(item)

#Question 13
for i in range(14):
    if i != 0 and i % 3 == 0:
        print(i)
#Question 14
temp = int(input("Saisir un chiffre"))
