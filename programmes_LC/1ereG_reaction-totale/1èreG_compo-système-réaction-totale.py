"""Détermination de la composition d'un système à l'état final (pour une réaction totale)

Description
-----------
Ce programme donne le réactif limitant et les concentrations à l'état final 
d'une réaction chimique totale.

Les formules brutes sont à donner en caractère unicode pour que les données 
affichées soient sans ambiguïté' (voir liste Reactifs et liste Produits, l 34-35).

Ce programme est inexact si le solvant intervient comme réactif ou produit.

Formules
--------

Informations
------------
Auteurs : Guillaume Gallician et la prépa agreg de Montrouge
Année de création : 2021
Version : 1.3
Version de Python : 3.7
Licence : Creative Commons Attribution - Pas d'utilisation Commerciale 4.0 International

Liste des modifications :

"""


# ======================== Equation de réaction ===============================
# a*réactif_1 + b*réactif_2 = c*produit_1 + d*produit_2
# Par exemple l'oxydation des ions thiosulfates par le diiode
# I2 + 2(S2O3)2- = 2I- + (S4O6)2-
# =============================================================================

Reactifs = [u'I\u2082', u'S\u2082O\u2083\u00B2\u207B']
Produits = [u'I\u207B', u'S\u2084O\u2086\u00B2\u207B']
Systeme = Reactifs + Produits

#######  indication des nombres stoechiométriques #######
a = 1
b = 2
c = 2
d = 1

Nombre_stoechio = [-a, -b, c, d] # Attention : prise en compte des nombres stoechio algébriques

#######  indications des conditions initiales  ####### assimilations des activités aux concentrations (en mol/L)

n1_ini = 0.5
n2_ini = 1
n3_ini = 0
n4_ini = 0

n_initiales = [n1_ini, n2_ini, n3_ini, n4_ini]

# =============================================================================
#           DÉBUT DU SCRIPT - RIEN NE DOIT ETRE MODIFIÉ EN-DESSOUS
# =============================================================================

#Définition des concentrations finales en fonctions des concentrations initiales

def n_fin(i,x):
    return n_initiales[i] + Nombre_stoechio[i]*x

# =============================================================================
# Détermination du réactif limitant et de l'avancement maximal
# =============================================================================

Xi_max = 0
if n1_ini/a < n2_ini/b:
    Xi_max = n1_ini/a
    print("Le réactif limitant est "+ Reactifs[0])
elif n1_ini/a > n2_ini/b:
    Xi_max = n2_ini/b
    print("Le réactif limitant est "+ Reactifs[1])
else:
    Xi_max = n2_ini/b
    print("Les réactifs sont introduits dans les proportions stoechiométriques")
    
# =============================================================================
# Écriture des concentrations à l'état final
# =============================================================================
print()
for i in range(4):
    print("n(" + Systeme[i] + ")final = " + str(n_fin(i,Xi_max)) + " mol" )
    
