# Fonction Exercice 1
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
  
# Fonction Exercice 2
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

dico = dictionnaire('Atelier 3/Exercice 2/mots.txt')
  

def motCorrespond(mot: str, motif: str)-> bool:
  """
  Vérifie si un mot correspond à un motif donné.

  Args:
      mot (str): Un mot.
      motif (str): Un motif de la forme 'a--e' où les tirets '-' indiquent des lettres quelconques.

  Returns:
      bool: True si le mot correspond au motif, False sinon.
  """
  if len(mot) != len(motif):
    return False
  for i in range(len(mot)):
    if motif[i] != '-' and motif[i] != mot[i]:
      return False
  return True


def presente(lettre: str, mot: str)-> int:
  """
  Vérifie si une lettre est présente dans un mot.
  
  Args:
      lettre (str): Une lettre.
      mot (str): Un mot.
      
  Returns:
      int: La position de la lettre dans le mot, -1 si la lettre n'est pas prés
  """
  for i in range(len(mot)):
    if mot[i] == lettre:
      return i
  return -1


def motPossibles (mot: str, lettres: str)-> bool:
  """
  Vérifie si un mot est possible avec un ensemble de lettres.
  
  Args:
      mot (str): Un mot.
      lettres (str): Un ensemble de lettres.
      
  Returns:
      bool: True si le mot est possible, False sinon.
  """
  for lettre in mot:
    if presente(lettre, lettres) == -1:
      return False
  return True

assert motPossibles('bonjour', 'bonjoru') == True


def motOptimaux (dico: list, lettres: str)-> list:
  """
  Retourne une liste des mots les plus grands, possibles avec un ensemble de lettres.
  
  Args:
      dico (list): Une liste de mots.
      lettres (str): Un ensemble de lettres.
      
  Returns:
      list: Une liste des mots les plus grands possibles.
  """
  lstRes = []
  lenMax = 0
  for mot in dico:
    if motPossibles(mot, lettres) and len(mot) > lenMax:
      lstRes = [mot]
      lenMax = len(mot)
    elif motPossibles(mot, lettres) and len(mot) == lenMax:
      lstRes.append(mot)
  return lstRes

assert motOptimaux(dico, 'bonjoruususotiurizprotyuiezamqoisnxcvbpaoizeur') == ['bonjour', 'bonsoir']