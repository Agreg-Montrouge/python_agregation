# -*- coding: utf-8 -*-
"""
Titrage d’une solution aqueuse d’acide éthanoïque
par une solution aqueuse d’hydroxyde de sodium

Auteur : directement inspiré de David Therincourt (Lycée Roland Garros - Académie de la Réunion)
Téléchargé sur le site https://physique-chimie-python.readthedocs.io/fr/latest/
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def derivee(x, y):
    y_prim = []
    for i in range (len(x)-1):
        k = (y[i+1]-y[i])/(x[i+1]-x[i])
        y_prim.append(k)
    return x[:-1], y_prim

plt.rcParams["figure.figsize"] = (8,10) # width, height in inches (100 dpi)
plt.subplots_adjust(hspace=0.15, left=0.10, bottom=0.06, right=0.95, top=0.94 ) # Position en %
# Mesures
Vb = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,12.2,12.4,12.6,12.8,13,13.2,13.4,13.6,13.8,14,14.2,14.4,14.6,14.8,15,16,17,18,19,20,21,22,23,24,25])
pH = np.array([3.21,3.60,3.88,4.07,4.24,4.38,4.51,4.64,4.78,4.93,5.11,5.28,5.60,5.69,5.78,5.95,6.03,6.28,6.75,7.08,9.32,10.26,10.68,10.83,10.94,11.1,11.17,11.29,11.47,11.60,11.70,11.83,11.90,11.95,12.00,12.02,12.08,12.10])

# Définition des variables
Cb = 0.100 # Concentration base en mol/L
C_AH = 0.145 # Concentration attendue en acide en mol/L
Vo = 10.0 # Volume solution d'acide éthanoïque en mL
Ve = (C_AH*Vo/Cb) #(en mL)

n_AH = np.zeros(len(Vb))
n_HO = np.zeros(len(Vb))
n_NA = np.zeros(len(Vb))
n_A = np.zeros(len(Vb))

# Cacluls
Vb_new, derivee_pH = derivee(Vb, pH)
max = max(derivee_pH)
Vbe = Vb_new[derivee_pH == max]
print("Volume à l'équivalence =", Vbe[0], "mL")

for i in range(len(Vb)) :
    Vol = Vb[i]
    if Vol <= Vbe[0]:
        # Reactifs
        n_AH[i] = Cb*Vbe[0] - Cb*Vol
        n_HO[i] = 0
        # Produits
        n_A[i] = Cb*Vol
        n_NA[i] = Cb*Vol
    else :
        # Reactifs
        n_AH[i] = 0
        n_HO[i] = Cb*(Vol-Vbe[0])
        # Produits
        n_A[i] = Cb*Vbe[0]
        n_NA[i] = Cb*Vol
        
# Première courbe
plt.subplot(311)
plt.plot(Vb, pH, "r+-")
plt.axvline(Vbe, color="blue")
plt.title("Titrage pH-métrique de l'acide éthanoïque par la soude", fontsize = 20)
#plt.xlabel("Vb (mL)")
plt.xlim(0,25)
plt.ylabel("pH", fontsize = 20)
plt.tick_params(axis = 'both', labelsize = 16)
plt.grid()
# Seconde courbe
plt.subplot(312)
plt.plot(Vb_new, derivee_pH, "r+-")
plt.axvline(Vbe, color="blue")
plt.title("Dérivation du pH", fontsize = 20)
#plt.xlabel("Vb (mL)")

plt.xlim(0,25)
plt.ylabel("$\dfrac{dpH}{dVb}$", fontsize = 20)
plt.tick_params(axis = 'both', labelsize = 16)
plt.grid()
plt.show()

# Troisième courbe (courbe d'évolution des quantités de matière)
plt.subplot(313)
plt.plot(Vb, n_AH, "r-+", label ='Acide éthanoïque $CH_3COOH$')
plt.plot(Vb, n_HO, "b-+", label ='Ions hydroxyde $HO^-$')
#plt.plot(Vb, n_NA, "g-+", label = 'Ions sodium Na+') # peut être placé en commentaire si jugé inutile
plt.plot(Vb, n_A, "c-+", label = 'Ions éthanoate $CH_3COO^-$')
plt.legend(fontsize = 12)
plt.title("Quantités de matière", fontsize = 20)
plt.xlabel("V (mL)", fontsize = 20)
plt.ylabel("n (mol)", fontsize = 20)
plt.tick_params(axis = 'both', labelsize = 16)
plt.xlim(0,25)
plt.grid()