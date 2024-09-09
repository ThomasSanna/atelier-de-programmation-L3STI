def motsNLettres(listeMots: list, n: int) -> list:
    """
    Retourne une liste de mots ayant exactement n lettres.

    Args:
        listeMots (list): La liste des mots à filtrer.
        n (int): Le nombre de lettres que les mots doivent avoir.

    Returns:
        list: Une liste de mots ayant exactement n lettres.
    """
    resultats = []
    for mot in listeMots:
        if len(mot) == n:
            resultats.append(mot)
    return resultats


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
        raise ValueError(f"Le préfixe '{prefixe}' est plus grand que le mot '{mot}', impossible de mettre en marche la fonction.")
    
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
        raise ValueError(f"Le suffixe '{suffixe}' est plus grand que le mot '{mot}', impossible de mettre en marche la fonction.")
    
    longSuffixe = len(suffixe)
    return mot[-longSuffixe:] == suffixe


def finissentPar(listeMots: list, suffixe: str) -> list:
    """
    Retourne une liste de mots finissant par un suffixe donné.

    Args:
        listeMots (list): La liste des mots à filtrer.
        suffixe (str): Le suffixe que les mots doivent avoir à la fin.

    Returns:
        list: Une liste de mots finissant par le suffixe.
    """
    resultats = []
    for mot in listeMots:
        try:
            if finitPar(mot, suffixe):
                resultats.append(mot)
        except ValueError as e:
            # Lever l'exception pour que l'appelant puisse la gérer
            raise e
            # on pourrait aussi print(e) pour ne pas arrêter l'éxécution du code.
    return resultats


def commencentPar(listeMots: list, prefixe: str) -> list:
    """
    Retourne une liste de mots commençant par un préfixe donné.

    Args:
        listeMots (list): La liste des mots à filtrer.
        prefixe (str): Le préfixe que les mots doivent avoir au début.

    Returns:
        list: Une liste de mots commençant par le préfixe.
    """
    resultats = []
    for mot in listeMots:
        try:
            if commencePar(mot, prefixe):
                resultats.append(mot)
        except ValueError as e:
            # Lever l'exception pour que l'appelant puisse la gérer
            raise e
            # on pourrait aussi print(e) pour ne pas arrêter l'éxécution du code.
    return resultats


def listeMots(listeMots: list, prefixe: str, suffixe: str, longueur: int) -> list:
    """
    Retourne une liste de mots qui commencent par un préfixe, finissent par un suffixe et ont une longueur donnée.

    Args:
        listeMots (list): La liste des mots à filtrer.
        prefixe (str): Le préfixe que les mots doivent avoir au début.
        suffixe (str): Le suffixe que les mots doivent avoir à la fin.
        longueur (int): La longueur que les mots doivent avoir.

    Returns:
        list: Une liste de mots répondant aux critères.
    """
    motsPrefixe = commencentPar(listeMots, prefixe)
    motsSuffixe = finissentPar(motsPrefixe, suffixe)
    motsLongueurDonnee = motsNLettres(motsSuffixe, longueur)
    return motsLongueurDonnee


def dictionnaire(fichier: str) -> list:
    """
    Lit un fichier et retourne une liste de mots.

    Args:
        fichier (str): Le chemin du fichier à lire.

    Returns:
        list: Une liste de mots contenus dans le fichier.
    """
    resultats = []
    with open(fichier, 'r', encoding='utf-8') as f:
        for line in f:
            resultats.append(line.strip())  # Utilisation de strip() pour enlever les espaces et les sauts de ligne
    return resultats


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
assert commencentPar(LST_MOT, "a") == ["a", "aurevoir", "abajour", "aimer"]

assert listeMots(LST_MOT, "bon", "jour", 7) == ["bonjour"]
assert listeMots(LST_MOT, "a", "ir", 5) == []
assert listeMots(LST_MOT, "re", "ir", 6) == ["revoir"]

assert dictionnaire('Atelier 3/Exercice 2/mots.txt') == ['bonjour', 'bonsoir', 'ça', 'va', 'moi', 'super', 'merci', 'je', 'vous', 'en', 'prie', 'non', 'pas', 'de', 'soucis']