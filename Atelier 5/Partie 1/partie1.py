from random import randint
import copy

# exercice 1
def genListRandom(intNbr=10, intBInf=0, intBSup=10)->list[int]:
  """
  Génère une liste de nombres aléatoires

  Args:
      intNbr (int): Nombre d'élément dans la liste
      intBInf (int, optional): Nombre minimal possible dans la liste. Defaults to 0.
      intBSup (int, optional): Nombre maximal possible dans la liste. Defaults to 10.

  Returns:
      list: Liste de nombres aléatoires
      
  Raises:
      ValueError: Si l'intervalle de nombre est mal défini
  """
  if intBInf > intBSup:
    raise ValueError('L\'intervalle de nombre est mal défini')
  return [randint(intBInf, intBSup) for i in range(intNbr)]

# exercice 2
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
  
  while len(listIndexRandom) != len(listToMix): # ajoute les index de manière unique et aléatoires
    nbRandom = randint(0, len(listToMix)-1)
    if nbRandom not in listIndexRandom:
      listIndexRandom.append(nbRandom)
      listMixed.append(listToMix[nbRandom])
  print(listToMix, listIndexRandom, listMixed)
  return listMixed

# exercice 3
def chooseElementList(listInWhichToChoose: list[any])-> any:
  """
  Choisi un élément aléatoire dans une liste de quelconque éléments.

  Args:
      listInWhichToChoose (list): Une liste de quelconque éléments

  Returns:
      Any:  élément aléatoire de la liste listInWhichToChoose
      
  Raises:
      ValueError: Si la liste est vide
  """
  return listInWhichToChoose[randint(0, len(listInWhichToChoose)-1)]

# exercice 4
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

def main():
  """
  Point d'entrée du programme.
  """
  lstExemple1 = [1, 2, 3, 4, 5]
  print(f"Exo2 : Liste {lstExemple1} mélangée : {mixList(lstExemple1)}")
  
if __name__ == '__main__':
  main()