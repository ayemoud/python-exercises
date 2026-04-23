import random

nb_min = 1
nb_max = 10
nb_questions = 4


def poser_question():
    a = random.randint(nb_min, nb_max)
    b = random.randint(nb_min, nb_max)
    reponse_str = input(f"Calculez : {a} + {b} = ")
    reponse_int = int(reponse_str)
    return reponse_int,a + b


for i in range(0, nb_questions):
    print(f"Question n°{i + 1} sur 4")
    reponse_int, reponse_correcte = poser_question()

    if reponse_int == reponse_correcte :
        print("Bonne reponSe")
        break
    else:
        print("Mauvaise reponse")
    

