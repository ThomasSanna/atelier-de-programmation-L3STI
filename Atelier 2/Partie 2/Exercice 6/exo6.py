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

test_present(present)