#Header
"""
programme principal
25/09/2023
François-Régis DRUTEL, Paul DUMONT
on pourrait rajouter une option de protection de 
saisies des entrées
"""
from Fonctions import acquiphrase, conversion, analyse

#Entrées :
dictionnaire = {"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "Martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "Jean" : 4, "." : 5}      

#table de transition d'états:
dicoetat={
    0 : [4,1,8,8,8,8],
    1 : [8,8,1,2,8,8],
    2 : [8,8,2,8,3,8],
    3 : [7,5,8,8,8,9],
    4 : [8,8,8,8,3,8],
    5 : [8,8,5,6,8,8],
    6 : [8,8,6,8,8,9],
    7 : [8,8,8,8,8,9], 
    8 : [8,8,8,8,8,8],
    9 : [9,9,9,9,9,9]
    }

#tests des fonctions
phrase = acquiphrase()
phraseconvertie = conversion(phrase,dicoetat)
print(analyse(dicoetat,phraseconvertie))