listeTest1 = [0, 2, 3, 1, 8, 9] # Sans répétition
listeTest2 = [0, 2, 3, 1, 8, 9, 4, 2, 3, 2] # Avec répétition
listeTriee = [0, 3, 4, 7, 8, 10, 13, 14, 17, 19, 20, 22, 25, 27, 30, 32, 33, 34, 37, 38, 39, 41, 43]

def position(lst: list, e: int) -> int:
    """
    Retourne L'index de la première occurrence de L'élément `e` dans la liste `lst`.
    Si L'élément n'est pas trouvé, retourne -1.

    Paramètres:
    lst (list): La liste dans laquelle chercher.
    e (int): L'élément à trouver.

    Retourne:
    int: L'index de la première occurrence de `e`, ou -1 si non trouvé.
    """
    for i in range(len(lst)):
        if lst[i] == e:
            return i
    return -1

def position2(lst: list, e: int) -> int:
    """
    Retourne L'index de la première occurrence de L'élément `e` dans la liste `lst` en utilisant une boucle while.
    Si L'élément n'est pas trouvé, retourne -1.

    Paramètres:
    lst (list): La liste dans laquelle chercher.
    e (int): L'élément à trouver.

    Retourne:
    int: L'index de la première occurrence de `e`, ou -1 si non trouvé.
    """
    i = 0
    while i < len(lst):
        if lst[i] == e:
            return i
        i += 1
    return -1

def nbOccurrences(lst: list, e: int) -> int:
    """
    Retourne le nombre d'occurrences de L'élément `e` dans la liste `lst`.

    Paramètres:
    lst (list): La liste dans laquelle chercher.
    e (int): L'élément à compter.

    Retourne:
    int: Le nombre d'occurrences de `e` dans `lst`.
    """
    occ = 0
    for elt in lst:
        occ += 1 if e == elt else 0
    return occ

def estTriee(lst: list) -> bool:
    """
    Vérifie si la liste `lst` est triée par ordre croissant en utilisant une boucle while.

    Paramètres:
    lst (list): La liste à vérifier.

    Retourne:
    bool: True si la liste est triée, False sinon.
    """
    triee = True
    i = 0
    while triee and i < len(lst) - 1:
        if lst[i] > lst[i + 1]:
            triee = False
        i += 1
    return triee

def estTriee2(lst: list) -> bool:
    """
    Vérifie si la liste `lst` est triée par ordre croissant en utilisant une boucle for.

    Paramètres:
    lst (list): La liste à vérifier.

    Retourne:
    bool: True si la liste est triée, False sinon.
    """
    triee = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            triee = False
    return triee

def positionTri(lst: list, e: int) -> int:
    """
    Retourne L'index de L'élément `e` dans la version triée de la liste `lst` en utilisant la recherche binaire.
    Si L'élément n'est pas trouvé, retourne -1.

    Paramètres:
    lst (list): La liste dans laquelle chercher.
    e (int): L'élément à trouver.

    Retourne:
    int: L'index de `e` dans la liste triée, ou -1 si non trouvé.
    """
    lstTrie = sorted(lst)
    low = 0
    hight = len(lstTrie) - 1
    while low <= hight:
        mid = low + (hight - low) // 2
        if e < lstTrie[mid]:
            hight = mid - 1
        elif e > lstTrie[mid]:
            low = mid + 1
        else:
            return mid
    return -1

def aRepetitions(lst: list) -> bool:
    """
    Vérifie si la liste `lst` contient des éléments répétés.

    Paramètres:
    lst (list): La liste à vérifier.

    Retourne:
    bool: True s'il y a des éléments répétés, False sinon.
    """
    T = []
    aRepet = False
    i = 0
    while not aRepet and i < len(lst):
        if lst[i] in T:
            aRepet = True
        else:
            T.append(lst[i])
        i += 1
    return aRepet

print(estTriee(listeTest1)) # False
print(estTriee2(listeTriee)) # True

print(positionTri(listeTriee, 38)) # 19
print(positionTri(listeTriee, 10)) # 5
print(positionTri(listeTriee, 0)) # 0
print(positionTri(listeTriee, 12)) # -1