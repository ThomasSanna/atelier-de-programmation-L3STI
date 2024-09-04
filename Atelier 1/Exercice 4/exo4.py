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
  
# NB : Le jour de Février va être modifié dans la fonction dateEstValide.
joursFinDeMois = [31, -1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

def dateEstValide(jour:int, mois:int, annee:int)->bool:
  if jour < 1 or mois < 1 or mois > 12:
    return False
  
  anneeBisextile = estBissextile(annee)
  joursFinDeMois[1] = 29 if anneeBisextile else 28
  if jour > joursFinDeMois[mois-1]: 
    return False
  else: 
    return True

def saisieDateNaissance():
  dateIncorrecte = True
  while dateIncorrecte:
    dateNaissance = input("Saisissez votre date de naissance (JJ/MM/AAAA) -> ")
    