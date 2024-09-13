#-------------------------------------------------------------------------------
# Name:        Statistiques des fichiers obtenus
# Purpose:
#
# Author:      Sebastien
#
# Created:     12/10/2022
# Copyright:   (c) Sebastien 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from sys import argv


########### INPUT ###########
rows = "dimension,seed,nbLLL,LLL,L4,time"
first = int(argv[1])
last = int(argv[2])
name = "L4-stats"


########### STATISTICS TOOLS ###########
moyenne = lambda tab : round(sum(tab)/len(tab), 4)
variance = lambda tab : sum([x*x for x in tab])/len(tab) - moyenne(tab)*moyenne(tab)
ecart_type = lambda tab : round(variance(tab)**0.5, 4)


######### DATAS EXTRACTION #########
for dim in range(first, last+1, 10):
    with open("L4-"+str(dim)+".csv", 'r') as file_in:
        datas = file_in.readlines()
    # results dictionnary
    list_keys = rows.split(',')
    dico = {k : [] for k in list_keys}
    for i in range(1, len(datas)):
        ligne = datas[i]
        try:
            ligne = [int(float(x)) if float(x) == round(float(x)) else float(x) for x in ligne[:-1].split(',')]
        except:
            print("Erreur : ligne ", i, ", fichier ", dim)
        for k in list_keys:
            dico[k].append(ligne[list_keys.index(k)])

    # creation du fichier
    if dim == first:
        with open(name+".csv", "w") as file:
            # entête
            file.write(list_keys[0]+",")
            for nom in list_keys[2:]:
                file.write(nom+"_average,")
                file.write(nom+"_std_deviation,")
                file.write(nom+"_min,")
                file.write(nom+"_max,")
            file.write(nom+"\n")
    with open(name+".csv", "a") as file:
        # remplissage
        file.write(str(dim)+",")
        for nom in list_keys[2:]:
            file.write(str(round(moyenne(dico[nom]),4))+",")
            file.write(str(round(ecart_type(dico[nom]),4))+",")
            file.write(str(round(min(dico[nom]),4))+",")
            file.write(str(round(max(dico[nom]),4))+",")
        file.write(nom+"\n")

    #file.write(str(round(min(LLL_gh),4))+",")
    #file.write(str(round(moyenne(LLL_gh),4))+",")
    #file.write(str(round(ecart_type(LLL_gh),4))+"\n")





