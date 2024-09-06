import matplotlib.pyplot as plt

lstFreq=[6,5,6,8,4,2,1,5]

# Fonction d'exercice 1
def valMax(lst: list) -> int:
    """
    Trouve la valeur maximale dans une liste.
    
    Paramètres:
        lst (list): Une liste d'entiers.
    
    Retourne:
        int: La valeur maximale dans la liste.
    """
    maxi = 0
    for elt in lst:
      if maxi < elt:
        maxi = elt
    return maxi

# Question 1
def histo(lstFreq:list)->list:
  valeurMax = valMax(lstFreq)
  lstHisto = [0 for i in range(valeurMax+1)]
  for elt in lstFreq:
    lstHisto[elt] += 1
  return lstHisto

print(histo(lstFreq))

def estInjective(lstFreq:list)->bool:
  lstHisto = histo(lstFreq)
  for elt in lstHisto:
    if elt > 1:
      return False
  return True
    
print(estInjective(lstFreq))

def estSurjective(lstFreq:list)->bool:
  lstHisto = histo(lstFreq)
  for elt in lstHisto:
    if elt < 1:
      return False
  return True

print(estSurjective(lstFreq))

def estBijective(lstFreq:list)->bool:
  return estInjective(lstFreq) and estSurjective(lstFreq)

# Question 2

def afficheHisto(lstFreq: list) -> None:
    """
    Affiche un histogramme basé sur une liste de fréquences.

    Args:
        lstFreq (list): Liste des fréquences à partir desquelles l'histogramme est généré.

    Returns:
        None
    """
    lstHisto = histo(lstFreq)
    strResultat = "HISTOGRAMME \n"
    maxOcc = valMax(lstHisto)
    
    # construction de l'histogramme ligne par ligne
    for i in range(maxOcc):
        for elt in lstHisto:
            if elt >= maxOcc - i:
                strResultat += " # " if elt < 10 else "# "
            else:
                strResultat += "   " if elt < 10 else "  "
        strResultat += '\n'
    
    for i in range(len(lstHisto)):
        strResultat += ' ' + str(i) + ' '
    
    print(strResultat)
  
lstFreq = [2, 3, 1, 8, 9, 4, 2, 3, 2, 10, 11, 11, 8, 9, 7, 4, 2, 1, 5, 6, 8, 9, 0, 8, 7, 6, 6, 3, 4, 4, 4, 2, 5]
print(histo(lstFreq))
afficheHisto(lstFreq)

def afficheHistoMatPlot(lstFreq: list) -> None:
    """
    Affiche un histogramme basé sur une liste de fréquences en utilisant Matplotlib.

    Args:
        lstFreq (list): Liste des fréquences à partir desquelles l'histogramme est généré.

    Returns:
        None
    """
    lstHisto = histo(lstFreq)
    plt.bar(range(len(lstHisto)), lstHisto)
    plt.xlabel('Valeurs')
    plt.ylabel('Occurrences')
    plt.title('Histogramme')
    plt.show()

afficheHistoMatPlot(lstFreq)