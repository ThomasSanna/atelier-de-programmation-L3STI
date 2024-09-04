F=[6,5,6,8,4,2,1,5]

# Question 1
def histo(F:list)->list:
  valMax = max(F)
  H = [0 for i in range(valMax+1)]
  for elt in F:
    H[elt] += 1
  return H

print(histo(F))

def estInjective(F:list)->bool:
  H = histo(F)
  inj = True
  i = 0
  while inj and i<len(H):
    if H[i] > 1:
      inj = False
    i += 1
  return inj
    
print(estInjective(F))

def estSurjective(F:list)->bool:
  H = histo(F)
  surj = True
  i = 0
  while surj and i<len(H):
    if H[i] < 1:
      surj = False
    i += 1
  return surj

print(estSurjective(F))

def estBijective(F:list)->bool:
  return estInjective(F) and estSurjective(F)

