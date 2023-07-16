# -*- coding: utf-8 -*-
"""
Simulation d'une courbe de titrage par conductimétrie

AH(aq) + HO-(aq) -> A-(aq) + H2O(l)
Conductivité molaire ionique en mS.m2.mol-1 à 25°C
lambda(Na+) = 5,0
lambda(HO-) = 20,0
lambda(A-) = 4,1

Auteur : David Therincourt (Lycée Roland Garros - Académie de la Réunion)
Téléchargé sur le site https://physique-chimie-python.readthedocs.io/fr/latest/
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (8,10) # width, height in inches (100 dpi)
plt.subplots_adjust(hspace=0.2, left=0.15, bottom=0.06, right=0.95, top=0.95 ) # Position en %
lambda_HO, lambda_Na, lambda_A = 20.0, 5.0, 4.1
Cb = 0.100 # Concentration base en mol/L
C_AH = 0.145 # Concentration acide en mol/L
Vo = 10.0E-3 # Volume solution d'acide éthanoïque
Veau = 200.0E-3 # Volume d'eau ajouté en L
Ve = C_AH*Vo/Cb # Volume équivalent en mL calculé Ve = C_AH*Vo/Cb
NB = 50 # Nb points
V = np.linspace(0, 2*Ve, NB) # Initialisatin du tableau de volume
# Initialisation des tableaux de concentration
n_AH = np.zeros(NB)
n_HO = np.zeros(NB)
n_NA = np.zeros(NB)
n_A = np.zeros(NB)

for i in range(NB) :
    Vol = V[i]
    if Vol <= Ve :
        # Reactifs
        n_AH[i] = C_AH*Vo - Cb*Vol
        n_HO[i] = 0
        # Produits
        n_A[i] = Cb*Vol
        n_NA[i] = Cb*Vol
    else :
        print(i, Vol)
        # Reactifs
        n_AH[i] = 0
        n_HO[i] = Cb*(Vol-Ve)
        # Produits
        n_A[i] = Cb*Ve
        n_NA[i] = Cb*Vol

# Calcul du tableau de conductivité
sigma = (lambda_HO*n_HO + lambda_A*n_A + lambda_Na*n_NA) / (Veau + V)

# Courbe d'évolution des quantités de matière
plt.subplot(211)
plt.plot(V*1000, n_AH, "r-+", label ='Acide éthanoïque $CH_3COOH$')
plt.plot(V*1000, n_HO, "b-+", label ='Ions hydroxyde $OH^-$')
plt.plot(V*1000, n_NA, "g-+", label = 'Ions sodium $Na^+$') # peut être placé en commentaire si jugé inutile
plt.plot(V*1000, n_A, "c-+", label = 'Ions éthanoate $CH_3COO^-$')
plt.legend(fontsize = 14)
plt.title("Evolution des quantités de matière", fontsize = 20)
plt.xlabel("V (mL)", fontsize = 20)
plt.ylabel("n (mol)", fontsize = 20)
plt.tick_params(axis = 'both', labelsize = 16)
plt.grid()

# Courbe d'évolution de la conductivité
plt.subplot(212)
plt.plot(V*1E3, sigma, "-+")
plt.axvline(Ve*1E3, color="red", linestyle ="dashed")
plt.title("Evolution de la conductivité de la solution", fontsize = 20)
plt.xlabel("V (mL)", fontsize = 20)
plt.ylabel("$\sigma~(S\cdot m^{-1})$", fontsize = 20)
plt.tick_params(axis = 'both', labelsize = 16)
plt.grid()

plt.show()
