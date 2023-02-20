# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions

# -> Definir les entites (donnees, actions)

# class Question
    # question / titre      - str
    # choix de reponses     - (str)
    # bonne reponse         - str
    # poser la question()   -> bool
# class ValidationReponse
    # reponse utilisateur
    # bonne reponse
    # score
    # recuperer la reponse
    # validater la reponse
# classe Questionnaire
    # Questions                 - (Question)
    # lancer questionnaire()    -> None

class Question():
    def __init__(self, title:str, possible_answers: tuple, good_answer:str):
        self.title = title
        self.possible_answers = possible_answers
        self.good_answer = good_answer


    def poser_question(self):
        # titre_question, r1, r2, r3, r4, choix_bonne_reponse
        choix = self.possible_answers
        bonne_reponse = self.good_answer
        print("QUESTION")
        print("  " + self.title)
        for index, choix in enumerate(choix):
            print("  ", index + 1, "-", choix)


def demander_reponse_numerique_utlisateur(min, max):
    reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int

        print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
    except:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utlisateur(min, max)
    

'''
titre = question[0]
choix = question[1]
bonne_reponse = question[2]
'''
def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    print("QUESTION")
    print("  " + question[0])
    for i in range(len(choix)):
        print("  ", i+1, "-", choix[i])

    print()
    resultat_response_correcte = False
    reponse_int = demander_reponse_numerique_utlisateur(1, len(choix))
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        resultat_response_correcte = True
    else:
        print("Mauvaise réponse")
        
    print()
    return resultat_response_correcte


'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Score final :", score, "sur", len(questionnaire))

"""questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)"""

q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
q1.poser_question()


