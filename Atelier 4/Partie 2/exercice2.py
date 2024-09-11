import numpy as np

def matriceTrace(matrice: np.ndarray) -> int:
  """
  Calcule la trace d'une matrice.
  
  args:
    matrice: np.ndarray - La matrice à traiter.
  
  return:
    int - La trace de la matrice.
  """
  if matrice.shape[0] != matrice.shape[1]:
    raise ValueError("La matrice n'est pas carrée")
  return np.sum(np.diag(matrice))

def estSymetrique(matrice: np.ndarray) -> bool:
  """
  Détermine si une matrice est symétrique.
  
  args:
    matrice: np.ndarray - La matrice à traiter.
  
  return:
    bool - True si la matrice est symétrique, False sinon.
  """
  return np.array_equal(matrice, matrice.T) # Compare la matrice avec sa transposée

def produitDiagonale(matrice: np.ndarray) -> int:
  """
  Calcule le produit des éléments de la diagonale d'une matrice.
  
  args:
    matrice: np.ndarray - La matrice à traiter.
  
  return:
    int - Le produit des éléments de la diagonale.
  """
  if matrice.shape[0] != matrice.shape[1]:
    raise ValueError("La matrice n'est pas carrée")
  return np.prod(np.diag(matrice))


  

def main():
  """
  Débute l'exécution du script.
  """
  A = np.random.randint(0, 10, (4, 4))
  I = np.eye(4)
  
  assert matriceTrace(A) == np.trace(A)
  
  assert not estSymetrique(A)
  assert estSymetrique((A + A.T)/2)
  assert estSymetrique(I)
  
  assert produitDiagonale(A) == np.prod(np.diag(A))
  assert produitDiagonale(I) == 1

if __name__ == "__main__":
    main()