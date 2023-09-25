#Header
"""
Fichier des fonctions
25/09/2023
François-Régis DRUTEL, Paul DUMONT
il reste à perfectionner la fonction d'analyse et d'afficher 
si la phrase est syntaxiquement correct
"""

def acquiphrase ():
#acquisition de la phrase à analyser    
    phrase = str(input("entrez votre phrase : "))
    phrase = phrase.split()
    return phrase

def conversion(phrase):
# transformation de la phrase en liste de chiffre qui représente l'état
    etat = []
    for mots in phrase :
        if mots in dictionnaire :
            etat.append(dictionnaire[mots])
    return etat

def analyse(dico,phrase):
#pour chaque valeur de notre liste de chiffre on va définir l'etat correspondant en fonction de notre dicoetat 
#notre fonction s'arrete après le dernier état et on regarde si la phrase et correcte ou non (8 ou 9)
    etat=0
    for i in phrase:
        
        etat=dico[etat][i]
        print(etat)
    
        if etat in [8, 9]:
            return etat == 9