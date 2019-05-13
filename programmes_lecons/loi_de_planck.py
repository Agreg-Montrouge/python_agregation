#Nom du programme : loi_de_planck

#Auteurs : François Lévrier, Emmanuel Baudin, Arnaud Raoux, Pierre Cladé et la prépa agreg de Montrouge

#Année de création : 2016 
#Version : 1.3

#Liste des modifications
#v 1.0 : 2016-03-01 Première version complète
#v 1.1 : 2016-05-02 Mise à jour de la mise en page - baudin@lpa.ens.fr
#v 1.2 : 2019-01-09 Remplacement de axisbg dépréciée par facecolor
#v 1.3 : 2019-05-10 Simplification du programme

import matplotlib.pyplot as plt
import numpy as np

from programmes_lecons import FloatSlider, IntSlider
from programmes_lecons import make_param_widgets, make_choose_plot, make_reset_button, make_log_button
from programmes_lecons import justify
from constantes import c, h, k

titre = r'Loi de Planck'

description = r"""Ce programme représente la loi de Planck du corps noir en fonction de la fréquence du rayonnement électromagnétique. Il est possible de modifier la température du corps noir pour observer les effets. 

Les lois de Rayleigh-Jeans et de Wien ont aussi été implémentées pour comparaison.

Planck : $\frac{2h\nu^3}{c^2 (e^{h\nu/kT} -1)}$

Wien : $\frac{2h\nu^3}{c^2 e^{h\nu/kT}}$

Rayleigh-Jeans: $\frac{2kT\nu^2}{c^2}$

"""

# Parametres de la fonction, avec des valeurs par defaut
parameters = {
    'T' : FloatSlider(value=5800, description='Température -- $T$ (K)', min=1, max=10000),
    }


# Modèles utilisés
def loi_de_planck(T, nu):
    return 2*h*nu**3/c**2 * 1/(np.exp(h*nu/(k*T)) - 1 )

def loi_de_rayleigh_jeans(T, nu):
    return 2*k*T*nu**2/c**2

def loi_de_wien(T, nu):
    return 2*h*nu**3/c**2 * 1/(np.exp(h*nu/(k*T)))


# Création de la figure
fig = plt.figure()
fig.suptitle(titre)
fig.text(0.02, .9, justify(description), multialignment='left', verticalalignment='top')

ax = fig.add_axes([0.35, 0.3, 0.6, 0.6])

ax.axvline(6.7E14,lw=2, color='purple') #violet
ax.axvline(5.7E14,lw=2, color='green') #vert
ax.axvline(4.6E14,lw=2, color='red') #rouge

ax.text(4.7E14, 5e-8, "rouge :  633 nm", color='red', rotation='vertical',horizontalalignment='left', verticalalignment='top')
ax.text(5.8E14, 5e-8, "vert : 525 nm", color='green', rotation='vertical',horizontalalignment='left', verticalalignment='top')
ax.text(6.8E14, 5e-8, "violet : 425 nm", color='purple', rotation='vertical',horizontalalignment='left', verticalalignment='top')

lines = {}
lines['Planck'], = ax.plot([], [], lw=2, color='blue',visible=True)
lines['Wien'], = ax.plot([], [], lw=2,color='black', visible=False)
lines['Rayleigh-Jeans'], = ax.plot([], [], lw=2, color='brown',visible=False)

nu = np.logspace(np.log10(1E13),np.log10(1.2E15),num=1001)

ax.set_xlim(nu.min(), nu.max())
ax.set_ylim(5E-11, 5E-8)

ax.set_xlabel(r"$\nu$ [$\mathrm{Hz}$]")
ax.set_ylabel(r"$B_\nu$ [$\mathrm{W.m^{-2}.Hz^{-1}.sr^{-1}}$]")

#ax.set_yscale('log')
#ax.set_xscale('log')

def plot_data(T):

    lines['Planck'].set_data(nu, loi_de_planck(T, nu))
    lines['Wien'].set_data(nu, loi_de_wien(T, nu))
    lines['Rayleigh-Jeans'].set_data(nu, loi_de_rayleigh_jeans(T, nu))

    fig.canvas.draw_idle()


param_widgets = make_param_widgets(parameters, plot_data, slider_box=[0.35, 0.07, 0.4, 0.05])
choose_widget = make_choose_plot(lines, box=[0.015, 0.25, 0.2, 0.15])
reset_button = make_reset_button(param_widgets)
log_button =  make_log_button(ax)

if __name__=='__main__':
    plt.show()



