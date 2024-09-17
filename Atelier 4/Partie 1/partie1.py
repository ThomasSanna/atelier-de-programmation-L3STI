# Question 1:

def sommeRecursive(lst: list[float]) -> float:
    """
    Calcule la somme des éléments d'une liste de manière récursive.
    
    Args:
        lst (list[float]): La liste des nombres flottants.
    
    Returns:
        float: La somme des éléments de la liste.
    
    Raises:
        ValueError: Si la liste est vide.
    """
    if not lst:
        raise ValueError('La liste est vide')
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sommeRecursive(lst[1:])

# Question 2:

def factorielleRecursive(n: int) -> int:
    """
    Calcule la factorielle d'un nombre de manière récursive.
    
    Args:
        n (int): Le nombre entier.
    
    Returns:
        int: La factorielle du nombre.
    
    Raises:
        ValueError: Si le nombre est négatif.
    """
    if n < 0:
        raise ValueError(f"Le nombre n={n} est négatif.")
    if n in (0, 1):
        return 1
    return n * factorielleRecursive(n - 1)

# Question 3:

def longueur(lst: list) -> int:
    """
    Calcule la longueur d'une liste de manière récursive.
    
    Args:
        lst (list): La liste dont on veut connaître la longueur.
    
    Returns:
        int: La longueur de la liste.
    """
    if not lst:
        return 0
    return 1 + longueur(lst[1:])

# Question 4:

def minimum(lst: list) -> int:
    """
    Trouve le minimum d'une liste de manière récursive.
    
    Args:
        lst (list): La liste des nombres.
    
    Returns:
        int: Le minimum de la liste.
    
    Raises:
        ValueError: Si la liste est vide.
    """
    if not lst:
        raise ValueError('La liste est vide, aucun minimum ne peut être défini.')
    if len(lst) == 1:
        return lst[0]
    
    minRest = minimum(lst[1:])
    if lst[0] < minRest:
        return lst[0]
    else:
        return minRest

# Question 5:

def listPairs(lst: list) -> list:
    """
    Retourne une liste contenant uniquement les éléments pairs de la liste d'origine.
    
    Args:
        lst (list): La liste des nombres.
    
    Returns:
        list: Une liste des nombres pairs.
    """
    if not lst:
        return []
    if lst[0] % 2 == 0:
        return [lst[0]] + listPairs(lst[1:])
    return listPairs(lst[1:])

# Question 6:

def concatList(lst: list) -> list:
    """
    Concatène les sous-listes d'une liste de manière récursive.
    
    Args:
        lst (list): La liste contenant des sous-listes.
    
    Returns:
        list: Une liste aplatie.
    """
    if not lst:
        return []
    if isinstance(lst[0], (list, tuple)):
        return concatList(lst[0]) + concatList(lst[1:])
    else:
        return [lst[0]] + concatList(lst[1:])

def concatListStr(lst: list) -> list[str]:
    """
    Concatène les sous-listes d'une liste de manière récursive.
    
    Args:
        lst (list): La liste contenant des sous-listes.
    
    Returns:
        list: Une liste aplatie.
    """
    if not lst:
        return []
    if isinstance(lst[0], (list, tuple)):
        return concatList(lst[0]) + concatList(lst[1:])
    else:
        return lst[0] + concatList(lst[1:])


# Question 7:

def incluse(lst1: list, lst2: list) -> bool:
    """
    Vérifie si tous les éléments de lst1 sont dans lst2 dans le même ordre.
    
    Args:
        lst1 (list): La première liste.
        lst2 (list): La deuxième liste.
    
    Returns:
        bool: True si lst1 est incluse dans lst2, sinon False.
    """
    if not lst1:
        return True
    if len(lst2) < len(lst1) or lst1[0] not in lst2:
        return False
    indEltLst2 = lst2.index(lst1[0]) # on fait ça car on sait que les éléments doivent être présent dans l'ordre
    return incluse(lst1[1:], lst2[(indEltLst2 + 1):]) # donc lst2 est coupé après l'élément traité (lst1[0])

def main():
    """
    Point d'entrée du programme.
    """
    # tests sommeRecursive()
    assert sommeRecursive([1.0, 2.0, 3.0, 4.0, 5.0]) == sum([1.0, 2.0, 3.0, 4.0, 5.0])
    try:
        sommeRecursive([])  # renvoie une erreur
    except ValueError as e:
        print(f"Problème (attendu) à l'exécution de la fonction sommeRecursive : {e}")

    # tests factorielleRecursive()
    assert factorielleRecursive(5) == 120
    assert factorielleRecursive(0) == 1
    try:
        factorielleRecursive(-16)  # renvoie une erreur
    except ValueError as e:
        print(f"Problème (attendu) à l'exécution de la fonction factorielleRecursive : {e}")

    # tests longueur()
    assert longueur([]) == 0
    assert longueur([1, 2, 0, 2]) == 4

    # tests minimum()
    assert minimum([3, 2, 6, 4, 1, 6]) == 1
    assert minimum([184]) == 184

    # tests listPairs()
    assert listPairs([0, 2, 1, 3, 2, 5, 6]) == [0, 2, 2, 6]
    assert listPairs([0, 2, 1, 5, 2, 5, 6, 5, 5, 5, 4, 5, 5, 7]) == [0, 2, 2, 6, 4]
    assert listPairs([]) == []

    # tests concatList()
    assert concatList([[0, 1], [2, 3], [4], [6, 7]]) == [0, 1, 2, 3, 4, 6, 7]
    assert concatList([]) == []
    assert concatList([[0, 1, [1, 2, 3, 4]], [2, [1, 2, [10, 23, 11, [1, 12], 2], 2, 3], 3], [4], [6, 7]]) == [0, 1, 1, 2, 3, 4, 2, 1, 2, 10, 23, 11, 1, 12, 2, 2, 3, 3, 4, 6, 7]

    # tests incluse()
    assert incluse([1, 2, 3], [1, 2, 3, 4, 5, 6]) == True
    assert incluse([1, 2, 3], [1, 2, 4, 5, 6]) == False
    assert incluse([1, 2, 3], [1, 2, 3]) == True
    assert incluse([1, 2, 3], [1, 2, 3, 4, 5, 6, 1, 2, 3]) == True
    assert incluse([1, 2, 3], []) == False
    assert incluse([], [1, 2, 3]) == True

if __name__ == '__main__':
    main()