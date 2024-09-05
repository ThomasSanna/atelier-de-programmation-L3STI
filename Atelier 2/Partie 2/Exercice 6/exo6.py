# Question 1

def present(L: list, e: int) -> bool:
    """
    Vérifie si un élément est présent dans une liste.

    Args:
        L (list): La liste dans laquelle chercher l'élément.
        e (int): L'élément à chercher.

    Returns:
        bool: True si l'élément est présent, False sinon.
    """
    for elt in L:
        if elt == e:
            return True
    return False
 
def test_present(present: callable):
    """
    Teste la fonction `present` avec différents cas de test.

    Args:
        present (callable): La fonction à tester.
    """
    # test sur une liste vide
    if not present([], 1):
        print("SUCCES : test liste vide")
    else:
        print("ECHEC : test liste vide")
    
    # liste d'entiers pour les tests
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # test début de liste
    if present(L, 1):
        print("SUCCES : test debut")
    else:
        print("ECHEC : test debut")
    
    # test fin de liste
    if present(L, 10):
        print("SUCCES : test fin")
    else:
        print("ECHEC : test fin")
    
    # test milieu de liste
    if present(L, 5):
        print("SUCCES : test milieu")
    else:
        print("ECHEC : test milieu")
    
    # test absence dans la liste
    if not present(L, 11):
        print("SUCCES : test absence")
    else:
        print("ECHEC : test absence")

print("Test present()")
test_present(present)
print('\n')

# Question 2

# ----------- Versions non-corrigées --------------
#VERSION 1 
def present1 (L, e) : 
  for i in range (0, len(L), 1) :  
    if (L[i] == e) :  
      return(True) 
    else :  
      return (False)  
  return (False)

print("Test present1()")
test_present(present1) 
print('\n')
 
#VERSION 2 
def present2 (L, e) : 
  b=True 
  for i in range (0, len(L), 1) :  
    if (L[i] == e) :  
      b=True 
    else :  
      b=False 
  return (b) 

print("Test present2()")
test_present(present2) 
print('\n')
 
#VERSION 3 
def present3 (L, e) : 
  b=True 
  for i in range (0, len(L), 1) : 
    return (L[i] == e)
  
print("Test present3()")
test_present(present3) 
print('\n')
 
#VERSION 4 
def present4 (L, e) : 
  b=False 
  i=0 
  while (i<len(L) and b) :  
    if (L[i] == e) :  
      b=True 
  return (b)

print("Test present4()")
test_present(present4) 
print('\n')

# Question 3

# ----------- Versions corrigées --------------
#VERSION 1 
def present1 (L, e) : 
  for i in range (0, len(L)) :  
    if (L[i] == e) :  
      return(True)
  return (False)

print("Test present1()")
test_present(present1) 
print('\n')
 
#VERSION 2 
def present2 (L, e) : 
  b=False 
  for i in range (0, len(L)) :  
    if (L[i] == e) :  
      b=True 
  return (b) 

print("Test present2()")
test_present(present2) 
print('\n')
 
#VERSION 3 
def present3 (L, e) : 
  b=False 
  for i in range (0, len(L)) :  
    if (L[i] == e) :  
      b = True 
  return (b) 
  
print("Test present3()")
test_present(present3) 
print('\n')
 
#VERSION 4 
def present4 (L, e) : 
  b=False 
  i = 0 
  while (i<len(L) and not b) :  
    if (L[i] == e) :  
      b=True 
    i += 1
  return (b)

print("Test present4()")
test_present(present4) 
print('\n')

# Question 4

def pos(L: list, e: int) -> list:
    """
    Retourne les positions d'un élément dans une liste.

    Args:
        L (list): La liste dans laquelle chercher les positions.
        e (int): L'élément dont on cherche les positions.

    Returns:
        list: Une liste des positions de l'élément dans la liste.
    """
    lInd = []
    for i in range(len(L)):
        if e == L[i]:
            lInd.append(i)
    return lInd

def test_pos(fonctionPos):
    """
    Teste la fonction `pos` avec différents cas de test.

    Args:
        fonctionPos (callable): La fonction à tester.
    """
    casTest = [
        ([1, 2, 3, 4, 2, 5], 2, [1, 4]),
        ([1, 2, 3, 4, 5], 6, []),
        ([1, 1, 1, 1, 1], 1, [0, 1, 2, 3, 4]),
        ([], 1, []),
        ([1, 2, 3, 4, 5], 3, [2])
    ]
    
    for (L, e, res) in (casTest):
        result = fonctionPos(L, e)
        if result == res:
            print(f"REUSSITE.")
        else:
            print(f"ECHEC: Résultat trouvé: {result}, Résultat attendu: {res}")

# Example usage
print("Test pos()")
test_pos(pos)
print('\n')

# ------ Fonctions non corrigées -------

# VERSION 1 
def pos1(L, e) : 
  Lres = list(L) 
  for i in range (0, len(L), 1) : 
    if (L[i] == e) : 
      Lres += [i]   
  return Lres 

print("Test pos1()")
test_pos(pos1)
print('\n')
 
# VERSION 2 
def pos2(L, e) : 
  Lres = list(L) 
  for i in range (0, len(L), 1) : 
    if (L[i] == e) : 
      Lres[i] = i   
  return Lres 
 
print("Test pos2()")
test_pos(pos2)
print('\n')
 
# VERSION 3 
def pos3(L, e) : 
  nb= L.count(e) 
  Lres = [0]*nb 
  for i in range (0, len(L), 1) : 
    if (L[i] == e) : 
      Lres.append(i)   
  return Lres 

print("Test pos3()")
test_pos(pos3)
print('\n')
 
# VERSION 4 
def pos4(L, e) : 
  nb= L.count(e) 
  Lres = [0]*nb 
  j=0 
  for i in range (0, len(L), 1) : 
    if (L[i] == e) : 
      Lres[j]= i  
  return Lres

print("Test pos4()")
test_pos(pos4)
print('\n')

# ------ Fonctions corrigées -------

# VERSION 1 
def pos1(L, e) : 
  Lres = [] # Lres = list(L) 
  for i in range (0, len(L)) : 
    if (L[i] == e) : 
      Lres += [i]   
  return Lres 

print("Test pos1()")
test_pos(pos1)
print('\n')
 
# VERSION 2 
def pos2(L, e) : 
  Lres = [] # Lres = list(L) 
  for i in range (0, len(L), 1) : 
    if (L[i] == e) : 
      Lres.append(i) # Lres[i] = i
  return Lres 
 
print("Test pos2()")
test_pos(pos2)
print('\n')
 
# VERSION 3 
def pos3(L, e) : 
  nb = L.count(e)
  j = 0
  Lres = [0]*nb 
  for i in range (0, len(L)) : 
    if (L[i] == e) : 
      Lres[j] = i # Lres.append(i)
      j += 1 # Incrémentation de J
  return Lres

print("Test pos3()")
test_pos(pos3)
print('\n')
 
# VERSION 4 
def pos4(L, e) : 
  nb = L.count(e) 
  Lres = [0]*nb 
  j = 0 
  for i in range (0, len(L)) : 
    if (L[i] == e) : 
      Lres[j] = i  
      j += 1 # Incrémentation de J !!
  return Lres

print("Test pos4()")
test_pos(pos4)
print('\n')