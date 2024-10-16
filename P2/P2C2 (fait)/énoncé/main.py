def main():
    
    # Entrée d'une liste de nombres et affichage de celle_ci
    liste = input("Entrez une suite de nombres (avec une virgule entre chaque nombre)")
    liste = liste.split(",")
    print(f"La liste est : {liste}")
    
    # Calcul de la somme des nombres
    somme = 0
    for nombre in liste:
        somme += int(nombre)
    print(f"La somme des nombres est : {somme}")

    # Calcul de la moyenne des nombres
    moyenne = 0
    for nombre in liste :
        moyenne = somme / len(liste)
    print(f"La moyenne des nombres est : {moyenne}")

    # Calcul du nombre de nombres supérieurs à la moyenne
    sup_moyenne = 0
    for nombre in liste :
        if int(nombre) > moyenne:
            sup_moyenne += 1
    print(f"Le nombre de nombres supérieurs à la moyenne est : {sup_moyenne}")
    
    # Calcul du nombre de nombres pairs
    nombres_pairs = 0
    i = 0
    while i < len(liste):
        if int(liste[i]) % 2 == 0:
            nombres_pairs += 1
        i += 1
    print(f"Le nombre de nombres pairs est : {nombres_pairs}")

if __name__ == "__main__":
    main()