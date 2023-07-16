"""Tracé du diagramme de distribution d'un couple acido-basique

Description
-----------
Ce programme trace un diagramme de distribution pour un couple acido-basique
impliquant un monoacide (ici l'acide acétique/ion acétate)

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
#                           Cas d'un monoacide
# =============================================================================

pKa = 4.8

def proportion_AH(pH, pKa):
    return 1/(1+10**(pH-pKa))*100 # s'obtient à partir de pH = pKa + log(A-/AH)

pH = np.linspace(0,14,1000)

plt.plot(pH, proportion_AH(pH,pKa), 'r--', label = '$CH_3COOH$')
plt.plot(pH, 100-proportion_AH(pH,pKa), 'b--', label = '$CH_3COO^-$')
plt.grid(True)
plt.xlabel('pH', fontsize = 24)
plt.ylabel("proportions (%)", fontsize = 24)
plt.tick_params(axis = 'both', labelsize = 20)
plt.legend(fontsize = 18)
plt.title("Diagramme de distribution du couple acide acétique / ion acétate", fontsize = 24)
plt.show()
