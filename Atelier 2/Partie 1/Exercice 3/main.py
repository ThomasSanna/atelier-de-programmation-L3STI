def separer(lstEntier:list)->list:
  indNegatif = 0
  indPositif = -1
  lsep = [0 for i in range(len(lstEntier))]
  for elt in lstEntier:
    if elt < 0:
      lsep[indNegatif] = elt
      indNegatif += 1
    elif elt > 0:
      lsep[indPositif] = elt
      indPositif -= 1
  # les 0 sont automatiquements mis au milieu du fait de L'initialiation de lsep à 0
  return lsep 

LST_ENTIER = [0, -2, 1, 6, -4, -3, 2, 8, -2, 5, 6, 0, 0, 8, -38]
print(separer(LST_ENTIER))
assert separer([]) == []
assert separer([1, 2, 3]) == [3, 2, 1]