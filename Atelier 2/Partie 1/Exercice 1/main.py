def somme1(lst: list) -> int:
    """
    Calcule la somme des éléments d'une liste en utilisant une boucle for avec des indices.
    
    Paramètres:
        lst (list): Une liste d'entiers.
    
    Retourne:
        int: La somme des éléments de la liste.
    """
    res = 0
    for i in range(len(lst)):
        res += lst[i]
    return res

def somme2(lst: list) -> int:
    res = 0
    for elt in lst:
        res += elt
    return res

def somme3(lst: list) -> int:
    res = 0
    i = 0
    while i < len(lst):
        res += lst[i]
        i += 1
    return res

lst2test1 = [1, 10, 100, 1000, 10000]

def test_exercice1():
    """
    Teste les fonctions de somme avec une liste vide et une liste d'exemple.
    Affiche les résultats des tests.
    """
    assert somme1([]) == 0 and somme2([]) == 0 and somme3([]) == 0
    assert somme1(lst2test1) == 11111 and somme2(lst2test1) == 11111 and somme3(lst2test1) == 11111

test_exercice1()

def moyenne(lst: list) -> float:
    """
    Calcule la moyenne des éléments d'une liste.
    
    Paramètres:
        lst (list): Une liste d'entiers.
    
    Retourne:
        float: La moyenne des éléments de la liste, ou 0 si la liste est vide.
    """
    return somme1(lst) / len(lst) if len(lst) > 0 else 0

def nbSup(lst: list, e: int) -> int:
    """
    Compte le nombre d'éléments dans une liste qui sont supérieurs à un certain seuil.
    
    Paramètres:
        lst (list): Une liste d'entiers.
        e (int): Le seuil à comparer.
    
    Retourne:
        int: Le nombre d'éléments supérieurs à e, ou -1 si les deux méthodes de comptage ne concordent pas.
    """
    res1 = 0
    for i in range(len(lst)):
        res1 += 1 if lst[i] > e else 0
    
    res2 = 0
    for elt in lst:
        res2 += 1 if elt > e else 0
    
    return res1 if res1 == res2 else -1

def moySup(lst: list, e: int) -> float:
    """
    Calcule la moyenne des éléments d'une liste qui sont supérieurs à un certain seuil.
    
    Paramètres:
        lst (list): Une liste d'entiers.
        e (int): Le seuil à comparer.
    
    Retourne:
        float: La moyenne des éléments supérieurs à e.
    """
    listSup = [elt for elt in lst if elt > e]
    return moyenne(listSup)

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
        maxi = elt if maxi < elt else maxi
    return maxi

def indMax(lst: list) -> int:
    """
    Trouve L'indice de la valeur maximale dans une liste.
    
    Paramètres:
        lst (list): Une liste d'entiers.
    
    Retourne:
        int: L'indice de la valeur maximale dans la liste.
    """
    maxi = 0
    indMaxi = 0
    for i in range(len(lst)):
        if maxi < lst[i]:
            maxi = lst[i]
            indMaxi = i
    return indMaxi