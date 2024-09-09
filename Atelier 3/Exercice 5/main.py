def ouvrante(car):
    """Renvoie True si le caractère est une parenthèse, un crochet ou une accolade ouvrante."""
    return car in '({['

def fermante(car):
    """Renvoie True si le caractère est une parenthèse, un crochet ou une accolade fermante."""
    return car in ')}]'

def renverse(car):
    """Renvoie le caractère correspondant à la parenthèse, au crochet ou à l'accolade fermante."""
    correspondance = {')': '(', '}': '{', ']': '['}
    return correspondance.get(car, car)  # si 'car' n'est pas dans le dictionnaire, on renvoie car sans le modifier

def operateur(car):
    """Renvoie True si le caractère est un opérateur (+, * ou -)."""
    return car in '+*-'

def nombre(car):
    """Renvoie True si la chaîne de caractères ne comporte que des caractères numériques."""
    return car.isdigit()

def caractereValide(car):
    """Renvoie True si le caractère est valide dans une expression arithmétique."""
    return car in '(){}[]+-* ' or car.isdigit()

assert ouvrante('(') == True
assert ouvrante(')') == False
assert fermante(')') == True
assert fermante('(') == False
assert renverse(')') == '('
assert renverse('(') == '('
assert operateur('+') == True
assert operateur('/') == False
assert nombre('123') == True
assert nombre('abc') == False
assert caractereValide('1') == True
assert caractereValide('a') == False


def verif_parenthese(expression: str) -> bool:
    p = []
    correspondances = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if ouvrante(char):
            # empiler les parenthèses ouvrantes
            p.append(char)
        elif fermante(char):
            # vérifier si la pile est vide ou si le sommet de la pile ne correspond pas
            if p == [] or p[-1] != correspondances[char]:
                return False
            # dépiler le sommet de la pile
            p.pop()
        elif not caractereValide(char):
            return False
    
    # vérifier si la pile est vide
    return not p

print(verif_parenthese("(3+2) * 6-1"))  # True
print(verif_parenthese("((3+2)*6-1"))   # False
print(verif_parenthese("(5+7]*12"))     # False