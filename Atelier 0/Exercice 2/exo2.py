import math

# retourne le prix(float) selon le poid et la lettre choisis par l'utilisateur
def getPrixTarification(lettre, poid:int):
  prix = 0
  listeTarif = list(lettre['tarificationPoidPrix'].keys()) # liste des poids disponibles pour la tarification
  indexTarif = 0
  # trouver le poids le plus proche sans dépasser le poids choisi
  while listeTarif[indexTarif] <= poid:
    indexTarif += 1
  indexTarif -= 1
  poidTarif = listeTarif[indexTarif]
  prix += lettre['tarificationPoidPrix'][poidTarif] # prix de base sans complément
  prix += (poid-poidTarif) * lettre['complement'] # prix final avec complément
  return prix

# dictionnaires des différents types de lettres avec leurs tarifications
Vert = {
  'nom': 'Lettre Vert',
  'maxPoid': 3000,
  'complement': 0.05,
  'tarificationPoidPrix':{ # poid/masse (g): prix (euro)
    20: 1.16,
    100: 2.32,
    250: 4.00,
    500: 6.00,
    1000: 7.50,
    3000: 10.50
  }
}

Prioritaire = {
  'nom': 'Lettre Prioritaire',
  'maxPoid': 3000,
  'complement': 0.05,
  'tarificationPoidPrix':{ # poid/masse (g): prix (euro)
    20: 1.43,
    100: 2.86,
    250: 5.26,
    500: 7.89,
    3000: 11.44
  }
}

Ecopli = {
  'nom': 'Ecopli',
  'maxPoid': math.inf,
  'complement': 0.02,
  'tarificationPoidPrix':{ # poid/masse (g): prix (euro)
    20: 1.14,
    100: 2.28,
    250: 3.92,
  }
}

# liste des types de lettres
typesLettres = [Vert, Prioritaire, Ecopli]

choixLetFait = False
lettreChoisie = None

# choix du type de lettre
while not choixLetFait:
  for elt in typesLettres:
    choixLettre = input('Votre lettre est une ' + elt['nom'] + ' ? O/N/Stop -> ')
    if choixLettre == 'O':
      choixLetFait = True
      lettreChoisie = elt 
      break
    elif choixLettre != 'N':
      choixLetFait = True
      break

# si une lettre a été choisie
if choixLettre == 'O':
  # choix du poid
  poidAutorise = False
  PoidChoisi = int(input('Quel est la masse (en g) de la lettre? -> '))
  if PoidChoisi <= elt['maxPoid']:
    poidAutorise = True

  # calcul du prix final
  prixFinal = getPrixTarification(lettreChoisie, PoidChoisi)
  print('Le prix final est de ', prixFinal, ' euros.')
  
  
# si aucun type de lettre n'a été choisi
else:
  print('Holla Problème sur le type de lettre')