import matplotlib.pyplot as plt

LST_FREQ = [6, 5, 6, 8, 4, 2, 1, 5]
LST_FREQ_2 = [2, 3, 1, 8, 9, 4, 2, 3, 2, 8, 9, 7, 4, 2, 1, 5, 6, 8, 9, 0, 8, 7, 6, 6, 3, 4, 4, 4, 2, 5, 10, 12, 13, 13, 11, 12]

# Fonction d'exercice 1
def valMax(lst: list) -> int:
    """
    Trouve la valeur maximale dans une liste.
    
    Args:
        lst (list): Une liste d'entiers.
    
    Returns:
        int: La valeur maximale dans la liste.
        
    Raises:
        ValueError: Si la liste lst est vide.
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
        
    Raises:
        ValueError: Si la liste lstFreq est vide.
    """
    try:
        valMaxValue = valMax(lstFreq) # Fonction à la ligne 7 : valMaxValue permet de donner la taille de la liste lstHisto ligne 51
    except:
        raise ValueError('La liste de comptage de fréquence est vide. Entrer une liste non-vide')
    
    lstHisto = [0 for i in range(valMaxValue + 1)]
    for elt in lstFreq:
        lstHisto[elt] += 1
    return lstHisto

assert histo([1, 2, 2, 3]) == [0, 1, 2, 1]
assert histo([0, 0, 0, 0]) == [4]
assert histo([1, 1, 1, 1]) == [0, 4]


def estInjective(lstHisto: list) -> bool:
    """
    Vérifie si une liste de comptage de fréquence injective (tous les éléments sont uniques).

    Args:
        lstFreq (list): Une liste de comptage de fréquence d'entiers.

    Returns:
        bool: True si la liste est injective, sinon False.
    """
    
    for elt in lstHisto:
        if elt > 1:
            return False
    return True

assert estInjective(histo([1, 2, 3, 4])) == True
assert estInjective(histo([1, 2, 2, 3])) == False
assert estInjective(histo([0, 1, 2, 3])) == True


def estSurjective(lstHisto: list) -> bool:
    """
    Vérifie si une liste de comptage de fréquence est surjective (chaque valeur possible apparaît au moins une fois).

    Args:
        lstFreq (list): Une liste de comptage de fréquence d'entiers.

    Returns:
        bool: True si la liste est surjective, sinon False.
    """
    
    for elt in lstHisto:
        if elt < 1:
            return False
    return True

assert estSurjective(histo([0, 1, 2, 3])) == True
assert estSurjective(histo([1, 2, 3, 4])) == False
assert estSurjective(histo([0, 0, 0, 0])) == True

def estBijective(lstHisto: list) -> bool:
    """
    Vérifie si une liste est bijective (injective et surjective).

    Args:
        lstFreq (list): Une liste d'entiers.

    Returns:
        bool: True si la liste est bijective, sinon False.
    """
    
    return estInjective(lstHisto) and estSurjective(lstHisto)

assert estBijective(histo([0, 1, 2, 3])) == True
assert estBijective(histo([1, 2, 3, 4])) == False
assert estBijective(histo([0, 0, 0, 0])) == False


def afficheHisto(lstHisto: list) -> None:
    """
    Affiche un histogramme basé sur une liste de comptage de fréquences.

    Args:
        lstFreq (list): Liste des fréquences à partir desquelles l'histogramme est généré.

    Returns:
        None, imprime le résultat à l'utilisation de la fonction
    """
    
    strResultat = "HISTOGRAMME \n"
    maxOcc = valMax(lstHisto) # Fonction à la ligne 7 : maxOcc permet de donner le nombre de ligne de l'histogramme imprimé

    # construction de l'histogramme ligne par ligne
    for ligne in range(maxOcc):
        for i, col in enumerate(lstHisto):
            if col >= maxOcc - ligne: # si la hauteur de la colonne est supérieure à la ligne actuelle
                strResultat += " " + "#"*len(str(i)) + " "  # imprime la hauteur de la colonne. Si index > 10: on affihe ## par ligne, ### pour index > 100 etc...
            else:
                strResultat += " " + " "*len(str(i)) + " "
        strResultat += '\n'

    for i in range(len(lstHisto)):
        strResultat += ' ' + str(i) + ' '

    print(strResultat)

afficheHisto(histo(LST_FREQ))
afficheHisto(histo(LST_FREQ_2))


def afficheHistoMatPlot(lstHisto: list) -> None:
    """
    Affiche un histogramme basé sur une liste de fréquences en utilisant Matplotlib.

    Args:
        lstFreq (list): Liste des fréquences à partir desquelles l'histogramme est généré.

    Returns:
        None, ouvre ue fenêtre MatPlotLib à l'utilisation de la fonction.
    """
    # Crée un histogramme en utilisant les valeurs de lstHisto
    # range(len(lstHisto)) génère les positions sur l'axe des x
    # lstHisto contient les hauteurs des barres sur l'axe des y
    plt.bar(range(len(lstHisto)), lstHisto)
    plt.xlabel('Valeurs')
    plt.ylabel('Occurrences')
    plt.title('Histogramme')
    plt.show()

afficheHistoMatPlot(histo(LST_FREQ))
afficheHistoMatPlot(histo(LST_FREQ_2))