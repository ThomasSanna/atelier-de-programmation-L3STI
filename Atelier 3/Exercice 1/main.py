import re # sers pour regex


def nomComplet(chaineEntree: str) -> str:
    """
    Formate une chaîne d'entrée en nom complet avec le nom en majuscules et le prénom avec la première lettre en majuscule.

    Args:
        chaineEntree (str): La chaîne d'entrée au format 'nom prenom'.

    Returns:
        str: La chaîne formatée avec le nom en majuscules et le prénom avec la première lettre en majuscule.

    Raises:
        ValueError: Si la chaîne d'entrée n'est pas au format 'nom prenom'.
    """
    parties = chaineEntree.split()
    if len(parties) != 2:
        raise ValueError("La chaîne d'entrée doit être au format 'nom prenom'")
    nom, prenom = parties
    return f"{nom.upper()} {prenom.capitalize()}" # upper() met toutes les lettre en majuscule. capitalize(), seulement la premiere.

assert nomComplet('probleme michel') == 'PROBLEME Michel'


def estMail(chaineEntree: str) -> (int, int):
    """
    Vérifie si une chaîne d'entrée est une adresse email valide.

    Args:
        chaineEntree (str): La chaîne d'entrée à vérifier.

    Returns:
        tuple: Un tuple (1, 0) si l'adresse email est valide, sinon un tuple (0, code_erreur) où code_erreur indique le type d'erreur:
            - 1: Partie locale vide
            - 2: Absence de '@'
            - 3: Nom de domaine vide
            - 4: Absence de '.'
            - 5: Point en premier/dernier caractère
            - 6: Deux points consécutifs
            - 7: Caractères interdits

    """
    # gestion d'erreur d'absence de @
    if '@' not in chaineEntree:
        return (0, 2)
    
    partieLocale, partieDomaine = chaineEntree.split('@', 1) # 1 pour spliter seulement avec le premier "@" 
    
    # gestion d'erreur d'absence de partie locale
    if not partieLocale:
        return (0, 1)
    
    # gestion d'erreur d'absence de point
    if '.' not in partieDomaine:
        return (0, 4)
    
    nomDomaine, extensionDomaine = partieDomaine.rsplit('.', 1) # rsplit commence à partir de la droite. 1 pour spliter seulement avec le dernier "."
    
    # gestion d'erreur d'absence de nom de domaine
    if not nomDomaine:
        return (0, 3)
    
    # gestion d'erreur de points au début/fin
    if partieLocale[0]=='.' or partieLocale[-1]=='.' or nomDomaine[0]=='.' or nomDomaine[-1]=='.':
        return (0, 5)
    
    # gestion d'erreur de doubles points
    if '..' in chaineEntree:
        return (0, 6)
    
    # gestion des caractères interdits
    CARACTERES_INTERDITS = '()<>@,;:\\"[]'
    chaineEntreeSansArobase = partieDomaine + partieLocale
    erreur = False
    i = 0
    while not erreur and i<len(chaineEntreeSansArobase):
        if chaineEntreeSansArobase[i] in CARACTERES_INTERDITS:
            erreur = True
        i += 1
    if erreur:
        return (0, 7)
    
    return (1, 0)


# Exemple de code avec regex :

def verifMailRegex(email: str)->bool:
    """
    Vérifie si un mail est correcte. Ne renvoie pas de statut d'erreur, seulement un booléen.

    Args:
        email (_type_): _description_

    Returns:
        _type_: _description_
    """
    email_regex = r'^[A-Za-z0-9\._%+\-]+@[A-Za-z0-9\.\-]+\.[A-Za-z]{2,}$'
    # r : raw string. Permet de ne pas interpréter les caractères spéciaux comme des caractères spéciaux. Ce qui simplifie l'écriture des regex.
    # Exemple sans le r à la ligne 111.
    
    # ^ : début de la chaîne
    # [A-Za-z0-9\._%+\-]+ : partie locale de l'email. "." et "-" ont besoin d'être précédés d'un "\" car ils sont des caractères spéciaux en regex. "+" à la fin du crochet signifie que le caractère précédent doit être présent au moins une fois.
    # @ : arobase
    # [A-Za-z0-9\.\-]+ : nom de domaine. "." et "-" ont besoin d'être précédés d'un "\" car ils sont des caractères spéciaux en regex. "+" à la fin du crochet signifie que le caractère précédent doit être présent au moins une fois.
    # \. : point
    # [A-Za-z]{2,} : extension de domaine. "{2,}" signifie que le caractère précédent doit être présent au moins 2 fois.
    # $ : fin de la chaîne
    
    # Exemple sans le r:
    email_regex = '^[A-Za-z0-9\\.\\_\\%\\+\\-]+@[A-Za-z0-9\\.\\-]+\\.[A-Za-z]{2,}$'
    
    if re.match(email_regex, email):
        return True
    else:
        return False




def main():
    assert estMail('bisgambiglia_paul@univ-corse.fr') == (1, 0)
    assert estMail('20224444@gmail.com') == (1, 0)

    assert estMail('bisgambiglia_paulOuniv-corse.fr') == (0, 2)

    assert estMail('bisgambiglia_paul@univ-corsePOINTfr') == (0, 4)

    assert estMail('.bisgambiglia_paul@univ-corse.fr') == (0, 5)
    assert estMail('bisgambiglia_paul@.univ-corse.fr') == (0, 5)
    assert estMail('bisgambiglia_paul@univ-corse..fr') == (0, 5)

    assert estMail('bisgambigli..a_paul@univ-corse.fr') == (0, 6)

    assert estMail('bisgam&bi\glia_paul@univ-corse.fr') == (0, 7)

    assert estMail('@univ-corse.fr') == (0, 1)
    
    print("Tous les tests ont été effectués pour la fonction estMail.\n")
    
    print("Tests de la fonction verifMailRegex")
    emails = [
        "exemple@test.com",
        "nom.prenom@example.fr",
        "invalid-email@",
        "nom+special%mail@domain.com",
        "nom_sans_domaine@exemple"
    ]

    for email in emails:
        print(f"Vérification de l'email \"{email}\": {verifMailRegex(email)}")

    
if __name__ == "__main__":
    main()