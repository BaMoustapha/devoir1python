import random

# Liste des régions du Sénégal avec leurs chefs-lieux
regions_senegal = {
    "Dakar": "Dakar",
    "Diourbel": "Diourbel",
    "Fatick": "Fatick",
    "Kaffrine": "Kaffrine",
    "Kaolack": "Kaolack",
    "Kédougou": "Kédougou",
    "Kolda": "Kolda",
    "Louga": "Louga",
    "Matam": "Matam",
    "Saint-Louis": "Saint-Louis",
    "Sédhiou": "Sédhiou",
    "Tambacounda": "Tambacounda",
    "Thiès": "Thiès",
    "Ziguinchor": "Ziguinchor"
}

meilleurs_scores = []

def afficher_meilleurs_scores():
    print("\nTop 5 des meilleurs scores :")
    for i, score in enumerate(sorted(meilleurs_scores, reverse=True)[:5]):
        print(f"{i + 1}. {score} points")

def jouer():
    score = 0
    points= 0
    
    regions_list = list(regions_senegal.items())
    random.shuffle(regions_list)
    
    afficher_meilleurs_scores()
    
    for i in range(10):  # On pose 10 questions
        region, chef_lieu = regions_list[i]
        
        print(f"Question {i + 1} : Quel est le chef-lieu de {region} ?")
        answer = input()
        
        if answer.lower() == chef_lieu.lower():
            score += points
            print(f"Bravo ! Vous avez gagné {50} points !")
            
            
        else:
            print("Réponse incorrecte!!!")
            print(f"Le chef-lieu de {region} est {chef_lieu}.")

            
                    
        meilleurs_scores.append(points)
        
if __name__ == "__main__":
    while True:
        jouer()
        reponse = input("\nVoulez-vous tenter une autre partie ? [o/n] : ").strip().lower()
        if reponse != 'o':
            print("OKAY BYE BYE!!!")
            break    
    