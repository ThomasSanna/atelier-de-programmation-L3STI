import matplotlib.pyplot as plt

lstFreq = [6,5,6,8,4,2,1,5]
lstFreq2 = [2, 3, 1, 8, 9, 4, 2, 3, 2, 8, 9, 7, 4, 2, 1, 5, 6, 8, 9, 0, 8, 7, 6, 6, 3, 4, 4, 4, 2, 5]

# Fonction d'exercice 1
def valMax(lst: list) -> int:
    """
    Trouve la valeur maximale dans une liste.
    
    Args:
        lst (list): Une liste d'entiers.
    
    Returns:
        int: La valeur maximale dans la liste.
    """
    if not lst:
        raise ValueError('La liste est vide!')
    maxi = 0
    for elt in lst:
        if maxi < elt:
            maxi = elt
    return maxi

assert valMax([1, 2, 3, 4, 5]) == 5
assert valMax([5, 4, 3, 2, 1]) == 5
assert valMax([0, 0, 0, 0]) == 0


def histo(lstFreq: list) -> list:
    """
    Donne l'histogramme de la liste de comptage de fréquence

    Args:
        lstFreq (list): Liste d'entier: comptage de fréquence

    Returns:
        list: Renvoie une liste d'entier: histogramme de lstFreq
    """
    valMaxValue = valMax(lstFreq)
    lstHisto = [0 for i in range(valMaxValue + 1)]
    for elt in lstFreq:
        lstHisto[elt] += 1
    return lstHisto

assert histo([1, 2, 2, 3]) == [0, 1, 2, 1]
assert histo([0, 0, 0, 0]) == [4]
assert histo([1, 1, 1, 1]) == [0, 4]


def estInjective(lstFreq: list) -> bool:
    """
    Vérifie si une liste est injective (tous les éléments sont uniques).

    Args:
        lst (list): Une liste d'entiers.

    Returns:
        bool: True si la liste est injective, sinon False.
    """
    lstHisto = histo(lstFreq)
    for elt in lstHisto:
        if elt > 1:
            return False
    return True

assert estInjective([1, 2, 3, 4]) == True
assert estInjective([1, 2, 2, 3]) == False
assert estInjective([0, 1, 2, 3]) == True


def estSurjective(lstFreq: list) -> bool:
    """
    Vérifie si une liste est surjective (chaque valeur possible apparaît au moins une fois).

    Args:
        lst (list): Une liste d'entiers.

    Returns:
        bool: True si la liste est surjective, sinon False.
    """
    lstHisto = histo(lstFreq)
    for elt in lstHisto:
        if elt < 1:
            return False
    return True

assert estSurjective([0, 1, 2, 3]) == True
assert estSurjective([1, 2, 3, 4]) == False
assert estSurjective([0, 0, 0, 0]) == True

def estBijective(lstFreq: list) -> bool:
    """
    Vérifie si une liste est bijective (injective et surjective).

    Args:
        lst (list): Une liste d'entiers.

    Returns:
        bool: True si la liste est bijective, sinon False.
    """
    return estInjective(lstFreq) and estSurjective(lstFreq)

assert estBijective([0, 1, 2, 3]) == True
assert estBijective([1, 2, 3, 4]) == False
assert estBijective([0, 0, 0, 0]) == False


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
                strResultat += " # "
            else:
                strResultat += "   "
        strResultat += '\n'

    for i in range(len(lstHisto)):
        strResultat += ' ' + str(i) + ' '

    print(strResultat)

afficheHisto(lstFreq2)


def afficheHistoMatPlot(lstFreq: list) -> None:
    """
    Affiche un histogramme basé sur une liste de fréquences en utilisant Matplotlib.

    Args:
        lstFreq (list): Liste des fréquences à partir desquelles l'histogramme est généré.

    Returns:
        None
    """
    lstHisto = histo(lstFreq2)
    # Crée un histogramme en utilisant les valeurs de lstHisto
    # range(len(lstHisto)) génère les positions sur l'axe des x
    # lstHisto contient les hauteurs des barres sur l'axe des y
    plt.bar(range(len(lstHisto)), lstHisto)
    plt.xlabel('Valeurs')
    plt.ylabel('Occurrences')
    plt.title('Histogramme')
    plt.show()

afficheHistoMatPlot(lstFreq)