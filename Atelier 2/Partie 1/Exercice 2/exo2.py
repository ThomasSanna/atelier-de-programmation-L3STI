listeTest1 = [0, 2, 3, 1, 8, 9] # Sans répétition
listeTest2 = [0, 2, 3, 1, 8, 9, 4, 2, 3, 2] # Avec répétition
listeTriee = [0, 3, 4, 7, 8, 10, 13, 14, 17, 19, 20, 22, 25, 27, 30, 32, 33, 34, 37, 38, 39, 41, 43]


def position(lst:list, e:int)->int:
  for i in range(len(lst)):
    if lst[i] == e:
      return i
  return -1

def position2(lst:list, e:int)->int:
  i=0
  while i < len(lst):
    if lst[i] == e: 
      return i
    i += 1
  return -1

def nbOccurrences(lst:list, e:int)->int:
  occ = 0
  for elt in lst:
    o += 1 if e == elt else 0
  return occ

def estTriee(lst:list)->bool:
  triee = True
  i = 0
  while triee and i < len(lst)-1:
    if lst[i] > lst[i+1]:
      triee = False
    i+=1
  return triee

def estTriee2(lst:list)->bool:
  triee = True
  for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
      triee = False
  return triee

print(estTriee(listeTest1)) # False
print(estTriee2(listeTriee)) # True

# estTriee avec la boucle for n'est pas la meilleure car elle ne s'arrete pas dès lors que 
# l'on sait que la liste n'est pas triee (dès que triee = False)

def positionTri(lst:list, e:int)->int:
  lstTrie = sorted(lst)
  low = 0
  hight = len(lstTrie)-1
  while low <= hight:
    mid = low + (hight - low)//2
    if e < lstTrie[mid] :
      hight = mid - 1
    elif e > lstTrie[mid]:
      low = mid + 1
    else:
      return mid
  return -1

print(positionTri(listeTriee, 38)) # 19
print(positionTri(listeTriee, 10)) # 5
print(positionTri(listeTriee, 0)) # 0
print(positionTri(listeTriee, 12)) # -1


def aRepetitions(lst:list)->bool:
  T = []
  aRepet = False
  i = 0
  while not aRepet and i < len(lst):
    if lst[i] in T:
      aRepet = True
    else:
      T.append(lst[i])
    i += 1
  return aRepet