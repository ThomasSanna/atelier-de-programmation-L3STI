def motsNLettres(lstMot: list, n: int) -> list:
    """
    Retourne une liste de mots ayant exactement n lettres.

    Args:
        lstMot (list): La liste des mots à filtrer.
        n (int): Le nombre de lettres que les mots doivent avoir.

    Returns:
        list: Une liste de mots ayant exactement n lettres.
    """
    lstRes = []
    for mot in lstMot:
        if len(mot) == n:
            lstRes.append(mot)
    return lstRes


def commencePar(mot: str, prefixe: str) -> bool:
    """
    Vérifie si un mot commence par un préfixe donné.

    Args:
        mot (str): Le mot à vérifier.
        prefixe (str): Le préfixe à chercher au début du mot.

    Returns:
        bool: True si le mot commence par le préfixe, False sinon.
    """
    if len(mot) < len(prefixe):
        raise ValueError('Le préfixe est plus grand que le mot, en gros')
    
    longPrefixe = len(prefixe)
    return mot[:longPrefixe] == prefixe


def finitPar(mot: str, suffixe: str) -> bool:
    """
    Vérifie si un mot finit par un suffixe donné.

    Args:
        mot (str): Le mot à vérifier.
        suffixe (str): Le suffixe à chercher à la fin du mot.

    Returns:
        bool: True si le mot finit par le suffixe, False sinon.
    """
    if len(mot) < len(suffixe):
        raise ValueError('Le suffixe est plus grand que le mot, en gros')
    
    longSuffixe = len(suffixe)
    return mot[-longSuffixe:] == suffixe


def finissentPar(lstMot: list, suffixe: str) -> list:
    """
    Retourne une liste de mots finissant par un suffixe donné.

    Args:
        lstMot (list): La liste des mots à filtrer.
        suffixe (str): Le suffixe que les mots doivent avoir à la fin.

    Returns:
        list: Une liste de mots finissant par le suffixe.
    """
    return [mot for mot in lstMot if finitPar(mot, suffixe)]


def commencentPar(lstMot: list, prefixe: str) -> list:
    """
    Retourne une liste de mots commençant par un préfixe donné.

    Args:
        lstMot (list): La liste des mots à filtrer.
        prefixe (str): Le préfixe que les mots doivent avoir au début.

    Returns:
        list: Une liste de mots commençant par le préfixe.
    """
    return [mot for mot in lstMot if commencePar(mot, prefixe)]


def listeMots(lstMots: list, prefixe: str, suffixe: str, longueur: int) -> list:
    """
    Retourne une liste de mots qui commencent par un préfixe, finissent par un suffixe et ont une longueur donnée.

    Args:
        lstMots (list): La liste des mots à filtrer.
        prefixe (str): Le préfixe que les mots doivent avoir au début.
        suffixe (str): Le suffixe que les mots doivent avoir à la fin.
        longueur (int): La longueur que les mots doivent avoir.

    Returns:
        list: Une liste de mots répondant aux critères.
    """
    motsPrefixe = commencentPar(lstMots, prefixe)
    motsSuffixe = finissentPar(motsPrefixe, suffixe)
    motsLongueurDonnee = motsNLettres(motsSuffixe, longueur)
    return motsLongueurDonnee
    # return list(set(commencentPar(lstMot, prefixe)) & set(finissentPar(lstMot, suffixe)) & set(motsNLettres(lstMot, n)))

def dictionnaire(fichier: str) -> list:
    """
    Lit un fichier et retourne une liste de mots.

    Args:
        fichier (str): Le chemin du fichier à lire.

    Returns:
        list: Une liste de mots contenus dans le fichier.
    """
    lstRes = []
    with open(fichier, 'r', encoding='utf-8') as f:
        for line in f:
            lstRes.append(line.strip())  # Utilisation de strip() pour enlever les espaces et les sauts de ligne
    return lstRes


# Liste de mots pour les tests
LST_MOT = ["jouer", "bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
"finir", "aimer"]

assert motsNLettres(LST_MOT, 5) == ['jouer', 'punir', 'finir', 'aimer']
assert motsNLettres(LST_MOT, 4) == ["jour", "cour"]
assert motsNLettres(LST_MOT, 7) == ['bonjour', 'pouvoir', 'abajour']

assert commencePar("bonjour", "bon") == True
assert commencePar("bonjour", "jour") == False
assert commencePar("aimer", "aim") == True

assert finitPar("bonjour", "jour") == True
assert finitPar("bonjour", "bon") == False
assert finitPar("aimer", "mer") == True

assert finissentPar(LST_MOT, "jour") == ["bonjour", "jour", "abajour"]
assert finissentPar(LST_MOT, "voir") == ["aurevoir", "revoir", "pouvoir"]
assert finissentPar(LST_MOT, "ir") == ['punir', 'aurevoir', 'revoir', 'pouvoir', 'finir']

assert commencentPar(LST_MOT, "bon") == ["bonjour"]
assert commencentPar(LST_MOT, "re") == ["revoir"]
assert commencentPar(LST_MOT, "a") == ["aurevoir", "abajour", "aimer"]

assert listeMots(LST_MOT, "bon", "jour", 7) == ["bonjour"]
assert listeMots(LST_MOT, "a", "ir", 5) == []
assert listeMots(LST_MOT, "re", "ir", 6) == ["revoir"]

assert dictionnaire('Atelier 3/Exercice 2/mots.txt') == ['bonjour', 'bonsoir', 'ça', 'va', 'moi', 'super', 'merci', 'je', 'vous', 'en', 'prie', 'non', 'pas', 'de', 'soucis']