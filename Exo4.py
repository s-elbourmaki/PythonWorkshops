try:
    nombre1 = float(input("Veuillez saisir le premier nombre : "))
    nombre2 = float(input("Veuillez saisir le deuxième nombre : "))
 
    print("\nCHOIX DE L'OPÉRATION :")
    print("1 : Addition (+)")
    print("2 : Soustraction (-)")
    print("3 : Multiplication (*)")
    print("4 : Division (/)")
    
    choix = input("Votre choix (1, 2, 3 ou 4) : ")
    
    if choix == '1':
        resultat = nombre1 + nombre2
        print(f"\nRésultat : {nombre1} + {nombre2} = {resultat}")
        
    elif choix == '2':
        resultat = nombre1 - nombre2
        print(f"\nRésultat : {nombre1} - {nombre2} = {resultat}")
        
    elif choix == '3':
        resultat = nombre1 * nombre2
        print(f"\nRésultat : {nombre1} * {nombre2} = {resultat}")
        
    elif choix == '4':
        #  division par zéro
        if nombre2 == 0:
            print("\n Erreur : La division par 0 est impossible.")
        else:
            resultat = nombre1 / nombre2
            print(f"\nRésultat : {nombre1} / {nombre2} = {resultat}")
            
    else:
        print("\n Erreur : Choix d'opération invalide. Veuillez saisir 1, 2, 3 ou 4.")

except ValueError:
    print("\n Erreur de saisie : Veuillez entrer des nombres valides.")