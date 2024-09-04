def separer(L:list)->list:
  indNeg = 0
  indPos = -1
  LSEP = [0 for i in range(len(L))]
  for elt in L:
    if elt < 0:
      LSEP[indNeg] = elt
      indNeg += 1
    elif elt > 0:
      LSEP[indPos] = elt
      indPos -= 1
  return LSEP

L = [0, -2, 1, 6, -4, -3, 2, 8, -2, 5, 6, 0, 0, 8, -38]
print(separer(L))
      