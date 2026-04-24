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

nb_points = 0
for i in range(0, nb_questions):
    print()
    print(f"Question n°{i + 1} sur 4")
    reponse_int, reponse_correcte = poser_question()

    if reponse_int == reponse_correcte :
        print("Bonne reponse")
        nb_points += 1
        
        
    else:
        print("Mauvaise reponse")
        nb_points = max(0, nb_points)


print(f"Votre note est de {nb_points} / {nb_questions}")

moyenne = int(nb_questions / 2)
if nb_points == nb_questions:
    print("Excellent!")
elif moyenne < nb_points:
    print("Bien!")
elif moyenne == nb_points:
    print("Peut faire mieux !")
else:
    print("Continue, tu peux t'améliorer !")



