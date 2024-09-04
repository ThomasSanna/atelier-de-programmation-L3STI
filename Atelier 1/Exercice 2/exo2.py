"""
Ce module fournit une fonction pour déterminer si une année est bissextile.

Fonctions:
    estBissextile(annee: int) -> bool:
        Détermine si une année donnée est bissextile.

    test() -> None:
        Effectue et imprime plusieurs résultats de la fonction estBissextile.

Exemple:
    >>> estBissextile(2020)
    True
    >>> estBissextile(1900)
    False
"""

def estBissextile(annee: int) -> bool:
    """
    Détermine si une année donnée est bissextile.

    Args:
        annee (int): L'année à vérifier.

    Returns:
        bool: True si l'année est bissextile, False sinon.
    """
    divPar4 = annee % 4 == 0
    divPar100 = annee % 100 == 0
    divPar400 = annee % 400 == 0
    return (divPar4 and not divPar100) or divPar400

def test() -> None:
    """
    Effectue et imprime plusieurs résultats de la fonction estBissextile.
    """
    print(estBissextile(2020))  # True
    print(estBissextile(1900))  # False
    print(estBissextile(2000))  # True
    print(estBissextile(2021))  # False
    print(estBissextile(2400))  # True

test()