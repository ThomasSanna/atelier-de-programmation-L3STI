import random

def placesLettre(ch: str, mot: str) -> list:
    """
    Retourne les positions d'une lettre dans un mot.

    Args:
        ch (str): La lettre à chercher dans le mot.
        mot (str): Le mot dans lequel chercher la lettre.

    Returns:
        list: Une liste des positions de la lettre dans le mot.

    Raises:
        ValueError: Si l'entrée de la lettre n'est pas valide (longueur différente de 1).
    """
    # gestion des erreurs de saisie
    if len(ch) < 1:
        raise ValueError("Vous devez entrer une lettre.")
    elif len(ch) > 1:
        raise ValueError(f"Vous devez entrer qu'un seul caractère, pas {len(ch)}.")
    
    indRes = []
    for i, elt in enumerate(mot):
        if elt == ch:
            indRes.append(i)
    return indRes


def outputStr(mot: str, lPos: list) -> str:
    """
    Retourne une chaîne de caractères avec des lettres trouvées et des tirets pour les lettres non trouvées.

    Args:
        mot (str): Le mot à afficher partiellement.
        lPos (list): La liste des positions des lettres trouvées.

    Returns:
        str: Une chaîne de caractères avec les lettres trouvées et des tirets pour les lettres non trouvées.
    """
    res = ""
    for i in range(len(mot)):
        if i in lPos:
            res += mot[i]
        else:
            res += "-"
    return res


def dictionnaire(fichier: str) -> list:
    """
    Lit un fichier et retourne une liste de mots.

    Args:
        fichier (str): Le chemin du fichier à lire.

    Returns:
        list: Une liste de mots contenus dans le fichier.
    """
    lstRes = []
    with open(fichier, "r", encoding="utf-8") as f:
        for line in f:
            line = line.lower()
            line = (
                line.strip()
            )  # Utilisation de strip() pour enlever les espaces et les sauts de ligne
            if "-" not in line and " " not in line and "'" not in line:
                lstRes.append(line.strip())
    return lstRes


def getMaxStrLen(lst: list) -> int:
    """
    Retourne la longueur maximale des chaînes de caractères dans une liste.

    Args:
        lst (list): Une liste de chaînes de caractères.

    Returns:
        int: La longueur maximale des chaînes de caractères dans la liste.
    """
    maxLen = 0
    for e in lst:
        if len(e) > maxLen:
            maxLen = len(e)
    return maxLen


def buildDict(lstMots: list) -> dict:
    """
    Construit un dictionnaire où les clés sont les longueurs des mots et les valeurs sont des listes de mots de cette longueur.

    Args:
        lstMot (list): Une liste de mots.

    Returns:
        dict: Un dictionnaire avec les longueurs des mots comme clés et les listes de mots comme valeurs.
    """
    maxLen = getMaxStrLen(lstMots)
    dictBuilded = {i: [] for i in range(4, maxLen+1)}
    for mot in lstMots:
        dictBuilded[len(mot)].append(mot)
    return dictBuilded


def selectWord(sortedWords: dict, wordLen: int) -> str:
    """
    Sélectionne un mot aléatoire d'une longueur donnée dans un dictionnaire de mots triés par longueur.

    Args:
        sortedWords (dict): Un dictionnaire avec les longueurs des mots comme clés et les listes de mots comme valeurs.
        wordLen (int): La longueur du mot à sélectionner.

    Returns:
        str: Un mot aléatoire de la longueur spécifiée.
    """
    lenMotsDictN = len(sortedWords[wordLen])
    return sortedWords[wordLen][random.randint(0, lenMotsDictN-1)]


def demandeDifficulteGetWordLen() -> int:
    """
    Demande au joueur de choisir une difficulté et retourne la longueur du mot correspondant à cette difficulté.

    Returns:
        int: La longueur du mot correspondant à la difficulté choisie.
    """
    choixFait = False
    while not choixFait:
        difficulte = input('Choisissez la difficulté: easy/normal/hard  -> ')
        choixFait = True
        if difficulte == "easy":
            lenWord = random.randint(4, 6)
        elif difficulte == 'normal':
            lenWord = random.randint(7, 8)
        elif difficulte == 'hard':
            lenWord = random.randint(9, 12)
        else:
            choixFait = False
    return lenWord


def runGame(LST_MOTS: list, LST_PENDU: list):
    """
    Lance le jeu du pendu. Le joueur doit deviner un mot en entrant des lettres une par une.

    Le jeu continue jusqu'à ce que le joueur trouve toutes les lettres du mot ou fasse 5 erreurs.
    
    Args:
        LST_MOTS (list): Une liste de mots.
        LST_PENDU (list): Une liste de lignes pour dessiner le pendu.
        
    Raises:
        ValueError: Si une erreur survient lors de l'entrée de la lettre.
    """
    dictMot = buildDict(LST_MOTS)
    lenMot = demandeDifficulteGetWordLen()
    motATrouver = selectWord(dictMot, lenMot)
    
    print("Chut, le mot est : ", motATrouver)
    
    nbErreur = 0
    lstIndexTrouve = []

    while nbErreur < 5 and len(lstIndexTrouve) != len(motATrouver):
        print("\nMot à trouver:")
        print(outputStr(motATrouver, lstIndexTrouve))
        
        try:
            chr = input("\nEntrez une lettre (minuscule) -> ")
            chr = chr.lower() # tous les mots sont en minuscule, on converti alors automatiquement le caractère envoyé en minuscule pour éviter certaines erreurs
        except:
            raise ValueError("Un problème est survenu lors de l'entrée de la lettre: Manipulation impossible.")

        try:
            lstIndexRes = placesLettre(chr, motATrouver) # nous renvoie une liste d'index ou le caractère se trouve dans le mot à trouver
        except ValueError as e:
            raise ValueError (str(e) + ": Impossible de placer la lettre.")
        
        if lstIndexRes == []: # càd si la lettre n'a pas été touvée dans le mot
            print("\nErreur ! La lettre " + chr + " n'est pas dans le mot cherché ! \n")
            nbErreur += 1
            
            if nbErreur > 0:
                print(f"Pendu : {nbErreur}/5 olala")
            for ligne in range(nbErreur): # A chaque nombre d'erreur, on ajoute une ligne de LST_PENDU (une ligne = un élément)
                print(LST_PENDU[ligne])
        else:
            lstIndexTrouve += lstIndexRes # ex: [1, 2] + [3, 4] = [1, 2, 3, 4]

    if nbErreur == 5: # il est necessaire de verifier nbErreur car sortir de la boucle while peut signifier avoir gagné ou avoir perdu
        print("\nPerdu !")
    else:
        print("\nBravo ! Le mot était bien ", motATrouver, "!")


def main():
    """
    Point d'entrée du programme
    """
    assert placesLettre("m", "maman") == [0, 2]
    
    assert outputStr("bonjour", [0, 1, 4]) == "bo--o--"
    
    LST_MOTS = dictionnaire("Atelier 3/Exercice 3/noms-capitales.txt")
    LST_PENDU = ["|---] ", "| O ", "| T ", "|/ \ ", "|______"]
    
    runGame(LST_MOTS, LST_PENDU)
    
if __name__ == "__main__":
    main()