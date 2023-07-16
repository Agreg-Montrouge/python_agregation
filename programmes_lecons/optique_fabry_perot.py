r"""Figure de diffraction par N fentes

Description
-----------
Ce programme représente la figure d'interférence obtenue lorsqu'une onde 
plane monochromatique de longueur d'onde $\lambda$ traverse un dispositif 
de $N$ fentes régulièrement espacées d'une distance $a$ (centre-centre) et de 
largeur $b$ chacunes. L'écran est positionné �  une distance $D$ des fentes. 

Le résultat présenté est l'intensité lumineuse normalisée en fonction de 
la position sur l'écran pour permettre une comparaison des différentes situations.

Formules
--------


Informations
------------
Auteurs : Arnaud Raoux, Emmanuel Baudin, François Lévrier, Pierre Cladé et la prépa agreg de Montrouge
Année de création : 2020
Version : 1.0
Version de Python : 3.6
Licence : Creative Commons Attribution - Pas d'utilisation Commerciale 4.0 International
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from programmes_lecons import FloatSlider, IntSlider
from programmes_lecons import make_param_widgets, make_choose_plot, make_reset_button
from programmes_lecons import justify

titre = r"Intensités issues d'une cavité Fabry-Pérot"

#description = r"""Ce programme représente la figure d'interférence obtenue lorsqu'une onde 
#plane monochromatique de longueur d'onde $\lambda$ traverse un dispositif 
#de $N$ fentes régulièrement espacées d'une distance $a$ (centre-centre) et de 
#largeur $b$ chacunes. L'écran est positionné �  une distance $D$ des fentes. 
#
#Le résultat présenté est l'intensité lumineuse normalisée en fonction de 
#la position sur l'écran pour permettre une comparaison des différentes situations.
#
#$\frac{I}{I_0} = \mathrm{sinc}^2\left(\frac{\pi bx}{\lambda D}\right)\times\frac{\sin^2(N\pi a x/\lambda D)}{N^2\sin^2(\pi ax/\lambda D)}$
#"""


#===========================================================
# --- Variables globales et paramètres ---------------------
#===========================================================

parameters = dict(
    m = FloatSlider(value=1, min=1, max=1000.0, description='Paramètre sans dim')
)

#===========================================================
# --- Modèle physique --------------------------------------
#===========================================================

def Itransmis(phi,m):
    return 1/(1+m*np.sin(phi/2)**2)

def Ir(phi,m):
    return 1-Itransmis(phi,m)

#===========================================================
# --- Réalisation du plot ----------------------------------
#===========================================================

# La fonction plot_data est appelée �  chaque modification des paramètres
def plot_data(m):

    phi = np.linspace(-15, 15, 2001) #Zone observee : +/- 1 cm
    sig = Itransmis(phi,m)
    refl = Ir(phi,m)

    lines['It'].set_data(phi, sig)  # On met a jour le signal
    lines['Ir'].set_data(phi, refl)  # On met a jour le signal
    fig.canvas.draw_idle()

#===========================================================
# --- Création de la figure et mise en page ----------------
#===========================================================

fig = plt.figure()
fig.suptitle(titre)
#fig.text(0.02, .9, justify(description), multialignment='left', verticalalignment='top')

ax = fig.add_axes([0.35, 0.3, 0.6, 0.6])

lines = {}
lines['It'], = ax.plot([],[], lw=2, color='red')
lines['Ir'], = ax.plot([],[], '--', lw=1, color='blue')
#lines['facteur de forme'], = ax.plot([],[], lw=1.5, ls='--', color='blue', visible=false)
#lines['facteur de structure'], = ax.plot([], [], lw=1.5, ls='--', color='green', visible=false)

ax.set_xlabel(r"Déphasage $\varphi$")
ax.set_ylabel('Intensité lumineuse normalisee')

ax.set_xlim(-15, 15)
ax.set_ylim(-0.1, 1.2)


param_widgets = make_param_widgets(parameters, plot_data, slider_box=[0.55, 0.07, 0.4, 0.15])
choose_widget = make_choose_plot(lines, box=[0.015, 0.15, 0.2, 0.15])
reset_button = make_reset_button(param_widgets)

if __name__=='__main__':
    plt.show()  # On provoque l'affichage a l'ecran
