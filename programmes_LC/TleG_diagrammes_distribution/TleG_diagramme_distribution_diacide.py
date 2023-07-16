"""Tracé du diagramme de distribution d'espèces chimiques impliquant un diacide.

Description
-----------
Ce programme trace un diagramme de distribution dans le cas d'un diacide (la glycine, un acide aminé)

Formules
--------
pH = pKa + log(A-/AH)


Informations
------------
Auteurs : Inspiré de la fiche Eduscol n°6 de "Programmer en Python" intitulée 
CONSTRUIRE UN DIAGRAMME DE DISTRIBUTION (Tle Générale - spécialité) mai 2020
par Guillaume Gallician et la prépa agreg de Montrouge
Année de création : 2022
Version : 1.3
Version de Python : 3.7
Licence : Creative Commons Attribution - Pas d'utilisation Commerciale 4.0 International

Liste des modifications :

"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
#                           Cas d'un diacide
# =============================================================================

# faire avec un acide aminé
pKa1 = 2.4
pKa2 = 9.6

def proportion_AH2(pH, pKa1, pKa2):
    return 1/(1 + 10**(pH-pKa1) + 10**(2*pH-pKa1-pKa2)) * 100

def proportion_AH(pH, pKa1, pKa2):
    return 1/(1 + 10**(pKa1-pH) + 10**(pH-pKa2)) * 100

#def proportion_A-(pH, pKa1, pKa2):
    #return

pH = np.linspace(0,14,1000)

plt.plot(pH, proportion_AH2(pH, pKa1, pKa2), 'r--', label = '$C_2H_6NO_2^+$')
plt.plot(pH, proportion_AH(pH, pKa1, pKa2), 'g--', label = '$C_2H_5NO_2$')
plt.plot(pH, 100 - proportion_AH2(pH, pKa1, pKa2) - proportion_AH(pH, pKa1, pKa2), 'b--', label = '$C_2H_4NO_2^-$')
plt.grid(True)
plt.xlabel('pH', fontsize = 24)
plt.ylabel("proportions (%)", fontsize = 24)
plt.tick_params(axis = 'both', labelsize = 20)
plt.legend(fontsize = 18)
plt.title("Diagramme de distribution des espèces acido-basiques associées à la glycine", fontsize = 24)
plt.show()
