import time
import random
import matplotlib.pyplot as plt
import copy

# Question 1
def mixList(listToMix:list[int])->list[int]:
  """
  Mélange une liste d'entier

  Args:
      listToMix (list[int]): Liste d'entier à mélanger

  Returns:
      list[int]: Liste d'entier mélangée
  """
  listIndexRandom = [] # une liste d'index uniques dans des places aléatoires 
  listMixed = []
  
  while len(listIndexRandom) < len(listToMix): # ajoute les index de manière unique et aléatoires
    nbRandom = random.randint(0, len(listToMix)-1)
    if nbRandom not in listIndexRandom:
      listIndexRandom.append(nbRandom)
      listMixed.append(listToMix[nbRandom])
  return listMixed

# Question 2
def chooseElementList(listInWhichToChoose: list[any])-> any:
  """
  Choisi un élément aléatoire dans une liste de quelconque éléments.

  Args:
      listInWhichToChoose (list): Une liste de quelconque éléments

  Returns:
      Any:  élément aléatoire de la liste listInWhichToChoose
  """
  return listInWhichToChoose[random.randint(0, len(listInWhichToChoose)-1)]

def extractElementsList(listInWhichToChoose: list[any], intNbrOfElementToExtract: int)-> list[any]:
  if len(listInWhichToChoose) < intNbrOfElementToExtract:
    raise ValueError ('Le nombre d\'élément à éxtraire est plus grand que la liste donnée. Pas bien')
  listTemp = copy.deepcopy(listInWhichToChoose)
  listResultat = []
  for i in range(intNbrOfElementToExtract):
    eltAleatoire = chooseElementList(listTemp)
    listResultat.append(eltAleatoire)
    listTemp.remove(eltAleatoire)
  return listResultat


# Question 1 Tests
def testMix():
  listTailles = [10, 100, 1000, 10000]
  mixTimesList = []
  shuffleTimesList = []

  for size in listTailles:
    lst = list(range(size))

    startTime = time.perf_counter()
    mixList(lst)
    endTime = time.perf_counter()
    mixTimesList.append(endTime - startTime)

    startTime = time.perf_counter()
    random.shuffle(lst)
    endTime = time.perf_counter()
    shuffleTimesList.append(endTime - startTime)

  plt.plot(listTailles, mixTimesList, label='mixList')
  plt.plot(listTailles, shuffleTimesList, label='random.shuffle')
  plt.xlabel('Taille de la liste')
  plt.ylabel('Temps (seconde)')
  plt.legend()
  plt.title('Performance Comparison')
  plt.show()
  
# Question 2 Tests
def testExtract():
  listTailles = [10, 100, 1000, 10000]
  extractTimesList = []
  sampleTimesList = []

  for size in listTailles:
    lst = list(range(size))

    startTime = time.perf_counter()
    extractElementsList(lst, size//2)
    endTime = time.perf_counter()
    extractTimesList.append(endTime - startTime)
    
    startTime = time.perf_counter()
    random.sample(lst, size//2)
    endTime = time.perf_counter()
    sampleTimesList.append(endTime - startTime)

  plt.plot(listTailles, extractTimesList, label='extractElementsList')
  plt.plot(listTailles, sampleTimesList, label='random.sample')
  plt.xlabel('Taille de la liste')
  plt.ylabel('Temps (seconde)')
  plt.legend()
  plt.title('Performance Comparison')
  plt.show()


if __name__ == "__main__":
  testMix()
  testExtract()