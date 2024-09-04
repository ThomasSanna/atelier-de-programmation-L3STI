"""
Ce module fournit des fonctions pour résoudre des équations quadratiques de la forme ax^2 + bx + c = 0.

Fonctions:
- discriminant(a: float, b: float, c: float) -> float: 
    Calcule le discriminant de l'équation quadratique.
- racineUnique(a: float, b: float) -> float: 
    Calcule la racine unique de l'équation quadratique lorsque le discriminant est nul.
- racineDouble(a: float, b: float, delta: float, num: int) -> float: 
    Calcule les deux racines de l'équation quadratique lorsque le discriminant est positif.
- strEquation(a: float, b: float, c: float) -> str: 
    Retourne une représentation sous forme de chaîne de l'équation quadratique.
- solutionEquation(a: float, b: float, c: float) -> str: 
    Retourne les solutions de l'équation quadratique sous forme de chaîne.
- equation(a: float, b: float, c: float): 
    Affiche les solutions de l'équation quadratique.
- test(): 
    Teste les fonctions du module.
"""

import math

def discriminant(a:float, b:float, c:float)->float:
  return (b**2) - (4*a*c)

def racineUnique(a:float, b:float)->float:
  return -b/(2*a)

def racineDouble(a:float, b:float, delta:float, num:int):
  if num == 1:
    return (-b + math.sqrt(delta)) / (2*a)
  elif num == 2:
    return (-b - math.sqrt(delta)) / (2*a)
  else:
    raise ValueError('Problème lors de la saisie de num')
  
def strEquation(a:float, b:float, c:float)->str:
  return str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c)

def solutionEquation(a:float, b:float, c:float)->str:
  res = "Solution de l'équation " + strEquation(a, b, c) + '\n'
  delta = discriminant(a, b, c)
  if delta < 0:
    res += "Pas de racine réelle \n"
  elif delta == 0:
    res += "Racine unique: x=" + str(racineUnique(a, b)) + "\n"
  else:
    res += "Racine double: \n"
    for num in range(1, 3):
      res += "x" + str(num) + "=" + str(racineDouble(a, b, delta, num)) + '\n'
  return res

def equation(a:float, b:float, c:float):
  print(solutionEquation(a, b, c))
  
def test():
  # Test de l'équation avec deux racines réelles
  print(solutionEquation(1, -3, 2))
  # Test de l'équation avec une racine unique
  print(solutionEquation(1, 2, 1))
  # Test de l'équation sans racine réelle
  print(solutionEquation(1, 0, 1))

# Appel de la fonction de test
test()