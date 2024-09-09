def motsNLettres(listeMots: list, n: int) -> list:
    """
    Retourne une liste de mots ayant exactement n lettres.

    Args:
        listeMots (list): La liste des mots à filtrer.
        n (int): Le nombre de lettres que les mots doivent avoir.

    Returns:
        list: Une liste de mots ayant exactement n lettres.
    """
    resultats = [mot for mot in listeMots if len(mot) == n]
    return resultats

assert motsNLettres(["jouer", "bonjour", "punir", "jour", "aurevoir"], 5) == ["jouer", "punir"]
assert motsNLettres(["jour", "cour", "aimer"], 4) == ["jour", "cour"]
assert motsNLettres(["bonjour", "revoir", "pouvoir", "abajour", "aurevoir"], 7) == ["bonjour", "pouvoir", "abajour"]


def dictionnaire(fichier: str) -> list:
    """
    Lit un fichier et retourne une liste de mots.

    Args:
        fichier (str): Le chemin du fichier à lire.

    Returns:
        list: Une liste de mots contenus dans le fichier.
    """
    resultats = []
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            resultats = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Erreur : le fichier {fichier} n'a pas été trouvé.")
    return resultats

assert dictionnaire('Atelier 3/Exercice 2/mots.txt') == ['bonjour', 'bonsoir', 'ça', 'va', 'moi', 'super', 'merci', 'je', 'vous', 'en', 'prie', 'non', 'pas', 'de', 'soucis']

DICO = dictionnaire('Atelier 3/Exercice 2/mots.txt')


def motCorrespond(mot: str, motif: str) -> bool:
    """
    Vérifie si un mot correspond à un motif donné.

    Args:
        mot (str): Un mot.
        motif (str): Un motif de la forme 'a--e' où les tirets '-' indiquent des lettres quelconques.

    Returns:
        bool: True si le mot correspond au motif, False sinon.
    """
    if len(mot) != len(motif):
        return False
    for i in range(len(mot)):
        if motif[i] != '-' and motif[i] != mot[i]:
            return False
    return True

assert motCorrespond("bonjour", "b-nj--r") == True
assert motCorrespond("bonjour", "b-nj--t") == False
assert motCorrespond("aimer", "a-m-r") == True


def presente(lettre: str, mot: str) -> int:
    """
    Vérifie si une lettre est présente dans un mot.
    
    Args:
        lettre (str): Une lettre.
        mot (str): Un mot.
        
    Returns:
        int: La position de la lettre dans le mot, -1 si la lettre n'est pas présente.
    """
    return mot.find(lettre)

assert presente('b', 'bonjour') == 0
assert presente('j', 'bonjour') == 3
assert presente('z', 'bonjour') == -1


def motPossible(mot: str, lettres: str) -> bool:
    """
    Vérifie si un mot est possible avec un ensemble de lettres.
    
    Args:
        mot (str): Un mot.
        lettres (str): Un ensemble de lettres.
        
    Returns:
        bool: True si le mot est possible, False sinon.
    """
    for lettre in mot:
        if presente(lettre, lettres) == -1:
            return False
    return True

assert motPossible('bonjour', 'bonjoru') == True
assert motPossible('bonjour', '') == False


def motsOptimaux(dico: list, lettres: str) -> list:
    """
    Retourne une liste des mots les plus grands, possibles avec un ensemble de lettres.
    
    Args:
        dico (list): Une liste de mots.
        lettres (str): Un ensemble de lettres.
        
    Returns:
        list: Une liste des mots les plus grands possibles.
    """
    resultats = []
    longueurMaximale = 0
    for mot in dico:
        longueurMot = len(mot)
        if motPossible(mot, lettres) and longueurMot > longueurMaximale:
            resultats = [mot]
            longueurMaximale = longueurMot
        elif motPossible(mot, lettres) and longueurMot == longueurMaximale:
            resultats.append(mot)
    return resultats

assert motsOptimaux(DICO, 'bonjoruususotiurizprotyuiezamqoisnxcvbpaoizeur') == ['bonjour', 'bonsoir']
assert motsOptimaux(DICO, 'abc') == []
assert motsOptimaux(DICO, 'sueemrepci') == ['super', 'merci']