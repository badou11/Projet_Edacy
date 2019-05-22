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
        
    if choix == 2:
        etu.extraction(20,'etudant_age.csv')
        
    if choix == 3:
        etu.statistique()
		



