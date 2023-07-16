'''
Created on Jun 2020
@Authors : Marieke Bonnaffé-Moity and Marie-Anne Dejoan - French Guyana

Etude de la réaction d'oxydation des ions péroxodisulfate par les ions iodure en présence d'un catalyseur (ions fer II)

Représentation de l'évolution temporelle de la concentration en ions péroxodilsulfate dans le milieur réactionnel
et mise en évidence de l'ordre 1 de la réaction étudiée

Les valeurs mesurées de l'absorbance et du temps sont extraites d'un fichier .txt
'''

#Importation des bibliothèques
from scipy.optimize import curve_fit
from pylab import *   #Importer la bibliothèque pylab qui permet d’utiliser de manière aisée les bibliothèques NumPy et matplotlib
import csv

#Importation des données (colonne 1 absorbance ; colonne 2 temps)
data = np.loadtxt("donnees.txt")
table = data[:,:]

#Initialisation des listes vides
Temps=[]
Absorbance=[]
Concentration=[]   #Concentration en ion peroxodisulfate en mol/L
C_mmol=[]          #Concentration en ion peroxodisulfate en mmol/L

Co = float(4.0E-3) #Concentration initiale en ion peroxodisulfate en mol/L
l = 1              #Largeur de la cuve en cm

#Construction des listes
for row in table:
    Absorbance.append(float(row[0]))
    Temps.append(float(row[1]))

epsilon = float(Absorbance[-1]/Co) #Coefficient d'exctinction molaire du diiode pour la longeur d'onde de travail en L.mol-1.cm-1 -

for i in range(len(Absorbance)):
    C=Co-Absorbance[i]/(epsilon*l)
    Concentration.append(C)
    C_mmol.append((10E2)*C)

#Modélisation de l'évolution de la concentration en ion peroxodisulfate au cours du temps
def exponentielle_decroissant(t,a,b,c):
    return a*exp(-t*b)

params1,covar1 = curve_fit(exponentielle_decroissant,Temps,Concentration)

C_modele = []
for val in Temps:
    C_modele.append(exponentielle_decroissant(val,*params1))


#Vitesse de réaction et modélisation
dt = Temps[2]-Temps[1]
v_mmol = -gradient(C_mmol,dt)       #v_mmol : vitesse de la réaction exprimée en mmol.L^(-1).s^(-1)

def lineaire(x,k):
    return k*x

params2, covar2 = curve_fit(lineaire,C_mmol,v_mmol)

coef = params2[0]                   #Coefficient directeur de la droite modélisée

fenetre1 = plt.figure('Fenetre 1')
#Tracé de la concentration en ions péroxodisulfate en fonction du temps
graph1 = fenetre1.add_subplot(121)
graph1.plot(Temps,Concentration,'b+',label="Acquisition")
#Tracé du résultat de la modélisation
graph1.plot(Temps,C_modele,'r-',label="Modélisation")
xlabel(r'$Temps \ en \ s$', fontsize = 22)
ylabel(r'$C_{peroxodisulfate} \ en \ mol.L^{-1}$', fontsize = 22)
tick_params(axis = 'both', labelsize = 15)
axis([0,600,0,0.003])
title (r'$C_{peroxodisulfate} = f(t)$', fontsize = 24)
plt.text(35,0.001,"Equation du modèle : C ="+str(round(params1[0],4))+r'$\times exp(-$'+str(round((params1[1]),4))+r'$t)$',bbox=dict(facecolor='red', alpha=0.5), fontsize = 18)
graph1.legend(fontsize = 18)
graph1.grid

#Tracé de la vitesse de la réaction en fonction de la concentration en ion peroxodisulafte
graph2 = fenetre1.add_subplot(122)
graph2.plot(C_mmol,v_mmol,'b+',label="Acquisition")
#Tracé du résultat de la modélisation
X = array([min(C_mmol),max(C_mmol)])     #Pour tracer une droite, 2 points sont suffisants
graph2.plot(X,coef*X,'r-',label="Modélisation")
xlabel(r'$C_{peroxodisulfate} \ en \ mmol.L^{-1}$', fontsize = 22)
ylabel(r'$Vitesse \ de \ la \ réaction \ en \ mmol.L^{-1}.s^{-1}$', fontsize = 22)
tick_params(axis = 'both', labelsize = 15)
axis([0,3,0,0.02])
title (r'$v = f(C)$', fontsize = 24)
plt.text(0.3,0.0015,r'$Equation \ du \ modèle \ : \ v_{mmol} \ =$'+str(round(coef,3))+r'$\times C_{mmol}$',bbox=dict(facecolor='blue', alpha=0.5), fontsize = 18)
graph2.legend(fontsize = 18)
graph2.grid

show()





