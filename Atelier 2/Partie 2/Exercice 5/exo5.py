nbEmplacement = 4
lObjets = [1, 2, 2, 3, 4, 5, 5]

def maxOccurence(lst:list)->int:
  """
  Retourne le nombre maximum d'occurrences d'un élément dans la liste lst.

  Args:
      lst (list): La liste des éléments.

  Returns:
    int: Le nombre maximum d'occurrences d'un élément dans la liste.
  """
  maxi = 0
  for i in range(len(lst)):
    # vérifie si L'élément courant a plus d'occurrences que le maximum actuel
    if maxi < lst.count(lst[i]):
      maxi = lst.count(lst[i])
  return maxi

def rangerParNombreOccurence(lst:list)->list:
  """
  Trie la liste lst par nombre d'occurrences décroissantes des éléments.
     
  Args:
      lst (list): La liste des éléments.
     
  Returns:
      list: La liste triée par nombre d'occurrences décroissantes.
  """
  lst.sort()
  maxOcc = maxOccurence(lst)
  # crée une liste de listes temporaires pour stocker les éléments par occurrences
  lTemp = [[] for i in range(maxOcc)]
  for elt in lst:
    # ajoute L'élément dans la liste temporaire correspondante
    lTemp[lst.count(elt)-1].append(elt)
  lRes = []
  for i in range(len(lTemp)):
    # ajoute les éléments des listes temporaires à la liste de résultat
    lRes += lTemp[len(lTemp)-(i+1)]
  return lRes

def agenceObjetVitrines(nbEmplacement:int, lObjets:list)->list:
  """
  Organise les objets dans les vitrines en fonction du nombre d'emplacements disponibles.
         
  Args:
      nbEmplacement (int): Le nombre d'emplacements disponibles par vitrine.
      lObjets (list): La liste des objets à organiser.
       
  Returns:
      list: Une liste de deux vitrines contenant les objets organisés.
  """
  lParOccurence = rangerParNombreOccurence(lObjets)
  vitrines = ([], [])
  for i in range(len(vitrines)):
    nbEmpPris = 0
    j = 0
    while j < len(lParOccurence) and nbEmpPris < nbEmplacement:
      # vérifie si L'objet n'est pas déjà dans la vitrine courante
      if lParOccurence[j] not in vitrines[i]:
        vitrines[i].append(lParOccurence[j])
        lParOccurence.pop(j)
        nbEmpPris += 1
      else:
        j += 1
  # trie les objets par ordre croissant dans chaque vitrine
  vitrines = map(sorted, vitrines)
  # Renvoie les deux vitrines et renvoie si les objets ont bien tous été pris ou non.
  return (list(vitrines), len(lParOccurence) == 0) 

print(agenceObjetVitrines(nbEmplacement, lObjets))