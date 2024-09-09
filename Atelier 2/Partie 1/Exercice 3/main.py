def separer(L:list)->list:
  indNeg = 0
  indPos = -1
  lsep = [0 for i in range(len(L))]
  for elt in L:
    if elt < 0:
      lsep[indNeg] = elt
      indNeg += 1
    elif elt > 0:
      lsep[indPos] = elt
      indPos -= 1
  return lsep

L = [0, -2, 1, 6, -4, -3, 2, 8, -2, 5, 6, 0, 0, 8, -38]
print(separer(L))
      