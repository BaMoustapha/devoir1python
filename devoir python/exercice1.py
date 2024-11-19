def afficher_calendrier():
    jours_dans_mois = int(input("Entrez le nombre de jours dans le mois : "))
    premier_jour = input("Entrez le jour de début du mois (LUN, MAR, MER, etc.) : ").upper()
    
    jours_semaine = ["LUN", "MAR", "MER", "JEU", "VEN", "SAM", "DIM"]
    
    premier_jour_index = jours_semaine.index(premier_jour)
    
    print(" ".join(jours_semaine))
    
    espaces = "    " * premier_jour_index
    print(espaces, end="")
    
    for jour in range(1, jours_dans_mois + 1):
        print(f"{jour: >3} ", end="")
        
        if (jour + premier_jour_index - 1) % 7 == 6:
            print()  

afficher_calendrier()
