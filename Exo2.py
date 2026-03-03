carnet_adresses = []
while True:
    print("\nMENU CARNET D'ADRESSES :")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Quitter le programme")
    
    choix = input("Veuillez choisir une option (1, 2 ou 3) : ")
    
    if choix == '1':
        nouveau_contact = input("Entrez le nom du nouveau contact : ")
        carnet_adresses.append(nouveau_contact)
        print(f"Le contact '{nouveau_contact}' a ete ajoute avec succes.")
        
    elif choix == '2':
        if not carnet_adresses:
            print("Votre carnet d'adresses est vide pour le moment.")
        else:
            print("\nListe des contacts : ")
            for index, contact in enumerate(carnet_adresses, start=1):
                print(f"{index}. {contact}")
                
    elif choix == '3':
        print("Fermeture du carnet d'adresses. Au revoir !")
        # pour sortir de la boucle while
        break
        
    else:
        print("Option invalide. Veuillez saisir 1, 2 ou 3.")