# Initialisation de la liste des contacts en dehors de la boucle
carnet = []

# Boucle principale pour maintenir le menu actif
while True:
    # Affichage du menu
    print("\n--- MENU CARNET D'ADRESSES ---")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Quitter le programme")
    
    # Saisie de l'utilisateur
    choix = input("Choisissez une option (1, 2 ou 3) : ")
    
    # Traitement du choix
    if choix == '1':
        nom = input("Entrez le nom du contact à ajouter : ")
        carnet.append(nom)
        print(f"✅ Contact '{nom}' ajouté avec succès.")
        
    elif choix == '2':
        if len(carnet) == 0:
            print("⚠️ Le carnet d'adresses est vide.")
        else:
            print("\n--- Liste des contacts ---")
            # Utilisation de enumerate pour afficher l'index (en commençant à 1)
            for index, contact in enumerate(carnet, start=1):
                print(f"{index}. {contact}")
                
    elif choix == '3':
        print("Fermeture du programme. Au revoir !")
        break # Permet de sortir de la boucle while
        
    else:
        print("❌ Option invalide. Veuillez réessayer.")