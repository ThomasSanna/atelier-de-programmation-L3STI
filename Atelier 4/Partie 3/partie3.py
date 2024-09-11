import numpy as np

def matriceAdjacence(s: list, a: list)-> np.ndarray:
  """
  Crée une matrice d'adjacence à partir des listes de sommets et d'arêtes.

  Args:
      s (list): La liste des sommets.
      a (list): La liste des arêtes (sommet1, sommet2).

  Returns:
      np.ndarray: La matrice d'adjacence.
  """
  mat = np.zeros((len(s), len(s)))
  for arc in a:
    try:
      mat[arc[0], arc[1]] = 1
    except IndexError:
      print(f"Erreur: l'arc {arc} n'est pas valide")
  return mat

def matriceAdjacencePond(s: list, a: list)-> np.ndarray:
  """
  Args:
      s (list): La liste des sommets.
      a (list): La liste des arêtes pondérées (sommet1, sommet2, poids)

  Returns:
      np.ndarray: La matrice d'adjacence pondérée.
  """
  mat = np.zeros((len(s), len(s)))
  for arc in a:
    try:
      mat[arc[0], arc[1]] = arc[2]
    except IndexError:
      print(f"Erreur: l'arc {arc} n'est pas valide")
  return mat

def lireMatriceFichier(nomFichier: str) -> np.ndarray:
    """
    Charge une matrice à partir d'un fichier texte.

    Args:
        nomFichier (str): Le chemin du fichier texte.

    Returns:
        np.ndarray: La matrice chargée.
        
    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
    """
    try:
      mat = np.loadtxt(nomFichier, dtype=int)
      return mat
    except:
      raise FileNotFoundError(f"Le fichier {nomFichier} est introuvable.")
    
def tousLesSommets(mat: np.ndarray) -> list:
  """
  Retourne une liste de tous les sommets d'un graphe représenté par une matrice d'adjacence.

  Args:
    mat (np.ndarray): La matrice d'adjacence représentant le graphe.

  Returns:
    list: Une liste contenant tous les sommets du graphe.
  """
  return list(range(len(mat)))

def listeArcs(mat: np.ndarray) -> list:
  """
  Retourne une liste de tous les arcs d'un graphe représenté par une matrice d'adjacence.

  Args:
    mat (np.ndarray): La matrice d'adjacence représentant le graphe.

  Returns:
    list: Une liste contenant tous les arcs du graphe.
  """ 
  arcs = [(i, j) for i in range(len(mat)) for j in range(len(mat)) if mat[i, j] != 0]
  return arcs

def matriceIncidence(mat: np.ndarray) -> np.ndarray:
  """
  Crée une matrice d'incidence à partir d'une matrice d'adjacence.

  Args:
    mat (np.ndarray): La matrice d'adjacence représentant le graphe.

  Returns:
    np.ndarray: La matrice d'incidence.
  """
  sommets = tousLesSommets(mat)
  
  # Filtrer les arcs pour éviter les doublons dans les arêtes non orientés
  arcs = []
  for a1, a2 in listeArcs(mat):
    if (a2, a1) not in arcs:
        arcs.append((a1, a2))
  
  matIncid = np.zeros((len(sommets), len(arcs)))

  for k, (i, j) in enumerate(arcs):
    if mat[i, j] == mat[j, i]:
      matIncid[i, k] = 1
      matIncid[j, k] = 1
    else:
      matIncid[i, k] = -1
      matIncid[j, k] = 1
  
  return matIncid

def estVoisin(mat: np.ndarray, sommet1: int, sommet2: int) -> bool:
  """
  Vérifie si deux sommets sont voisins dans un graphe représenté par une matrice d'adjacence.

  Args:
    mat (np.ndarray): La matrice d'adjacence représentant le graphe.
    sommet1 (int): Le premier sommet.
    sommet2 (int): Le deuxième sommet.

  Returns:
    bool: True si les sommets sont voisins, False sinon.
  """
  if sommet1 == sommet2:
    raise ValueError("Les sommets doivent être différents")
  return mat[sommet1, sommet2] != 0 or mat[sommet2, sommet1] != 0


def main():
  """
  Point d'entrée du programme
  """
  SOMMETS = [0, 1, 2, 3]
  ARCS = [(0, 1), (1, 2), (2, 3), (3, 0), (2, 0), (2, 1)]
  
  matAdj = matriceAdjacence(SOMMETS, ARCS)
  print("matriceAdjacence\n", matAdj)
  
  ARCS_PONDS = [(0, 1, 5), (1, 2, 3), (2, 3, 2), (3, 0, 1)]
  print('\nlmatriceAdjPond()\n', matriceAdjacencePond(SOMMETS, ARCS_PONDS))
  
  try:
    print('\nlireMatriceFicher()\n', lireMatriceFichier('Atelier 4\Partie 3\graph1.txt'))
  except FileNotFoundError as e:
    print('\n', e)
    
  print('\ntousLesSommets()\n', tousLesSommets(matAdj))

  print('\nlisteArcs()\n', listeArcs(matAdj))
   
  print('\nMatrice d\'incidence\n', matriceIncidence(matAdj))

  print('\nestVoisin()\n', estVoisin(matAdj, 0, 1))
  print(estVoisin(matAdj, 0, 3))
  print(estVoisin(matAdj, 1, 3))
  

if __name__ == "__main__":
  main()