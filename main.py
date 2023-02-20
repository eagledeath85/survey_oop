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


class Question:
    def __init__(self, title:str, possible_answers: tuple, good_answer:str):
        self.title = title
        self.possible_answers = possible_answers
        self.good_answer = good_answer

    def FromData(data):
        q = Question(data[2], data[0], data[1])
        return q

    def poser_question(self):
        print("QUESTION")
        print("  " + self.title)
        for index, choix in enumerate(self.possible_answers):
            print("  ", index + 1, "-", choix)
        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.possible_answers))
        if self.possible_answers[reponse_int-1].lower() == self.good_answer.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
        print()
        return resultat_response_correcte


    def demander_reponse_numerique_utlisateur(min, max) -> int:
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int
            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    

class Questionnaire:

    def __init__(self, questions):
        self.questions = questions

    def lancer_questionnaire(self):
        score = 0
        for question in self.questions:
            if question.poser_question():
                score += 1
        print("Score final :", score, "sur", len(self.questions))


questions = (
            Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
            Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
            Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles"),
            )

questionnaire = Questionnaire(questions)
questionnaire.lancer_questionnaire()

# Il existe une fonction de classe particuliere permettant de creer des objects meme si l'ordre des parametres n'est pas le bon
# Cette fonction se nomme FromData()
# Elle peut etre utilisee si par exemple on veut lire des donnees venant d'une source externe
data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
q = Question.FromData(data)
q.poser_question()


