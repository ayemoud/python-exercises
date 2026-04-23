import random

nb_min = 1
nb_max = 10

def poser_question():
    a = random.randint(nb_min, nb_max)
    b = random.randint(nb_min, nb_max)
    reponse_str = input(f"Calculez : {a} + {b} = ")
    reponse_int = int(reponse_str)
    return reponse_int,a + b


while True:
    reponse_int, reponse_correcte = poser_question()

    if reponse_int == reponse_correcte :
        print("Bonne reposne")
        break
    else:
        print("Mauvaise reponse")
    

