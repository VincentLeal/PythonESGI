from math import *
#Question 1
temps = 6.892
distance = 19.7

#Question 2
nom = input("Saisir un nom")
age = input("Saisir un age")
print(nom, age)

nom = str(input("Saisir un nom"))
age = int(input("saisir un age"))

#Question 3
temp = float(input("saisir un float"))
if temp >= 0:
    print(sqrt(temp))
else:
    print("ERROR")

#Question 4
array = [str(input("saisir un premier mot")), str(input("saisir un deuxième mot"))]
array.sort()
print(array[0])

#Question 5
pSeuil = 2.3
vSeuil = 7.41

p = float(input("Saisir la pression"))
v = float(input("Saisir le volume"))

if p > pSeuil and v > vSeuil:
    print("ARRET IMEDIAT")
elif p > pSeuil and v <= vSeuil:
    print("AUGMENTER LE VOLUME DE L'ENCEINTE")
elif p <= pSeuil and v > vSeuil:
    print("DIMINER LE VOLUME DE L'ENCEINTE")
else:
    print("TOUT VA BIEN")


