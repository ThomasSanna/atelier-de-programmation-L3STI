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
  


def dateEstValide(jour:int, mois:int, annee:int)->bool:
  anneeBisextile = estBissextile(annee)
  