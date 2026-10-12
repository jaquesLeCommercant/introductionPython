prenom = None
age = 0
while prenom != "Jaqueline" :
    prenom = input("Quel est ton prénom ?")
    if prenom == "Jaqueline" :
        break
    else :
        print(f"Non {prenom}. Pas bonjour.")
        continue
print(f"Bonjour {prenom} !")
while age < 18 :
    age = int(input("Quel est ton âge ?"))
    if age >= 18 :
        break
    else :
        print("Ce site web est réservé aux personnes majeures.")
        continue
print(f"Bienvenue sur le site web, {prenom}.")