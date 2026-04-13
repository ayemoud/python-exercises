
import random
def demander_nombre(nb_min, nb_max):
    while True:
        nb_str = input(f"Quel est le nombre magique entre {nb_min} et {nb_max} : ")
        try:
                nb_int = int(nb_str)
                
        except :
            print("Erreur: Vous devez entrer un nombre. Réessayer.")
            
        else:
            if nb_int < nb_min or nb_int > nb_max:
                print(f"Vous ne pouvez choisir que des nombres compris entre {nb_min} et {nb_max}.")
                
            else:
                return nb_int   



nb_min = 1
nb_max = 10
nb_mag = random.randint(nb_min, nb_max)

nb_vies = 4


for i in range(0, nb_vies):
    vies = nb_vies - i
    print(f"Il vous reste {vies} vies! ")
    nb_user = demander_nombre(nb_min, nb_max)

    if nb_user == nb_mag:
        print(f"Bravo!! Le nombre magique est bien : {nb_mag} ")
        break
        
    elif nb_user < nb_mag:
        
        print("Le nombre magique est plus grand !!")
        
    else:
        
        print("Le nombre magique est plus petit !!")
else:      
    print("Vous avez perdu!")
    print(f"Le nombre magique était : {nb_mag}")
        




















