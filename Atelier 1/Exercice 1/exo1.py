"""
Ce module fournit une fonction pour déterminer la catégorie de l'IMC (Indice de Masse Corporelle) en fonction d'une valeur donnée.

Dictionnaire:
    dicoIMC (dict): Un dictionnaire où les clés sont des tuples représentant des intervalles d'IMC et les valeurs sont des chaînes de caractères décrivant la catégorie de l'IMC.

Fonctions:
    messageImc(imc: float) -> str:
        Retourne la catégorie de l'IMC pour une valeur d'IMC donnée.

    test() -> None:
        Effectue et imprime plusieurs résultats de la fonction messageImc.

Exemple:
    >>> print(messageImc(22))
    Corpulence normale
"""

import math

DICO_IMC = {
    (0, 16.5): "Dénutrition ou famine",
    (16.5, 18.5): "Maigreur",
    (18.5, 25): "Corpulence normale",
    (25, 30): "Surpoids",
    (30, 35): "Obésité modérée",
    (35, 40): "Obésité sévère",
    (40, math.inf): "Obésité morbide"
}

def messageImc(imc: float) -> str:
    """
    Retourne la catégorie de l'IMC pour une valeur d'IMC donnée.

    Args:
        imc (float): La valeur de l'IMC.

    Returns:
        str: La catégorie de l'IMC correspondant à la valeur donnée.
    """
    if imc < 0:
        return "L'IMC ne peut pas être négatif"
        
    listeIMC = list(DICO_IMC.keys())
    i = 0
    while not (listeIMC[i][0] <= imc and listeIMC[i][1] >= imc):
        i += 1
    return DICO_IMC[listeIMC[i]]

def test() -> None:
    """
    Effectue et imprime plusieurs résultats de la fonction messageImc.
    """
    print(messageImc(-19.0))  # L'IMC ne peut pas être négatif
    print(messageImc(10.0))   # Dénutrition ou famine
    print(messageImc(20.0))   # Corpulence normale
    print(messageImc(32.0))   # Obésité modérée
    print(messageImc(50.0))   # Obésité morbide

test()