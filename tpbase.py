# ─────────────────────────────────────────────────────────────
#  EL BOURMAKI Salim, IDAI 25-26
# ─────────────────────────────────────────────────────────────
donnees = [
    ("Sara",    "Math",     12,    "G1"),
    ("Sara",    "Info",     14,    "G1"),
    ("Ahmed",   "Math",     9,     "G2"),
    ("Adam",    "Chimie",   18,    "G1"),
    ("Sara",    "Math",     11,    "G1"),
    ("Bouchra", "Info",     "abc", "G2"),
    ("",        "Math",     10,    "G1"),
    ("Yassine", "Info",     22,    "G2"),
    ("Ahmed",   "Info",     13,    "G2"),
    ("Adam",    "Math",     None,  "G1"),
    ("Sara",    "Chimie",   16,    "G1"),
    ("Adam",    "Info",     7,     "G1"),
    ("Ahmed",   "Math",     9,     "G2"),
    ("Hana",    "Physique", 15,    "G3"),
    ("Hana",    "Math",     8,     "G3"),
]
# ============================================================
#  PARTIE 1 : NETTOYAGE ET VALIDATION
# ============================================================
def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement

    if not isinstance(nom, str) or nom.strip() == "":
        return (False, "raison : nom vide ou invalide")

    if not isinstance(matiere, str) or matiere.strip() == "":
        return (False, "raison : matière vide ou invalide")

    if not isinstance(groupe, str) or groupe.strip() == "":
        return (False, "raison : groupe vide ou invalide")

    if note is None:
        return (False, "raison : note erronée (None)")

    try:
        note_num = float(note)
    except (ValueError, TypeError):
        return (False, "raison : note erronée (non numérique)")

    if note_num < 0 or note_num > 20:
        return (False, "raison : note erronée (hors plage [0, 20])")

    return (True, "")


valides        = []
erreurs        = []
doublons_exact = set()
vus            = {}

for ligne in donnees:
    est_valide, raison = valider(ligne)

    if est_valide:
        nom, matiere, note, groupe = ligne
        ligne_propre = (nom.strip(), matiere.strip(), float(note), groupe.strip())

        if ligne_propre in vus:
            doublons_exact.add(ligne_propre)
        else:
            vus[ligne_propre] = True

        valides.append(ligne_propre)
    else:
        erreurs.append({"ligne": ligne, "raison": raison})

# ============================================================
#  PARTIE 2 : STRUCTURATION
# ============================================================
matieres_distinctes = set()
for nom, matiere, note, groupe in valides:
    matieres_distinctes.add(matiere)

notes_par_etudiant = {}
for nom, matiere, note, groupe in valides:
    if nom not in notes_par_etudiant:
        notes_par_etudiant[nom] = {}
    if matiere not in notes_par_etudiant[nom]:
        notes_par_etudiant[nom][matiere] = []
    notes_par_etudiant[nom][matiere].append(note)

etudiants_par_groupe = {}
for nom, matiere, note, groupe in valides:
    if groupe not in etudiants_par_groupe:
        etudiants_par_groupe[groupe] = set()
    etudiants_par_groupe[groupe].add(nom)

# ============================================================
#  PARTIE 3 : CALCULS ET STATISTIQUES
# ============================================================
def somme_recursive(liste_notes):
    if len(liste_notes) == 0:
        return 0
    return liste_notes[0] + somme_recursive(liste_notes[1:])

def calculer_moyenne(liste_notes):
    if len(liste_notes) == 0:
        return None
    return somme_recursive(liste_notes) / len(liste_notes)

stats_etudiants = {}

for etudiant, matieres in notes_par_etudiant.items():
    toutes_les_notes     = []
    moyennes_par_matiere = {}

    for matiere, notes in matieres.items():
        moy = calculer_moyenne(notes)
        moyennes_par_matiere[matiere] = moy
        for n in notes:
            toutes_les_notes.append(n)

    stats_etudiants[etudiant] = {
        "generale":    calculer_moyenne(toutes_les_notes),
        "par_matiere": moyennes_par_matiere
    }

# ============================================================
#  PARTIE 4 : ANALYSE AVANCÉE ET DÉTECTION D'ANOMALIES
# ============================================================
SEUIL_MOYENNE_FAIBLE = 10.0
SEUIL_ECART_INSTABLE = 6.0

alertes = {
    "notes_multiples_meme_matiere": [],
    "profil_incomplet":             [],
    "groupe_moyenne_faible":        [],
    "ecart_instable":               []
}

for etudiant, matieres in notes_par_etudiant.items():
    for matiere, notes in matieres.items():
        if len(notes) > 1:
            alertes["notes_multiples_meme_matiere"].append({
                "etudiant": etudiant,
                "matiere":  matiere,
                "notes":    notes
            })

for etudiant, matieres in notes_par_etudiant.items():
    matieres_etudiant   = set(matieres.keys())
    matieres_manquantes = matieres_distinctes - matieres_etudiant
    if len(matieres_manquantes) > 0:
        alertes["profil_incomplet"].append({
            "etudiant":            etudiant,
            "matieres_manquantes": matieres_manquantes
        })

for groupe, etudiants in etudiants_par_groupe.items():
    notes_groupe = []
    for etudiant in etudiants:
        for matiere, notes in notes_par_etudiant[etudiant].items():
            for n in notes:
                notes_groupe.append(n)
    moy_groupe = calculer_moyenne(notes_groupe)
    if moy_groupe is not None and moy_groupe < SEUIL_MOYENNE_FAIBLE:
        alertes["groupe_moyenne_faible"].append({
            "groupe":  groupe,
            "moyenne": round(moy_groupe, 2)
        })

for etudiant, matieres in notes_par_etudiant.items():
    toutes = []
    for notes in matieres.values():
        for n in notes:
            toutes.append(n)
    if len(toutes) >= 2:
        note_min = toutes[0]
        note_max = toutes[0]
        for n in toutes:
            if n < note_min:
                note_min = n
            if n > note_max:
                note_max = n
        ecart = note_max - note_min
        if ecart >= SEUIL_ECART_INSTABLE:
            alertes["ecart_instable"].append({
                "etudiant": etudiant,
                "note_min": note_min,
                "note_max": note_max,
                "ecart":    round(ecart, 2)
            })

# ============================================================
#  FONCTIONS D'AFFICHAGE — une par partie
# ============================================================
separateur = "=" * 60
def afficher_partie1():
    print()
    print(separateur)
    print("  PARTIE 1 – NETTOYAGE ET VALIDATION")
    print(separateur)

    print("\n--- Enregistrements VALIDES ---")
    for v in valides:
        print(f"  {v}")

    print("\n--- Enregistrements INVALIDES ---")
    for e in erreurs:
        print(f"  Ligne  : {e['ligne']}")
        print(f"  {e['raison']}")
        print()

    print("--- Doublons exacts détectés ---")
    if len(doublons_exact) == 0:
        print("  Aucun doublon exact.")
    else:
        for d in doublons_exact:
            print(f"  {d}")

def afficher_partie2():
    print()
    print(separateur)
    print("  PARTIE 2 – STRUCTURATION")
    print(separateur)

    print(f"\n--- Matières distinctes ({len(matieres_distinctes)}) ---")
    print(f"  {matieres_distinctes}")

    print("\n--- Notes par étudiant (hiérarchie) ---")
    for etudiant, matieres in notes_par_etudiant.items():
        print(f"  {etudiant} :")
        for matiere, notes in matieres.items():
            print(f"    {matiere} : {notes}")

    print("\n--- Étudiants par groupe ---")
    for groupe, etudiants in etudiants_par_groupe.items():
        print(f"  {groupe} : {etudiants}")

def afficher_partie3():
    print()
    print(separateur)
    print("  PARTIE 3 – CALCULS ET STATISTIQUES")
    print(separateur)

    print("\n--- Moyennes par étudiant ---")
    for etudiant, stats in stats_etudiants.items():
        print(f"  {etudiant}")
        print(f"    Moyenne générale : {round(stats['generale'], 2)}")
        for matiere, moy in stats["par_matiere"].items():
            print(f"    {matiere} : {round(moy, 2)}")

def afficher_partie4():
    print()
    print(separateur)
    print("  PARTIE 4 – ANOMALIES DÉTECTÉES")
    print(separateur)

    print("\n--- Anomalie 1 : notes multiples pour une même matière ---")
    if len(alertes["notes_multiples_meme_matiere"]) == 0:
        print("  Aucune anomalie détectée.")
    else:
        for a in alertes["notes_multiples_meme_matiere"]:
            print(f"  {a['etudiant']} – {a['matiere']} : notes = {a['notes']}")

    print("\n--- Anomalie 2 : profil incomplet ---")
    if len(alertes["profil_incomplet"]) == 0:
        print("  Aucun profil incomplet.")
    else:
        for a in alertes["profil_incomplet"]:
            print(f"  {a['etudiant']} manque : {a['matieres_manquantes']}")

    print(f"\n--- Anomalie 3 : groupes avec moyenne < {SEUIL_MOYENNE_FAIBLE} ---")
    if len(alertes["groupe_moyenne_faible"]) == 0:
        print("  Aucun groupe en difficulté.")
    else:
        for a in alertes["groupe_moyenne_faible"]:
            print(f"  Groupe {a['groupe']} : moyenne = {a['moyenne']}")

    print(f"\n--- Anomalie 4 : écart instable (>= {SEUIL_ECART_INSTABLE} points) ---")
    if len(alertes["ecart_instable"]) == 0:
        print("  Aucun étudiant avec un écart instable.")
    else:
        for a in alertes["ecart_instable"]:
            print(f"  {a['etudiant']} : min={a['note_min']} "
                  f"max={a['note_max']} écart={a['ecart']}")

# ============================================================
#  MENU PRINCIPAL
# ============================================================
def afficher_menu():
    print()
    print(separateur)
    print("           MENU PRINCIPAL")
    print(separateur)
    print("  1 - Nettoyage et Validation")
    print("  2 - Structuration des données")
    print("  3 - Calculs et Statistiques")
    print("  4 - Anomalies et Alertes")
    print("  0 - Quitter")
    print(separateur)

# ── Boucle principale ────────────────────────────────────────
while True:
    afficher_menu()
    try:
        choix = int(input("  Votre choix (0-4) : "))
    except ValueError:
        print("\n  Erreur : veuillez entrer un nombre entre 0 et 4.")
        continue
    if choix == 1:
        afficher_partie1()
    elif choix == 2:
        afficher_partie2()
    elif choix == 3:
        afficher_partie3()
    elif choix == 4:
        afficher_partie4()
    elif choix == 0:
        print()
        print(separateur)
        print()
        print(separateur)
        break
    else:
        print("\n  Choix invalide. Entrez un nombre entre 0 et 4.")