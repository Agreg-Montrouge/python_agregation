#Nom du programme : PortraitdePhase

#Auteurs : Arnaud Raoux, François Lévrier, Emmanuel Baudin, Pierre Cladé et la prépa agreg de Montrouge

#Année de création : 2016 
#Version : 1.1

#Liste des modifications
#v 1.00 : 2016-05-02 Première version complète
#v 1.1 : supression des variables globales

titre = "Portrait de phase d'un pendule"

description="""Représente partiellement le portrait de phase d'une solution de l'équation d'un pendule simple. Seules les trajectoires commençant à theta=0 (avec une grande gamme de vitesses initiales) sont tracées, d'où un portrait de phase non rempli."""


#import des bibliothèques python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint # Pour la resolution d'equations differentielles

from programmes_lecons import justify

# =============================================================================
# --- Définitions ------------------------------------------------
# =============================================================================

omega0 = 4 # Pulsation propre en U.A.

N = 100 # le nombre de pas
t = np.linspace(0, 5, N) # le temps en U.A.

# Etats initiaux
Ninit = 20 # nbr de conditions initiales
dtheta_init_list = np.linspace(-50, 50, Ninit)


# =============================================================================
# --- Fonction intermediaire ------------------------------------------------
# =============================================================================

def eq_diff(etat_courant, t, omega0):
    """
    Fonction qui encode l equation differentielle
    """  
    return np.array([etat_courant[1], -omega0**2*np.sin(etat_courant[0])])


def plot_data(ax, omega0):
    """Résolution de l'equation differentielle pour chaque condition intiale"""

    for dtheta_init in dtheta_init_list:
        etat_init=np.array([0, dtheta_init/omega0])
        solution = odeint(eq_diff, etat_init, t, args=(omega0,))

        ax.plot(solution[:,0], solution[:,1], color='red', linewidth=1)
        ax.plot(-solution[:,0], solution[:,1], color='red', linewidth=1) # la fonction dtheta(theta) etant paire


# =============================================================================
# --- Creation de la figure ------------------------------------------
# =============================================================================
fig = plt.figure()
fig.suptitle(titre)
fig.text(0.5, .93, justify(description, 120), multialignment='left', verticalalignment='top', horizontalalignment='center')

ax = fig.add_axes([0.1, 0.06, 0.8, 0.8])

ax.set_ylim(-15,15)
ax.set_ylabel(r'$\dot \theta$')
ax.set_xlim(-8,8)
ax.set_xlabel(r'$\theta$')

plot_data(ax, omega0=4)
#ax.axis('equal')

if __name__=="__main__":
    plt.show()


