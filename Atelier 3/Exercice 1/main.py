def nomComplet(chaineEntree: str) -> str:
  parties = chaineEntree.split()
  if len(parties) != 2:
    raise ValueError("La chaîne d'entrée doit être au format 'nom prenom'")
  nom, prenom = parties
  return f"{nom.upper()} {prenom.capitalize()}"

def estMail(chaineEntree: str) -> (int, int):
  if '@' not in chaineEntree:
    return (0, 2)
  
  partieLocale, partieDomaine = chaineEntree.split('@', 1) # 1 pour ne pas spliter les '@' suivants
  
  if not partieLocale:
    return (0, 1)
  
  if '.' not in partieDomaine:
    return (0, 4)
  
  nomDomaine, extensionDomaine = partieDomaine.rsplit('.', 1) # 1 pour ne pas spliter les '.' suivants
  
  if not nomDomaine:
    return (0, 3)
  
  return (1, 0)

assert nomComplet('bisgambiglia paul') == 'BISGAMBIGLIA Paul'

assert estMail('bisgambiglia_paul@univ-corse.fr') == (1, 0)

assert estMail('bisgambiglia_paulOuniv-corse.fr') == (0, 2)

assert estMail('bisgambiglia_paul@univ-corsePOINTfr') == (0, 4)

assert estMail('@univ-corse.fr') == (0, 1)