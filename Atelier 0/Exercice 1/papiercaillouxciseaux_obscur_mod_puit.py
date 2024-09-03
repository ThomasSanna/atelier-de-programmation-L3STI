import random

scoreJoueur1 = 0
scoreJoueur2 = 0
nombrePartie = 0

contreIA = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )

if contreIA == 'O':
    nomJoueur1 = input("Quel est votre nom ? ")
    print("Bienvenu ", nomJoueur1, " nous allons jouer ensemble \n")
    nomJoueur2 = 'Machine'
elif contreIA == 'N':
    nomJoueur1 = input("Quel est votre nom ? ")
    print("Bienvenu ", nomJoueur1, " nous allons jouer ensemble")
    nomJoueur2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu ", nomJoueur2, " nous allons jouer ensemble \n")
else:
    print("Je n'ai pas compris votre réponse")

jeuEnMarche = True
while jeuEnMarche:
    nombrePartie += 1 
    
    choixJ1OK = False
    while not choixJ1OK:
        choixJoueur1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ".format(nom=nomJoueur1))
        if choixJoueur1 in ('pierre', 'papier', 'ciseaux', 'puit'):
            choixJ1OK = True
        else:
            print('Faites un effort SVP')
    
    if contreIA == 0:
        choixJoueur2 = ['papier','pierre','ciseaux', 'puit'][random.randint(0, 3)]
    else :
        print("Au tour du joueur", nomJoueur2)
        
        choixJ2OK = False
        while not choixJ2OK:
            choixJoueur1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ".format(nom=nomJoueur1))
            if choixJoueur1 in ('pierre', 'papier', 'ciseaux', 'puit'):
                choixJ2OK = True
            else:
                print('Faites un effort SVP')
        
    #On affiche les choix de chacun
    print("Si on récapitule :",nomJoueur1, choixJoueur1, "et", nomJoueur2, choixJoueur2,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if choixJoueur1 == choixJoueur2 :
        resultatGagnant = "aucun de vous, vous êtes ex æquo"
        
    elif (choixJoueur1 == 'papier' and choixJoueur2 == 'pierre') or (choixJoueur1 == 'ciseaux' and choixJoueur2 == 'papier') or (choixJoueur1 == 'pierre' and choixJoueur2 == 'ciseaux'):
        resultatGagnant = nomJoueur1
        scoreJoueur1 += 1
        
    elif ((choixJoueur1 == 'puit' and choixJoueur2 in ('pierre', 'ciseaux')) or (choixJoueur1 == 'feuille' and choixJoueur2 == 'puit')):
        resultatGagnant = nomJoueur1
        scoreJoueur1 += 1

    else:
        resultatGagnant = nomJoueur2
        scoreJoueur2 += 1
        
    print("le gagnant est",resultatGagnant)
    print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    
    if nombrePartie >=5:
        jeuEnMarche = False
        
    if nombrePartie>=1 and nombrePartie<=4:
        #On propose au joueur de s'arreter
        rejouer = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nomJoueur1, nomJoueur2))
        if rejouer == 'O':
            jeuEnMarche = True
        elif rejouer == 'N':
            jeuEnMarche = False
        else:
            jeuEnMarche = True
            print("Vous ne répondez pas à la question, on continue")
  

# quand la boucle s'arrête        
print("Merci d'avoir joué ! A bientôt")