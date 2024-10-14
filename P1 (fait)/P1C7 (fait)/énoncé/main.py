# Création d'un dictionnaire
fruits = {
    "pomme" : "rouge", 
    "banane" : "jaune", 
    "orange" : "orange"
}

# Ajout de la clé kiwi
fruits["kiwi"] = "vert"

# Ajout de la valeur de la banane dans une variable 
couleur_banane = fruits["banane"]

# Modification de la valeur de pomme en vert
fruits["pomme"] = "vert"

# Suppression de la banane du dictionnaire
del fruits["banane"]

# Affichage du dictionnaire
print(fruits)