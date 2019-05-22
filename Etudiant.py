# -*- coding: utf-8 -*-

import csv
class Etudiant():
	"""docstring for Etudiant"""
	file = 'liste_etudiant.csv'

	def extraction(self,num,file_name):
		with open('liste_etudiant.csv','r') as file_reader :
			csv_reader = csv.DictReader(file_reader)
			fieldnames = ['nom','prenom','adresse','moyenne','age','region','specialite','sexe']
			
			if num==10:
				with open(file_name,'w') as file_writer :
					csv_writer = csv.DictWriter(file_writer,fieldnames=fieldnames,delimiter='|')
					csv_writer.writeheader()
					for line in csv_reader:
						if int(line['moyenne'])>=num :
							csv_writer.writerow(line )
							for i in range(len(fieldnames) ):
								print('%-8s : %s'%(fieldnames[i],line[fieldnames[i]]) )
								# csv_writer.writerow(fieldnames[i]+' :'+ line[fieldnames[i]] )  

								i+=1
							print('\n')
			elif num==20:
				with open(file_name,'w') as file_writer :
					csv_writer = csv.DictWriter(file_writer,fieldnames=fieldnames,delimiter='|')
					csv_writer.writeheader()
					for line in csv_reader:
						if int(line['age'])>num :
							csv_writer.writerow(line )
							for i in range(len(fieldnames) ):
								print('%-8s : %s'%(fieldnames[i],line[fieldnames[i]]) )
								# csv_writer.writerow('%-8s : %s'%(fieldnames[i],line[fieldnames[i]])  )

								i+=1
							print('\n')

	def statistique(self):
		
		with open('liste_etudiant.csv','r') as file_reader :
			csv_reader = csv.DictReader(file_reader)
			num=0
			Moyenne=0
			sexe_F=0
			sexe_M=0

			my_dico = {}
			num_etu = {}
			moyenne = {}
			row_num=0

			for line in csv_reader:
				Moyenne +=int(line['moyenne'])
				num+=1
				if line['sexe']=='femme':
					sexe_F+=1
				elif line['sexe']=='homme':
					sexe_M+=1

				if row_num==0:
						my_dico[line['region']] =int(line['moyenne'] )
						num_etu[line['region']] = 1
						row_num+=1

				elif line['region'] in my_dico.keys() :
					my_dico[line['region']] += int(line['moyenne'])
					num_etu[line['region']] += 1

				elif (line['region'] in my_dico.keys() ) == False :
					my_dico[line['region']] = int(line['moyenne'])
					num_etu[line['region']] = 1

			for region in my_dico.keys():
				moyenne[region] = my_dico[region]/num_etu[region]

			sorted_moy = sorted(moyenne.values())
			best_moy = sorted_moy[-1]
			best_region = {cle:valeur for cle,valeur in moyenne.items() if valeur==best_moy}
			print(best_region)

			with open('statistique.txt','w') as file_writer :
				file_writer.write('La Moyenne de l\'ecole est de :'+str(Moyenne/num)+'\n'  )
				file_writer.write('le Pourcentage de fille est de :'+str ((sexe_F*num)/100 )+'%'+'\n'  )
				file_writer.write( 'le Pourcentage de Garçon est de :'+str((sexe_M*num)/100) +'%'+'\n' )
				the_best = 'La region de {} a la meilleures moyenne qui est de  : {} ' 
				for cle,valeur in best_region.items():
					 the_best = the_best.format(cle,valeur)
				print(the_best)
				file_writer.write( the_best)

		print('La Moyenne de l\'ecole est de :',Moyenne/num)
		print('le Pourcentage de fille est de :',(sexe_F*num)/100 ,'%')
		print('le Pourcentage de Garçon est de :',(sexe_M*num)/100 ,'%')
			

