"""
Ce module fournit des fonctions pour résoudre des équations quadratiques de la forme ax^2 + bx + c = 0.

Fonctions:
    discriminant(a: float, b: float, c: float) -> float:
        Calcule le discriminant de l'équation quadratique.
        
    racineUnique(a: float, b: float) -> float:
        Calcule la racine unique de l'équation quadratique lorsque le discriminant est nul.
        
    racineDouble(a: float, b: float, delta: float, num: int) -> float:
        Calcule l'une des deux racines de l'équation quadratique lorsque le discriminant est positif.
        
    strEquation(a: float, b: float, c: float) -> str:
        Retourne une représentation sous forme de chaîne de caractères de l'équation quadratique.
        
    solutionEquation(a: float, b: float, c: float) -> str:
        Retourne une chaîne de caractères décrivant les solutions de l'équation quadratique.
"""

import math

def discriminant(a: float, b: float, c: float) -> float:
    """
    Calcule le discriminant de l'équation quadratique ax^2 + bx + c = 0.
    
    Args:
        a (float): Coefficient de x^2.
        b (float): Coefficient de x.
        c (float): Terme constant.
        
    Returns:
        float: Le discriminant de l'équation quadratique.
    """
    return (b**2) - (4*a*c)

def racineUnique(a: float, b: float) -> float:
    """
    Calcule la racine unique de l'équation quadratique lorsque le discriminant est nul.
    
    Args:
        a (float): Coefficient de x^2.
        b (float): Coefficient de x.
        
    Returns:
        float: La racine unique de l'équation quadratique.
    """
    return -b/(2*a)

def racineDouble(a: float, b: float, delta: float, num: int) -> float:
    """
    Calcule l'une des deux racines de l'équation quadratique lorsque le discriminant est positif.
    
    Args:
        a (float): Coefficient de x^2.
        b (float): Coefficient de x.
        delta (float): Le discriminant de l'équation quadratique.
        num (int): Indicateur de la racine à calculer (1 pour la première racine, 2 pour la deuxième racine).
        
    Returns:
        float: La racine calculée de l'équation quadratique.
        
    Raises:
        ValueError: Si num n'est pas 1 ou 2.
    """
    if num == 1:
        return (-b + math.sqrt(delta)) / (2*a)
    elif num == 2:
        return (-b - math.sqrt(delta)) / (2*a)
    else:
        raise ValueError('Problème lors de la saisie de num')

def strEquation(a: float, b: float, c: float) -> str:
    """
    Retourne une représentation sous forme de chaîne de caractères de l'équation quadratique ax^2 + bx + c = 0.
    
    Args:
        a (float): Coefficient de x^2.
        b (float): Coefficient de x.
        c (float): Terme constant.
        
    Returns:
        str: La représentation sous forme de chaîne de caractères de l'équation quadratique.
    """
    return str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c)

def solutionEquation(a: float, b: float, c: float) -> str:
    """
    Retourne une chaîne de caractères décrivant les solutions de l'équation quadratique ax^2 + bx + c = 0.
    
    Args:
        a (float): Coefficient de x^2.
        b (float): Coefficient de x.
        c (float): Terme constant.
        
    Returns:
        str: Une chaîne de caractères décrivant les solutions de l'équation quadratique.
    """
    res = "Solution de l'équation " + strEquation(a, b, c) + '\n'
    delta = discriminant(a, b, c)
    if delta < 0:
        res += "Pas de racine réelle \n"
    elif delta == 0:
        res += "Racine unique: " + str(racineUnique(a, b)) + '\n'
    else:
        res += "Deux racines: " + str(racineDouble(a, b, delta, 1)) + " et " + str(racineDouble(a, b, delta, 2)) + '\n'
    return res

def equation(a:float, b:float, c:float):
    print(solutionEquation(a, b, c))

def test():
    equation(1, -3, 0)
    equation(2, 5, 1)
    equation(1, 1, 1)

test()
