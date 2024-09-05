# Question 1

def present(lst: list, e: int) -> bool:
    """
    Vérifie si un élément est présent dans une liste.

    Args:
        lst (list): La liste dans laquelle chercher lst'élément.
        e (int): lst'élément à chercher.

    Returns:
        bool: True si lst'élément est présent, False sinon.
    """
    for elt in lst:
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
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # test début de liste
    if present(lst, 1):
        print("SUCCES : test debut")
    else:
        print("ECHEC : test debut")
    
    # test fin de liste
    if present(lst, 10):
        print("SUCCES : test fin")
    else:
        print("ECHEC : test fin")
    
    # test milieu de liste
    if present(lst, 5):
        print("SUCCES : test milieu")
    else:
        print("ECHEC : test milieu")
    
    # test absence dans la liste
    if not present(lst, 11):
        print("SUCCES : test absence")
    else:
        print("ECHEC : test absence")

print("Test present()")
test_present(present)
print('\n')

# Question 2

# ----------- Versions non-corrigées --------------
#VERSION 1 
def present1 (lst, e) : 
  for i in range (0, len(lst), 1) :  
    if (lst[i] == e) :  
      return(True) 
    else :  
      return (False)  
  return (False)

print("Test present1()")
test_present(present1) 
print('\n')
 
#VERSION 2 
def present2 (lst, e) : 
  b=True 
  for i in range (0, len(lst), 1) :  
    if (lst[i] == e) :  
      b=True 
    else :  
      b=False 
  return (b) 

print("Test present2()")
test_present(present2) 
print('\n')
 
#VERSION 3 
def present3 (lst, e) : 
  b=True 
  for i in range (0, len(lst), 1) : 
    return (lst[i] == e)
  
print("Test present3()")
test_present(present3) 
print('\n')
 
#VERSION 4 
def present4 (lst, e) : 
  b=False 
  i=0 
  while (i<len(lst) and b) :  
    if (lst[i] == e) :  
      b=True 
  return (b)

print("Test present4()")
test_present(present4) 
print('\n')

# Question 3

# ----------- Versions corrigées --------------
#VERSION 1 
def present1 (lst, e) : 
  for i in range (0, len(lst)) :  
    if (lst[i] == e) :  
      return(True)
  return (False)

print("Test present1()")
test_present(present1) 
print('\n')
 
#VERSION 2 
def present2 (lst, e) : 
  b=False 
  for i in range (0, len(lst)) :  
    if (lst[i] == e) :  
      b=True 
  return (b) 

print("Test present2()")
test_present(present2) 
print('\n')
 
#VERSION 3 
def present3 (lst, e) : 
  b=False 
  for i in range (0, len(lst)) :  
    if (lst[i] == e) :  
      b = True 
  return (b) 
  
print("Test present3()")
test_present(present3) 
print('\n')
 
#VERSION 4 
def present4 (lst, e) : 
  b=False 
  i = 0 
  while (i<len(lst) and not b) :  
    if (lst[i] == e) :  
      b=True 
    i += 1
  return (b)

print("Test present4()")
test_present(present4) 
print('\n')

# Question 4

def pos(lst: list, e: int) -> list:
    """
    Retourne les positions d'un élément dans une liste.

    Args:
        lst (list): La liste dans laquelle chercher les positions.
        e (int): lst'élément dont on cherche les positions.

    Returns:
        list: Une liste des positions de lst'élément dans la liste.
    """
    lInd = []
    for i in range(len(lst)):
        if e == lst[i]:
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
    
    for (lst, e, res) in (casTest):
        result = fonctionPos(lst, e)
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
def pos1(lst, e) : 
  Lres = list(lst) 
  for i in range (0, len(lst), 1) : 
    if (lst[i] == e) : 
      Lres += [i]   
  return Lres 

print("Test pos1()")
test_pos(pos1)
print('\n')
 
# VERSION 2 
def pos2(lst, e) : 
  Lres = list(lst) 
  for i in range (0, len(lst), 1) : 
    if (lst[i] == e) : 
      Lres[i] = i   
  return Lres 
 
print("Test pos2()")
test_pos(pos2)
print('\n')
 
# VERSION 3 
def pos3(lst, e) : 
  nb= lst.count(e) 
  Lres = [0]*nb 
  for i in range (0, len(lst), 1) : 
    if (lst[i] == e) : 
      Lres.append(i)   
  return Lres 

print("Test pos3()")
test_pos(pos3)
print('\n')
 
# VERSION 4 
def pos4(lst, e) : 
  nb= lst.count(e) 
  Lres = [0]*nb 
  j=0 
  for i in range (0, len(lst), 1) : 
    if (lst[i] == e) : 
      Lres[j]= i  
  return Lres

print("Test pos4()")
test_pos(pos4)
print('\n')

# ------ Fonctions corrigées -------

# VERSION 1 
def pos1(lst, e) : 
  Lres = [] # Lres = list(lst) 
  for i in range (0, len(lst)) : 
    if (lst[i] == e) : 
      Lres += [i]   
  return Lres 

print("Test pos1()")
test_pos(pos1)
print('\n')
 
# VERSION 2 
def pos2(lst, e) : 
  Lres = [] # Lres = list(lst) 
  for i in range (0, len(lst), 1) : 
    if (lst[i] == e) : 
      Lres.append(i) # Lres[i] = i
  return Lres 
 
print("Test pos2()")
test_pos(pos2)
print('\n')
 
# VERSION 3 
def pos3(lst, e) : 
  nb = lst.count(e)
  j = 0
  Lres = [0]*nb 
  for i in range (0, len(lst)) : 
    if (lst[i] == e) : 
      Lres[j] = i # Lres.append(i)
      j += 1 # Incrémentation de J
  return Lres

print("Test pos3()")
test_pos(pos3)
print('\n')
 
# VERSION 4 
def pos4(lst, e) : 
  nb = lst.count(e) 
  Lres = [0]*nb 
  j = 0 
  for i in range (0, len(lst)) : 
    if (lst[i] == e) : 
      Lres[j] = i  
      j += 1 # Incrémentation de J !!
  return Lres

print("Test pos4()")
test_pos(pos4)
print('\n')