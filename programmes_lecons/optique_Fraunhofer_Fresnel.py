#!/usr/bin/env python3
# -*- Encoding: utf-8 -*-
#
r"""Figure de diffraction par une fente

Description
-----------
Ce programme représente la figure d'interférence obtenue lorsqu'une onde 
plane monochromatique de longueur d'onde $\lambda$ traverse un dispositif 
de $N$ fentes régulièrement espacées d'une distance $a$ (centre-centre) et de 
largeur $b$ chacunes. L'écran est positionné à une distance $D$ des fentes. 

Le résultat présenté est l'intensité lumineuse normalisée en fonction de 
la position sur l'écran pour permettre une comparaison des différentes situations.

Formules
--------
$\frac{I}{I_0} = \mathrm{sinc}^2\left(\frac{\pi bx}{\lambda D}\right)\times\frac{\sin^2(N\pi a x/\lambda D)}{N^2\sin^2(\pi ax/\lambda D)}$


Informations
------------
Auteurs : Arnaud Raoux, Pierre Cladé et la prépa agreg de Montrouge
Année de création : 2016 
Version : 1.3
Version de Python : 3.6
Licence : Creative Commons Attribution - Pas d'utilisation Commerciale 4.0 International

Liste des modifications :
    * v 1.0 : 2024-03-28 Première version complète
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy.special as sc


from programmes_lecons import FloatSlider, IntSlider
from programmes_lecons import make_param_widgets, make_choose_plot, make_reset_button
from programmes_lecons import justify

titre = r"Figure de diffraction par une fente"

description = r"""Ce programme représente la diffraction par une fente de largeur $a$ dans 
les approximations de Fresnel et de Fraunhofer. L'écran est positionné à une distance $D$ de la fente. 

Le résultat présenté est l'intensité lumineuse normalisée.
"""


#===========================================================
# --- Variables globales et paramètres ---------------------
#===========================================================

parameters = dict(
    a = FloatSlider(value=0.1, min=0.05, max=3.0, description='Largeur de fente -- a (mm)'),
    lamb = FloatSlider(value=0.633, min=0.1, max=3., description=r"Longueur d'onde -- $\lambda_0$ (µm)"),
    D = FloatSlider(value=1, min=.3, max=2, description="Distance fentes-écran -- $D$ (m)"),
#    form_fact = Checkbox(value=False, description='Facteur de forme'),
#    form_struct = Checkbox(value=False, description='Facteur de structure')
)

#===========================================================
# --- Modèle physique --------------------------------------
#===========================================================

def Fraunhofer(F,x,y,w):
    Ix = 4*F*(np.sinc(2*F*x/w))**2
    Iy = 4*F*(np.sinc(2*F*y/w))**2
    return Ix*Iy

def Fresnel(F,x,y,w):
    lim = np.sqrt(2*F)*np.array([-(1+x/w),1-x/w,-(1+y/w),1-y/w])
    S, C = sc.fresnel(lim)
    Ix=0.5*((C[1]-C[0])**2+(S[1]-S[0])**2)
    Iy=0.5*((C[3]-C[2])**2+(S[3]-S[2])**2)
    return Ix*Iy


#===========================================================
# --- Réalisation du plot ----------------------------------
#===========================================================

# La fonction plot_data est appelée à chaque modification des paramètres
def plot_data(lamb,a, D):
    # Conversion en SI
    lamb = lamb*1E-6
    a = a*1E-3
    F = a**2 / (lamb*D)
    
    N= 2001
    x = 1e-2*np.linspace(-1, 1, N) #Zone observee 

    form = Fraunhofer(F,x,0,a)
    struct = np.zeros(N)
    for i in np.arange(N):
        struct[i] = Fresnel(F,x[i],0,a)

    lines['Approximation de Fraunhofer'].set_data(x, form)  # On met a jour la forme
    lines['Approximation de Fresnel'].set_data(x, struct)  # On met a jour la structure

    fig.canvas.draw_idle()

#===========================================================
# --- Création de la figure et mise en page ----------------
#===========================================================

param=np.zeros(3)
for i, (key, elm) in enumerate(parameters.items()):
    param[i]=elm.value

F=param[0]**2/(param[1]*param[2])

fig = plt.figure()
fig.suptitle(titre)
fig.text(0.02, .9, justify(description), multialignment='left', verticalalignment='top')

ax = fig.add_axes([0.35, 0.3, 0.6, 0.6])

lines = {}
lines['Approximation de Fraunhofer'], = ax.plot([],[], lw=1.5, ls='-', color='blue')#, visible=False)
lines['Approximation de Fresnel'], = ax.plot([], [], lw=1.5, ls='-', color='red')

ax.set_xlabel(r"Position sur l'écran $x$")
ax.set_ylabel('Intensité lumineuse normalisee')

ax.set_xlim(-1e-2, 1e-2)
ax.set_ylim(-0.1, 2.2)

ax.text(0, 1, r'$F=${}'.format(F), verticalalignment='bottom', horizontalalignment='center')

param_widgets = make_param_widgets(parameters, plot_data, slider_box=[0.55, 0.07, 0.4, 0.15])
choose_widget = make_choose_plot(lines, box=[0.015, 0.15, 0.2, 0.15])
reset_button = make_reset_button(param_widgets)

if __name__=='__main__':
    plt.show()  # On provoque l'affichage a l'ecran
    
    for i, (key, elm) in enumerate(parameters.items()):
        param[i]=elm.value
    F=param[0]**2/(param[1]*param[2])

