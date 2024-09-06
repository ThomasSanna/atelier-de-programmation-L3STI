lstMot=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
"finir", "aimer"]

def motsNLettres(lstMot:list, n:int)->list:
  lstRes = []
  for mot in lstMot:
    if len(mot) == n:
      lstRes.append(mot)
  return lstRes

def commencePar(mot:str, prefixe:str)->bool:
  longPrefixe = len(prefixe)
  return  mot[:longPrefixe] == prefixe # ou "prefixe in mot" mais bon
  # Ex: "Salut"[0] == "S", "Salut"[2] == 'l', "Salut"[:2] == "Sal"


assert commencePar('along', 'alo') == True

def finitPar(mot:str, suffixe:str)->bool:
  longSuffixe = len(suffixe)
  return mot[-longSuffixe:] == suffixe # ou "suffixe in mot" mais bon
  # Ex: "Salut"[-1] == "t", "Salut"[-2] == 'u', "Salut"[-2:] == "ut"

assert finitPar("along", "long") == True

def finissentPar(lstMot:list, suffixe:str)->list:
  return [mot for mot in lstMot if finitPar(mot, suffixe)]

assert finissentPar(lstMot, 'jour') == ['bonjour', 'jour', 'abajour']

def commencentPar(lstMot:list, prefixe:str)->list:
  return [mot for mot in lstMot if commencePar(mot, prefixe)]

def listeMots(lstMot:list, prefixe:str, suffixe:str, n:int)->str:
  return [mot for mot in lstMot if commencePar(mot, prefixe) and finitPar(mot, suffixe) and motsNLettres(lstMot, n)]

def dictionnaire(fichier:str)->list:
  lstRes = []
  f = open(fichier, 'r', encoding='utf-8')
  for line in f:
    lstRes.append(line[:-1]) # "[:-1]" enleve les "/n"
  return lstRes

assert dictionnaire('Atelier 3/Exercice 2/mots.txt') == ['bonjour', 'bonsoir', 'ça', 'va', 'moi', 'super', 'merci', 'je', 'vous', 'en', 'prie', 'non', 'pas', 'de', 'soucis']