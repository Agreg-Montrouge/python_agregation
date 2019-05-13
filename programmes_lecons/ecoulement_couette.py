#Nom du programme : EcoulementCouette

#Auteurs : Emmanuel Baudin, Arnaud Raoux, François Lévrier et la prépa agreg de Montrouge

#Année de création : 2016 
#Version : 1.1

#Liste des modifications
#v 1.0 : 2016-05-02 Première version complète - baudin@lpa.ens.fr

#Version de Python
#3.4

#LICENCE
#Cette oeuvre, création, site ou texte est sous licence Creative Commons Attribution - Pas d'Utilisation Commerciale 4.0 International. Pour accéder à une copie de cette licence, merci de vous rendre à l'adresse suivante http://creativecommons.org/licenses/by-nc/4.0/ ou envoyez un courrier à Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.

#Description : 
#Ce programme représente le champ de vitesse dans un ecoulement Couette plan

import matplotlib.pyplot as plt
import numpy as np

import programmes_lecons

titre = 'Écoulement de Couette plan'

#Definition d'un maillage du plan dans lequel a lieu l'ecoulement
Y, X = np.mgrid[-1:1:25j, 0:3:6j]

#Calcul du champ de vitesse
U = 4.*(Y+1)/2.
V = 0

#Epaisseur des vecteurs vitesse
widths = np.linspace(0, 2, X.size)

# Creation de la figure
fig = plt.figure()
fig.suptitle(titre)

ax = fig.subplots(1, 1)

#Creation des vecteurs vitesse
ax.quiver(X, Y, U, V, 
           color='Teal', 
           scale=25,
           headlength=10)

#Definition des axes
ax.set_xlim(0, 3)
ax.set_ylim(-1.5, 1.5)

#Repere des limites superieure et inferieure de l'ecoulement
ax.axhline(1, color='k')
ax.axhline(-1, color='k')

#Nom des axes
ax.set_xlabel('Position X (m)')
ax.set_ylabel('Position Z (m)')

if __name__=="__main__":
    plt.show(fig) # On provoque l'affichage a l'ecran
