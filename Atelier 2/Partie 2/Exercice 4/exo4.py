import matplotlib.pyplot as plt

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

# Question 2

def afficheHisto(F:list):
  H = histo(F)
  res = "HISTOGRAMME \n"
  maxOcc = max(H)
  for i in range(maxOcc):
    for elt in H:
      if elt >= maxOcc - i:
        res += " # "  
      else:
        res += "   "
    res += '\n'
  for i in range(len(H)):
    res += ' ' + str(i) + ' '
  print(res)
  
F = [0, 2, 3, 1, 8, 9, 4, 2, 3, 2]
print(histo(F))
afficheHisto(F)

def afficheHistoMatPlot(F:list):
  H = histo(F)
  plt.bar(range(len(H)), H)
  plt.xlabel('Valeurs')
  plt.ylabel('Occurrences')
  plt.title('Histogramme')
  plt.show()
  
afficheHistoMatPlot(F)