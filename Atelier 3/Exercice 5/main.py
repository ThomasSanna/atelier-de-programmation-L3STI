def ouvrante(car: str) -> bool:
    """
    Vérifie si le caractère est une parenthèse, une accolade ou un crochet ouvrant.

    Args:
        car (str): Le caractère à vérifier. Doit être une chaîne non vide.

    Returns:
        bool: True si le caractère est '(', '{', ou '[', sinon False.

    Raises:
        ValueError: Si le caractère est une chaîne vide.
    """
    if not car:
        raise ValueError("Le caractère d'entrée doit être une chaîne non vide.")
    return car in "({["


def fermante(car: str) -> bool:
    """
    Vérifie si le caractère est une parenthèse, une accolade ou un crochet fermant.

    Args:
        car (str): Le caractère à vérifier. Doit être une chaîne non vide.

    Returns:
        bool: True si le caractère est ')', '}', ou ']', sinon False.

    Raises:
        ValueError: Si le caractère est une chaîne vide.
    """
    if not car:
        raise ValueError("Le caractère d'entrée doit être une chaîne non vide.")
    return car in ")}]"


def renverse(car: str) -> str:
    """
    Obtenir le caractère ouvrant correspondant pour une parenthèse, une accolade ou un crochet fermant.

    Args:
        car (str): Le caractère fermant. Doit être une chaîne non vide.

    Returns:
        str: Le caractère ouvrant correspondant, ou le caractère lui-même s'il n'est pas trouvé.

    Raises:
        ValueError: Si le caractère est une chaîne vide.
    """
    if not car:
        raise ValueError("Le caractère d'entrée doit être une chaîne non vide.")
    correspondance = {")": "(", "}": "{", "]": "["}
    return correspondance.get(car, car)


def operateur(car: str) -> bool:
    """
    Vérifie si le caractère est un opérateur arithmétique (+, *, ou -).

    Args:
        car (str): Le caractère à vérifier. Doit être une chaîne non vide.

    Returns:
        bool: True si le caractère est '+', '*', ou '-', sinon False.

    Raises:
        ValueError: Si le caractère est une chaîne vide.
    """
    if not car:
        raise ValueError("Le caractère d'entrée doit être une chaîne non vide.")
    return car in "+*-"


def nombre(car: str) -> bool:
    """
    Vérifie si la chaîne est composée uniquement de caractères numériques.

    Args:
        car (str): La chaîne à vérifier. Doit être une chaîne non vide.

    Returns:
        bool: True si la chaîne est numérique, sinon False.

    Raises:
        ValueError: Si la chaîne est vide.
    """
    if not car:
        raise ValueError("La chaîne d'entrée doit être non vide.")
    return car.isdigit()


def caractere_valide(car: str) -> bool:
    """
    Vérifie si le caractère est valide dans une expression arithmétique.

    Args:
        car (str): Le caractère à vérifier. Doit être une chaîne non vide.

    Returns:
        bool: True si le caractère est un chiffre, un opérateur, une parenthèse, une accolade, un crochet ou un espace, sinon False.

    Raises:
        ValueError: Si le caractère est une chaîne vide.
    """
    if not car:
        raise ValueError("Le caractère d'entrée doit être une chaîne non vide.")
    return car in "(){}[]+-* " or car.isdigit()


def verif_parenthese(expression: str) -> bool:
    """
    Vérifie si les parenthèses, accolades et crochets dans l'expression sont équilibrés.

    Args:
        expression (str): L'expression arithmétique à vérifier.

    Returns:
        bool: True si l'expression est équilibrée, sinon False.
    """
    if not expression:
        return True
    
    pile = []
    correspondances = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if ouvrante(char):
            pile.append(char)
        elif fermante(char):
            if not pile or pile[-1] != correspondances[char]:
                return False
            pile.pop()
        elif not caractere_valide(char):
            return False

    return not pile


# Tests
assert ouvrante("(") == True
assert ouvrante("{") == True
assert ouvrante("[") == True
assert ouvrante(")") == False
assert ouvrante("a") == False

assert fermante(")") == True
assert fermante("}") == True
assert fermante("]") == True
assert fermante("(") == False
assert fermante("a") == False

assert renverse(")") == "("
assert renverse("}") == "{"
assert renverse("]") == "["
assert renverse("(") == "("
assert renverse("a") == "a"

assert operateur("+") == True
assert operateur("*") == True
assert operateur("-") == True
assert operateur("/") == False
assert operateur("a") == False

assert nombre("123") == True
assert nombre("0") == True
assert nombre("a") == False
assert nombre("1a") == False

assert caractere_valide("1") == True
assert caractere_valide("+") == True
assert caractere_valide("(") == True
assert caractere_valide(" ") == True
assert caractere_valide("a") == False

assert verif_parenthese("()") == True
assert verif_parenthese("({[]})") == True
assert verif_parenthese("({[})") == False
assert verif_parenthese("({[a]})") == False
assert verif_parenthese("") == True
