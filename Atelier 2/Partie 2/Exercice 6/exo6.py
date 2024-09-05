# Question 1

def present(L:list, e:int)->bool:
  for elt in L:
    if elt == e:
      return True
  return False

def test_present(present: callable):
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