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
    return f"{nom.upper()} {prenom.capitalize()}"

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

    """
    if '@' not in chaineEntree:
        return (0, 2)
    
    partieLocale, partieDomaine = chaineEntree.split('@', 1) # 1 pour ne pas spliter les '@' suivants
    
    if not partieLocale:
        return (0, 1)
    
    if '.' not in partieDomaine:
        return (0, 4)
    
    nomDomaine, extensionDomaine = partieDomaine.rsplit('.', 1) # rsplit sert à partir de la droite pour ne pas spliter les '.' précédents
    
    if not nomDomaine:
        return (0, 3)
    
    return (1, 0)

# Tests
assert nomComplet('bisgambiglia paul') == 'BISGAMBIGLIA Paul'

assert estMail('bisgambiglia_paul@univ-corse.fr') == (1, 0)

assert estMail('bisgambiglia_paulOuniv-corse.fr') == (0, 2)

assert estMail('bisgambiglia_paul@univ-corsePOINTfr') == (0, 4)

assert estMail('@univ-corse.fr') == (0, 1)