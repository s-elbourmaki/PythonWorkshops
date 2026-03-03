
age_texte = input("saisir votre age : ")

# transformation du texte en entier
age = int(age_texte)


if age >= 0 and age <= 12:
    statut = "Enfant"
elif age >= 13 and age <= 17:
    statut = "Adolescent"
elif age >= 18 and age <= 64:
    statut = "Adulte"
elif age >= 65:
    statut = "Senior"
else:
    statut = "Age invalide (négatif)"

print(f"Selon votre age ({age} ans), votre statut est : {statut}")