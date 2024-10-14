# Création de la liste Fruits
fruits = ["pomme", "banane", "orange"]

# Ajout du kiwi dans la liste
fruits.append("kiwi")

# Suppression de l'orange
fruits.remove("orange")

# Modification du 2ème fruit par ananas
fruits[1] = "ananas"

# Affichage de la longueur de la liste
print(f"La liste contient {len(fruits)} fruits.")

# Triage de la liste et affichage
fruits.sort()
print(fruits)