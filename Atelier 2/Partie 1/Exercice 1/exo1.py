def somme1(L: list) -> int:
    """
    Calcule la somme des éléments d'une liste en utilisant une boucle for avec des indices.
    
    Paramètres:
        L (list): Une liste d'entiers.
    
    Retourne:
        int: La somme des éléments de la liste.
    """
    res = 0
    for i in range(len(L)):
        res += L[i]
    return res

def somme2(L: list) -> int:
    """
    Calcule la somme des éléments d'une liste en utilisant une boucle for directement sur les éléments.
    
    Paramètres:
        L (list): Une liste d'entiers.
    
    Retourne:
        int: La somme des éléments de la liste.
    """
    res = 0
    for elt in L:
        res += elt
    return res

def somme3(L: list) -> int:
    """
    Calcule la somme des éléments d'une liste en utilisant une boucle while.
    
    Paramètres:
        L (list): Une liste d'entiers.
    
    Retourne:
        int: La somme des éléments de la liste.
    """
    res = 0
    i = 0
    while i < len(L):
        res += L[i]
        i += 1
    return res

lst2test1 = [1, 10, 100, 1000, 10000]

def test_exercice1():
    """
    Teste les fonctions de somme avec une liste vide et une liste d'exemple.
    Affiche les résultats des tests.
    """
    print("TEST SOMME")
    # test liste vide
    print("Test liste vide : ", somme1([]), somme2([]), somme3([]))
    # test somme 11111
    print("Test somme 11111 : ", somme1(lst2test1), somme2(lst2test1), somme3(lst2test1))

test_exercice1()

def moyenne(L: list) -> float:
    """
    Calcule la moyenne des éléments d'une liste.
    
    Paramètres:
        L (list): Une liste d'entiers.
    
    Retourne:
        float: La moyenne des éléments de la liste, ou 0 si la liste est vide.
    """
    return somme1(L) / len(L) if len(L) > 0 else 0

def nbSup(L: list, e: int) -> int:
    """
    Compte le nombre d'éléments dans une liste qui sont supérieurs à un certain seuil.
    
    Paramètres:
        L (list): Une liste d'entiers.
        e (int): Le seuil à comparer.
    
    Retourne:
        int: Le nombre d'éléments supérieurs à e, ou -1 si les deux méthodes de comptage ne concordent pas.
    """
    res1 = 0
    for i in range(len(L)):
        res1 += 1 if L[i] > e else 0
    
    res2 = 0
    for elt in L:
        res2 += 1 if elt > e else 0
    
    return res1 if res1 == res2 else -1

def moySup(L: list, e: int) -> float:
    """
    Calcule la moyenne des éléments d'une liste qui sont supérieurs à un certain seuil.
    
    Paramètres:
        L (list): Une liste d'entiers.
        e (int): Le seuil à comparer.
    
    Retourne:
        float: La moyenne des éléments supérieurs à e.
    """
    listSup = [elt for elt in L if elt > e]
    return moyenne(listSup)

def valMax(L: list) -> int:
    """
    Trouve la valeur maximale dans une liste.
    
    Paramètres:
        L (list): Une liste d'entiers.
    
    Retourne:
        int: La valeur maximale dans la liste.
    """
    maxi = 0
    for elt in L:
        maxi = elt if maxi < elt else maxi
    return maxi

def indMax(L: list) -> int:
    """
    Trouve l'indice de la valeur maximale dans une liste.
    
    Paramètres:
        L (list): Une liste d'entiers.
    
    Retourne:
        int: L'indice de la valeur maximale dans la liste.
    """
    maxi = 0
    indMaxi = 0
    for i in range(len(L)):
        if maxi < L[i]:
            maxi = L[i]
            indMaxi = i
    return indMaxi