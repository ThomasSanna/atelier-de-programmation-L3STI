"""
Ce module contient des fonctions pour calculer l'âge d'une personne à partir de sa date de naissance,
vérifier si une personne est majeure, et tester l'accès basé sur l'âge.

Fonctions:
    estBissextile(annee: int) -> bool:
        Détermine si une année est bissextile.
        Paramètres:
            annee (int): L'année à vérifier.
        Retourne:
            bool: True si l'année est bissextile, False sinon.

    age(dateNaissance: str) -> int:
        Calcule l'âge d'une personne à partir de sa date de naissance.
        Paramètres:
            dateNaissance (str): La date de naissance au format 'JJ/MM/AAAA'.
        Retourne:
            int: L'âge de la personne en années.
        Lève:
            ValueError: Si la date de naissance n'est pas valide.

    estMajeur(dateNaissance: str) -> bool:
        Vérifie si une personne est majeure (18 ans ou plus).
        Paramètres:
            dateNaissance (str): La date de naissance au format 'JJ/MM/AAAA'.
        Retourne:
            bool: True si la personne est majeure, False sinon.

    testAcces():
        Demande la date de naissance de l'utilisateur, calcule son âge, et affiche un message
        indiquant si l'accès est autorisé ou interdit en fonction de l'âge.
        Cette fonction ne prend aucun paramètre et ne retourne rien.
"""

from datetime import date

def estBissextile(annee: int) -> bool:
    """ Détermine si une année est bissextile.
        Args:
            annee (int): L'année à vérifier.
        Returns:
            bool: True si l'année est bissextile, False sinon.
    """
    divPar4 = annee % 4 == 0
    divPar100 = annee % 100 == 0
    divPar400 = annee % 400 == 0
    return (divPar4 and not divPar100) or divPar400
  
# Le jour de Février va être modifié dans la fonction dateEstValide:
# joursFinDeMois[1] est temporairement égal à -1: 29 si bisextile, sinon 28
# voir ligne 69
joursFinDeMois = [31, -1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #joursFinDeMois n'est donc pas une constante

def dateEstValide(jour:int, mois:int, annee:int)->bool:
  """ Détermine si une date est Valide selon plusieurs critères.

  Args:
      jour (int): jour de la date
      mois (int): mois de la date
      annee (int): année de la date

  Returns:
      bool: renvoie True ou False si la date est valide ou non.
  """
  if jour < 1 or mois < 1 or mois > 12:
    return False
  
  anneeBisextile = estBissextile(annee)
  joursFinDeMois[1] = 29 if anneeBisextile else 28
  return jour <= joursFinDeMois[mois-1]

def saisieDateNaissance()->str:
  """Permet de saisir une date de naissance et vérifier sa conformité

  Returns:
      str: Renvoie la date de naissance sous forme "JJ-MM-AAAA"
  """
  dateIncorrecte = True
  while dateIncorrecte:
    dateNaissance = input("Saisissez votre date de naissance (JJ-MM-AAAA) -> ")
    if len(dateNaissance) == 10 and dateNaissance[2] == '-' and dateNaissance[5] == '-':
      jour, mois, annee = dateNaissance.split('-')
      if dateEstValide(int(jour), int(mois), int(annee)):
        dateIncorrecte = False
      else:
        print("La date fournie n'est pas valide. Veuillez recommencer\n")
    else:
      print('Erreur lors de la saisie. Veuillez recommencer\n')
    return dateNaissance

  
def age(dateNaissance:str)->int:
  """_summary_

  Args:
      dateNaissance (str): La date de naissance, sous forme de chaine de caractère "JJ-MM-AAAA"

  Raises:
      ValueError: Si la date de naissance n'est pas valide en utilisant la fonction dateEstValide(), Erreur

  Returns:
      int: Age de la personne
  """
  jour, mois, annee = map(int, dateNaissance.split('-')) # map convertis en int chaque element de dateNaissance.split()
  if dateEstValide(jour, mois, annee):
    anneeNow, moisNow, _ = map(int, str(date.today()).split('-'))
    diffAnnee = anneeNow - annee
    diffMois = moisNow - mois
    while diffMois < 0:
      diffAnnee -= 1
    return diffAnnee
  else:
    raise ValueError("La date n'est pas valide")
    

def estMajeur(dateNaissance:str)->bool:
  """Vérifie si la personne est majeure selon sa date de naissance.

  Args:
      dateNaissance (str): La date de naissance, sous forme de chaine de caractère "JJ-MM-AAAA".

  Returns:
      bool: Renvoie True si la personne est majeure, False sinon.
  """
  return age(dateNaissance) >= 18

def testAcces():
  """ Test et affiche les différents résultats des fonctions """
  dateNaissance = saisieDateNaissance()
  agePersonne = age(dateNaissance)
  res = ''
  if estMajeur(dateNaissance):
    res += "Bonjour, vous avez " + str(agePersonne) + " ans. Accès autorisé."
  else:
    res += "Désolé, vous avez " + str(agePersonne) + " ans. Accès interdit."
  print(res)
    
testAcces()