import numpy as np

# Question 1

def mySearchsorted(table: np.ndarray, element: int) -> int:
  """
  Custom implementation of numpy's searchsorted function.
  """
  for i in range(len(table)):
    if table[i] >= element:
      return i
  return len(table)
  
# Question 2

def myWhere(table: np.ndarray, valeur: int) -> list:
  """
  Custom implementation of numpy's where function.
  """
  result = []
  for t, e in np.ndenumerate(table):
    if e == valeur:
      result.append(t)
  return result

# Question 3.1

def myAddV1(tableA: np.ndarray, tableB: np.ndarray) -> np.ndarray:
  """
  Custom implementation of matrix addition using ndenumerate.
  """
  if tableA.shape != tableB.shape:
    raise ValueError("Les dimensions des matrices ne correspondent pas")
  result = np.zeros(tableA.shape, dtype=int)
  for t, _ in np.ndenumerate(tableA):
    result[t] = tableA[t] + tableB[t]
  return result

# Question 3.2

def myAddV2(tableA: np.ndarray, tableB: np.ndarray) -> np.ndarray:
  """
  Custom implementation of matrix addition using nested loops.
  """
  if tableA.shape != tableB.shape:
    raise ValueError("Les dimensions des matrices ne correspondent pas")
  result = np.zeros(tableA.shape, dtype=int)
  for i in range(tableA.shape[0]):
    for j in range(tableA.shape[1]):
      result[i, j] = tableA[i, j] + tableB[i, j]
  return result

def main():
  """
  Débute l'exécution du script.
  """
  arr = np.array([1, 2, 3, 4, 5, 6, 14])
  assert mySearchsorted(arr, 8) == 6
  assert mySearchsorted(arr, 4) == 3

  arr = np.array([[1, 2, 3], [4, 5, 4], [4, 7, 8]])
  assert myWhere(arr, 4) == [(1, 0), (1, 2), (2, 0)]

  a = np.array(([3, 1], [6, 4]))
  b = np.array(([1, 8], [4, 2]))

  assert np.array_equal(myAddV1(a, b), np.array(([4, 9], [10, 6])))
  assert np.array_equal(myAddV2(a, b), np.array(([4, 9], [10, 6])))


  # Autres exercices autour des matrices
  m = np.arange(1, 10).reshape(3, 3)
  print(f'm = {m}\n')

  mPlus10 = m + 10
  print(f'mPlus10 = {mPlus10}\n')

  mFois2 = m * 2
  print(f'mTimes2 = {mFois2}\n')

  print(f'deuxième ligne = {m[1, :]}\n')
  print(f'troisième colonne = {m[:, 2]}\n')
  print(f'sous-matrice 2x2 du coin supérieur gauche = {m[:2, :2]}\n')

if __name__ == "__main__":
    main()