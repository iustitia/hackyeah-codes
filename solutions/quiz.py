# questions source: https://funtest.pl/test/funtestgry5004/

questions = ['Jakie miasto jest stolicą Włoch? ',
             'Ile dni ma lipiec? ',
             'Który z oceanów jest największy? ',
             'Z iloma państwami graniczy Hiszpania? ']

answers = ['Rzym', '31', 'Spokojny', '2']

################

"""Stwórz mechanizm quizu dla powyższych pytań i odpowiedzi. 
Wyświetl pytanie, przyjmij odpowiedź od użytkownika i określ czy jest prawidłowa. Wypisz o tym informację.
"""

################

for i, q in enumerate(questions):
    a = input(q)
    if a == answers[i]:
        print("Poprawna odpowiedź")
    else:
        print("Niestety nie. Poprawna odpowiedź to: " + answers[i])
