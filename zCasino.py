import os
from random import randrange 
from math import ceil
#zCasino 
# Code du Jeu de Roulette adaptee
#le joueur choisit un nom
def nom_utilisateur() :
        nom_utilisateur = input ("taper votre nom:")
        #on met la 1ere lettre du nom en majuscules
        nom_utilisateur = nom_utilisateur.capitalize ()
# declation du montant du joueur au depart
argent = 2000 #Le jouer a 2000 $
continuer_la_partie = True
print("Bienvenue a la table de roulette, vous avez" , argent , "$")
while continuer_la_partie : # Tant que le joueur veut continuer la partie
#on va lui demandere le nombre sur lequel il veut miser 
        nombre_mise = -1 
        while nombre_mise < 0 or nombre_mise > 49: # tant que le joueur veut miser,
        #le nombre doit etre compris entre 0 a 49
                nombre_mise = input("Taper un nombre compris entre 0 a 49 sur lequel vous allez miser : ")
                #Le nombre mise doit etre un nombre entier 
                try:
                        nombre_mise = int(nombre_mise)
                except ValueError: #Si vous n'avez pas saisi un nombre 
                        print ( "Vous n'avez pas saisi un nombre.")
                if nombre_mise < 0 : # Si le nombre mise est inferieur a 0
                        print( "Le nombre mise est negatif.")
                elif nombre_mise > 49 : #et si il est superieur a 49
                        print("Ce nombre est superieur a 49.")  
#Apres avoir mise, on choisi le nombre d'argent a miser 
        mise = 0
        while mise <= 0 or mise > argent : 
                mise = input ("Taper le montant que vous allez miser:")
                try :
                        mise = int(mise) #Le montant doit etre un nombre entier
                except ValueError: #Vous n'avez pas taper un nombre 
                        print("Veuillez taper un nombre:")
                        mise = -1
                        continue
                if mise <= 0: 
                        print("La mise saisi est trop faible ou egale a 0.")
                elif mise > argent : #si le montant est superieur a votre argent
                        print ("Vous ne pouvez pas miser ce montant, votre argent est de:", argent,"$" )
#Maintenant que le nombre mise et le montant de la mise selectionne
#on vas faire tourner la roulette
        numero_gagnant = randrange (50)
        print ("La roulette tourne .....tourne......tourne et s'arrete" , numero_gagnant)
#le gain du joueur
        if numero_gagnant == mise:
                print ("FELICITATIONS!!!! vous avez gagne" ,mise * 3, "$")
                argent += mise * 3 
        elif numero_gagnant % 2 == nombre_mise % 2 : #ils sont de la meme couleur
                mise = ceil(mise * 0,5)
                print("Vous avez miser sur la bonne couleur. vous obtenez: " , argent, "$")
                argent += mise
        else: #sinon
                print("Vous avez perdu la mise..")
                argent-=mise
#si vous etes ruine, fin de la partie 
        if numero_gagnant <=0 : #si le numero gagnant est infeieur ou egale a 0
                print ("Vous etes ruine!!!!! FIN DE LA PARTIE ")
                continuer_la_partie = False
        else : #sinon, on affiche le gain du joueur
                print("Vous avez maintenant:" , argent , "$")
                quiter = input ("Voulez vous quitter la partie? si oui taper :o")
                if quitter == o or quitter == O :
                        print("vous nous quitter avec vos gains.")
                        continuer_la_partie = False

os.system("Pause")

                

                
                        
                
                
                
        
                
        

