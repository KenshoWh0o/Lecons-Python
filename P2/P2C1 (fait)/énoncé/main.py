def main():
    
    # Entrée de l'opération souhaitée
    nombre_a_gauche = input("Entrez le premier nombre !")
    nombre_a_droite = input("Entrez le deuxième nombre !")
    symbole = input("Entrez l'opération souhaitée (=,-,*,/)")
    
    # Définition de base de la variable résultat
    resultat = 0
    
    # Vérification que les nombres entrés soient entiers
    if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric() :
        print("Nombres non entiers !")
    else :
        nombre_a_gauche = int(nombre_a_gauche)
        nombre_a_droite = int(nombre_a_droite)
    
    # Vérification que le symbole est valide et calcul
    match symbole :
        case "+" :
            resultat = nombre_a_gauche + nombre_a_droite
        case "-" :
            resultat = nombre_a_gauche - nombre_a_droite
        case "*" :
            resultat = nombre_a_gauche * nombre_a_droite
        case "/" :
            if nombre_a_droite == 0 :
                print("On ne peut pas diviser par 0 !")
            else :
                resultat = nombre_a_gauche / nombre_a_droite
        case _ :
            print("Symbole invalide !")
    
    # Affichage du résultat
    print(f"Le résultat est {resultat} !")

if __name__ == "__main__":
    main()