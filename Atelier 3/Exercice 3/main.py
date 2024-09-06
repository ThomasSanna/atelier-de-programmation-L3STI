import random

def placesLettre(ch: str, mot: str) -> list:
    """
    Retourne les positions d'une lettre dans un mot.

    Args:
        ch (str): La lettre à chercher dans le mot.
        mot (str): Le mot dans lequel chercher la lettre.

    Returns:
        list: Une liste des positions de la lettre dans le mot.

    Raises:
        ValueError: Si l'entrée de la lettre n'est pas valide (longueur différente de 1).
    """
    indRes = []
    if len(ch) != 1:
        raise ValueError("Un problème est survenu lors de l'entrée de la lettre")
    for i, elt in enumerate(mot):
        if elt == ch:
            indRes.append(i)
    return indRes

assert placesLettre("m", 'maman') == [0, 2]

def outputStr(mot: str, lPos: list) -> str:
    """
    Retourne une chaîne de caractères avec des lettres trouvées et des tirets pour les lettres non trouvées.

    Args:
        mot (str): Le mot à afficher partiellement.
        lPos (list): La liste des positions des lettres trouvées.

    Returns:
        str: Une chaîne de caractères avec les lettres trouvées et des tirets pour les lettres non trouvées.
    """
    res = ''
    for i in range(len(mot)):
        if i in lPos:
            res += mot[i]
        else:
            res += '-'
    return res
  
def dictionnaire(fichier: str) -> list:
    """
    Lit un fichier et retourne une liste de mots.

    Args:
        fichier (str): Le chemin du fichier à lire.

    Returns:
        list: Une liste de mots contenus dans le fichier.
    """
    lstRes = []
    with open(fichier, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.lower()
            line = line.strip() # Utilisation de strip() pour enlever les espaces et les sauts de ligne
            if '-' not in line and ' ' not in line and "'" not in line:
              lstRes.append(line.strip()) 
    return lstRes
  

assert outputStr('bonjour', [0, 1, 4]) == 'bo--o--'

lstPendu = ["|---] ", 
            "| O ", 
            "| T ", 
            "|/ \ ", 
            "|______"]

def runGame():
    """
    Lance le jeu du pendu. Le joueur doit deviner un mot en entrant des lettres une par une.

    Le jeu continue jusqu'à ce que le joueur trouve toutes les lettres du mot ou fasse 5 erreurs.
    """
    lstMot = dictionnaire('Atelier 3/Exercice 3/noms-capitales.txt')
    indRandom = random.randint(0, len(lstMot) - 1)
    motATrouver = lstMot[indRandom]
    print('Chut, le mot est : ', motATrouver)
    nbErreur = 0
    lstIndTrouve = []

    while nbErreur < 5 and len(lstIndTrouve) != len(motATrouver):
        print("\nMot à trouver:")
        print(outputStr(motATrouver, lstIndTrouve))
        
        try:
            chr = str(input('\nEntrez une lettre (minuscule) -> '))
            chr = chr.lower()
        except:
            raise ValueError("\nUn problème est survenu lors de l'entrée de la lettre")
          
        lstIndRes = placesLettre(chr, motATrouver)
        if lstIndRes == []:
            print("\nErreur! La lettre " + chr + " n'est pas dans le mot cherché ! \n")
            nbErreur += 1
            for i in range(nbErreur):
                print(lstPendu[i])
        else:
            lstIndTrouve += lstIndRes

    if nbErreur == 5:
        print("\n Perdu !")
    else:
        print("Bravo ! Le mot était bien ", motATrouver, "!")

# runGame()

def getMaxStrLen(lst: list) -> int:
  maxLen = 0
  for e in lst:
    if len(e) > maxLen:
      maxLen = len(e)
  return maxLen
    

def build_dict(lst: list) -> dict:
  lstMot = dictionnaire('Atelier 3/Exercice 3/noms-capitales.txt')
  maxLen = getMaxStrLen(lstMot)
  print(maxLen)
  dictBuilded = {i:[] for i in range(maxLen)}

build_dict([])