"""Détermination de la composition d'un système à l'état final (pour une évolution dans le sens direct)

Description
-----------
Ce programme donne l'avancement final, le taux d'avancement, et les 
concentrations à l'état final d'une réaction chimique.
Il ne fonctionne que pour des réactions dont les nombres stoechiométriques 
sont tous égaux à 1 (par exemple la dissociation d'un monoacide dans l'eau).

Il fonctionne aussi bien pour des évolutions dans le sens direct que pour des
évolutions dans le sens indirect.

Il est laissé à l'appréciation de l'utilisateur de donner les formules brutes
en caractère unicode ou non, auquel cas l'utilisateur prendra garde de nommer 
"H2O" en caractère unicode aux lignes 74 et 108.

Formules
--------
Loi d'action des masses


Informations
------------
Auteurs : Guillaume Gallician et la prépa agreg de Montrouge
Année de création : 2021
Version : 1.3
Version de Python : 3.7
Licence : Creative Commons Attribution - Pas d'utilisation Commerciale 4.0 International

Liste des modifications :

"""


import numpy as np

# ======================== Equation de réaction ===============================
# a*réactif_1 + b*réactif_2 = c*produit_1 + d*produit_2
# Par exemple la dissociation de l'acide acétique dans l'eau
# CH3COOH + H2O = CH3COO- + H3O+
# =============================================================================

Reactifs = ["CH3COOH", "H2O"]
Produits = ["CH3COO-", "H3O+"]
Systeme = Reactifs + Produits

# Indication de la constante d'équilibre thermodynamique K°(T) - Cas d'un équilibre (réaction non totale)
Keq = 1*10**(-4.8) # Ka de l'acide acétique

#######  indication des nombres stoechiométriques ####### doivent tous être égaux à 1
a = 1
b = 1
c = 1
d = 1

Nombre_stoechio = [-a, -b, c, d] # Attention : prise en compte des nombres stoechio algébriques

#######  indications des conditions initiales  ####### assimilations des activités aux concentrations (en mol/L)

C1_ini = 0.5
C2_ini = 1
C3_ini = 0.5
C4_ini = 0.3

C_initiales = [C1_ini, C2_ini, C3_ini, C4_ini]

# =============================================================================
#           DÉBUT DU SCRIPT - RIEN NE DOIT ETRE MODIFIÉ EN-DESSOUS
# =============================================================================

# Définition des concentrations finales en fonction des concentrations initiales

def C_fin(i,x):
    if Systeme[i] == 'H2O':
        return 1  # La "concentration de H2O" n'a pas de sens mais ici on définit en réalité son activité, prise constante et égale à 1.
    else:
        return round(C_initiales[i] + Nombre_stoechio[i]*x, 5)    # la fonction round détermine le nombre de chiffres après la virgule

# =============================================================================
# Détermination de l'avancement à l'état final grâce à la loi d'action des masses (LAM)
# =============================================================================

Xi_max = min(C1_ini/a, C2_ini/b) # détermination de l'avancement théorique maximal

if a == b == c == d == 1:
    # expression polynomiale de la LAM :
    # (1-Keq)*x**2 + (Keq*(C1_ini + C2_ini) + C3_ini + C4_ini)*x + (C3_ini*C4_ini - Keq*(C1_ini*C2_ini)) = 0 
    p = [(1-Keq), (Keq*(C1_ini + C2_ini) + C3_ini + C4_ini), (C3_ini*C4_ini - Keq*(C1_ini*C2_ini))]
    solutions = np.roots(p)
    for s in solutions:
        if 0 < s and s < Xi_max:                      # évolution dans le sens direct
            x = round(s,5)
            print("L'avancement final est égal à " + str(x) + " mol/L" + "\n")
            t = round(x/Xi_max, 5)
            print("Le taux d'avancement est " + str(t) + "\n")
        elif s < 0 and -s < min(C3_ini/c, C4_ini/d):  # traduit une possible évolution dans le sens indirect
            Xi_min = -min(C3_ini/c, C4_ini/d)         # NB Xi_min est strictement négatif
            x = round(s,5)
            print("L'avancement final est égal à " + str(x) + " mol/L" + "\n")
            t = round(x/Xi_min, 5)
            print("Considérant la réaction dans le sens indirect, le taux d'avancement est " + str(t) + "\n")
    
# =============================================================================
#           Écriture des quantités de matières dans l'état final
# =============================================================================

    for i in range(4):
        if Systeme[i] == 'H2O':
            print("H\u2082O est en large excès")
        else:
            print("[" + Systeme[i] + "]finale = " + str(C_fin(i,x)) + " mol/L")

else :
    print("Les nombres stoechiométriques ne sont pas tous égaux à 1")