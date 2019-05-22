# -*- coding: utf-8 -*-

from Etudiant import Etudiant

etu = Etudiant()
choix = 0

while choix != 4:
    print('---------------------------------------------')
    print('|                                           |')
    print('|             		MENU                   |')
    print('|                                           |')
    print('|      1-Les etudiants ayants la moyenne    |')
    print('|                                           |')
    print('|      2-Les etudiants de plus de 20 Ans    |')
    print('|                                           |')
    print('|      3-Statistique Global                 |')
    print('|                                           |')
    print('|      4-Quitter                            |')
    print('|                                           |')
    print('|                                           |')
    print('---------------------------------------------') 	
    
    choix = int(input("faite votre choix : "))
    if choix == 1:
        etu.extraction(10,'etudant_avec_la_moyenne.csv')
        print('Le fichier Etudiant_avec_la_moyenne.csv a ete extrait avec succes \n ')
        
    if choix == 2:
        etu.extraction(20,'etudant_age.csv')
        print('Le fichier Etudiant_age.csv a ete extrait avec succes \n ')

        
    if choix == 3:
        etu.statistique()
        print('Le fichier statistique.csv a ete extrait avec succes \n ')
    


print('\nMerci de votre visite !')
print('Bye \n')


		



