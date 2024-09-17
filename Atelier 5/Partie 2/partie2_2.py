import time
import matplotlib.pyplot as plt
import random
import copy

# Exercice 6
# Question 1
def sortList(lst: list[int])->list[int]:
  """ 
  Trie une liste d'entiers
  
  Args:
      lst (list[int]): Liste d'entiers à trier
      
  Returns:
      list[int]: Liste d'entiers triée
  """
  lstTriee = copy.deepcopy(lst)
  if len(lstTriee) <= 1:
      return lstTriee
  pivot = lstTriee[len(lstTriee) // 2]
  moins = [elt for elt in lstTriee if elt < pivot]
  egal = [elt for elt in lstTriee if elt == pivot]
  plus = [elt for elt in lstTriee if elt > pivot]
  return sortList(moins) + egal + sortList(plus)

# Question 2
def testQ1():
  listTailles = [10, 100, 1000, 10000]
  question1TimesList = []
  sortedTimesList = []

  for size in listTailles:
    lst = list(-i-size for i in range(size))

    startTime = time.perf_counter()
    sortList(lst)
    endTime = time.perf_counter()
    question1TimesList.append(endTime - startTime)
    
    startTime = time.perf_counter()
    sorted(lst)
    endTime = time.perf_counter()
    sortedTimesList.append(endTime - startTime)

  plt.plot(listTailles, question1TimesList, label='SortList')
  plt.plot(listTailles, sortedTimesList, label='Sorted de python')
  plt.xlabel('Taille de la liste')
  plt.ylabel('Temps (seconde)')
  plt.legend()
  plt.title('Performance Comparison')
  plt.show()


# Exercice 7
# Question 1
def triStupide(lst:list[int])-> list[int]:
  """
  Trie une liste d'entier

  Args:
      lst (list[int]): Liste d'entier à trier

  Returns:
      list[int]: Liste d'entier triée
  """
  lstTriee = copy.deepcopy(lst)
  tentative = 0
  while lstTriee != sorted(lstTriee):
    tentative += 1
    random.shuffle(lstTriee)
  return lstTriee, str(tentative) + " tentatives"

# Question 2
def triInsertion(lst: list[int])-> list[int]:
  """
  Trie une liste d'entier

  Args:
      lst (list[int]): Liste d'entier à trier

  Returns:
      list[int]: Liste d'entier triée
  """
  lstTriee = copy.deepcopy(lst)
  for i in range(len(lstTriee)):
    x = lstTriee[i]
    j = i
    while j > 0 and lstTriee[j - 1] > x:
      lstTriee[j] = lstTriee[j-1]
      j -= 1
    lstTriee[j] = x
    
# Question 3
def triSelection(lst: list[int])-> list[int]:
  """
  Trie une liste d'entier

  Args:
      lst (list[int]): Liste d'entier à trier

  Returns:
      list[int]: Liste d'entier triée
  """
  lstTriee = copy.deepcopy(lst)
  for i in range(len(lstTriee)):
    minIndex = i
    for j in range(i+1, len(lstTriee)):
      if lstTriee[j] < lstTriee[minIndex]:
        minIndex = j
    lstTriee[i], lstTriee[minIndex] = lstTriee[minIndex], lstTriee[i]
    
# Question 4
def triABulles(lst: list[int])-> list[int]:
  """
  Trie une liste d'entier

  Args:
      lst (list[int]): Liste d'entier à trier

  Returns:
      list[int]: Liste d'entier triée
  """
  lstTriee = copy.deepcopy(lst)
  for i in range(len(lstTriee)):
    for j in range(len(lstTriee)-1):
      if lstTriee[j] > lstTriee[j+1]:
        lstTriee[j], lstTriee[j+1] = lstTriee[j+1], lstTriee[j]
        
# Question 5
def triFusion(lst: list[int])-> list[int]:
  """
  Trie une liste d'entier

  Args:
      lst (list[int]): Liste d'entier à trier

  Returns:
      list[int]: Liste d'entier triée
  """
  lstTriee = copy.deepcopy(lst)
  if len(lstTriee) <= 1:
    return lstTriee
  else:
    milieu = len(lstTriee) // 2
    gauche = triFusion(lstTriee[:milieu])
    droite = triFusion(lstTriee[milieu:])
    return fusion(gauche, droite)
    
def fusion(gauche: list[int], droite: list[int]) -> list[int]:
  """
  Fusionne deux listes triées en une seule liste triée

  Args:
      gauche (list[int]): Première liste triée
      droite (list[int]): Deuxième liste triée

  Returns:
      list[int]: Liste fusionnée et triée
  """
  resultat = []
  i = j = 0

  while i < len(gauche) and j < len(droite):
    if gauche[i] < droite[j]:
      resultat.append(gauche[i])
      i += 1
    else:
      resultat.append(droite[j])
      j += 1

  resultat.extend(gauche[i:])
  resultat.extend(droite[j:])
  return resultat

# Question 6
def triParBase(lst: list[int]) -> list[int]:
  """
  Trie une liste d'entiers en utilisant le tri par base (radix sort)

  Args:
    lst (list[int]): Liste d'entiers à trier

  Returns:
    list[int]: Liste d'entiers triée
  """
  lstTriee = copy.deepcopy(lst)
  if not lstTriee:
    return lstTriee

  # Trouver le nombre maximum pour connaître le nombre de chiffres
  nombreMax = max(lstTriee)
  exposant = 1  # Exposant pour accéder à chaque chiffre (unité, dizaine, centaine, ...) (initialisé à 10^0)

  while nombreMax // exposant > 0:
    lstTriee = triComptage(lstTriee, exposant)
    exposant *= 10

  return lstTriee

def triComptage(lst: list[int], exposant: int) -> list[int]:
  """
  Trie une liste d'entiers en utilisant le tri par comptage basé sur un chiffre spécifique

  Args:
    lst (list[int]): Liste d'entiers à trier
    exposant (int): Exposant pour accéder à un chiffre spécifique

  Returns:
    list[int]: Liste d'entiers triée par le chiffre spécifié
  """
  taille = len(lst)
  sortie = [0] * taille # Liste de sortie (c'est la liste triée)
  compte = [0] * 10

  # Compter les occurrences des chiffres
  for i in range(taille):
    index = lst[i] // exposant
    compte[index % 10] += 1

  # Changer compte[i] pour qu'il contienne la position de ce chiffre dans sortie
  for i in range(1, 10):
    compte[i] += compte[i - 1]

  # Construire la sortie triée
  i = taille - 1
  while i >= 0:
    index = lst[i] // exposant
    sortie[compte[index % 10] - 1] = lst[i]
    compte[index % 10] -= 1
    i -= 1

  return sortie
  
# TESTS
def testsFonctions():
  lst = [random.randint(0, 100) for i in range(10)]
  
  start = time.perf_counter()
  sortList(lst)
  end = time.perf_counter()
  print("Temps d'execution du tri rapide : ", end - start)
  
  # start = time.perf_counter()
  # triStupide(lst)
  # end = time.perf_counter()
  # print("Temps d'execution du tri stupide : ", end - start)
  
  # start = time.perf_counter()
  # triStupide(lst)
  # end = time.perf_counter()
  # print("Temps d'execution du tri par insertion : ", end - start)
  
  start = time.perf_counter()
  triSelection(lst)
  end = time.perf_counter()
  print("Temps d'execution du tri par selection : ", end - start)
  
  start = time.perf_counter()
  triABulles(lst)
  end = time.perf_counter()
  print("Temps d'execution du tri à bulles : ", end - start)
  
  start = time.perf_counter()
  triFusion(lst)
  end = time.perf_counter()
  print("Temps d'execution du tri fusion : ", end - start)
  
  start = time.perf_counter()
  triParBase(lst)
  end = time.perf_counter()
  print("Temps d'execution du tri par base : ", end - start)

if __name__ == "__main__":
  # testQ1()
  testsFonctions()