#Header
"""
Fichier des fonctions
25/09/2023
François-Régis DRUTEL, Paul DUMONT

"""
#acquisition de la phrase à analyser et transformation en liste d'états
def acquiphrase ():
    phrase = str(input("entrez votre phrase : "))
    phrase = phrase.split()
    return phrase


dictionnaire = {"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "Martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "Jean" : 4, "." : 5}      


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


def analyse(phrase):
    etat = 0
    while etat != 8:
        for mot in phrase:
            etat = dicoetat[etat][dictionnaire[mot]]

    return etat

def conversion(phrase):
    etat = []
    for mots in phrase :
        if mots in dictionnaire :
            etat.append(dictionnaire[mots])
    return etat
            
phrase = acquiphrase()
print(conversion(phrase))