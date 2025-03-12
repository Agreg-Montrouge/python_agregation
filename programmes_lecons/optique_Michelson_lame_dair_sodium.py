#!/usr/bin/env python3
# -*- Encoding: utf-8 -*-
#
"""
@author: Hubert COSTE

Centre de préparation à l'agrégation de physique de Montrouge 
(ENS PSL - Sorbonne université - Paris Saclay)
Promotion 2024-2025

Itensité lumineuse pour un Michelson en lame d'air pour:
    - une source monochromatique 
    - une lampe à vapeur de soduim (2 longueurs d'onde)

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


import matplotlib as mpl
mpl.rc('lines', linewidth=3)
mpl.rc('font', size=15)
mpl.rc('axes', linewidth=1.5, labelsize=15)
mpl.rc('legend', fontsize=15)
cm = 1/2.54

#%%

r = np.linspace(-1, 1, 200)*1e-2
f = 0.1 #focal de lentille
i = np.arctan(r/f)
e = 0.2 #épaisseur lame d'air par défaut

#Sodium
lambda1 = 589.5924
lambda2 = 588.995
dlam = lambda1-lambda2 

#Plot 1D
delta = 2*e*np.cos(i)*1e-3 #différence de marche
I1_I0 = 1 + np.cos(2*np.pi*delta/(lambda1*1e-9))
I2_I0 = 1 + np.cos(2*np.pi*delta/(lambda2*1e-9))
I_I0_tot = I1_I0 + I2_I0

#Plot 2D
x,y = np.meshgrid(r,r)
r_mesh = np.sqrt(x**2 + y**2)
i_mesh = np.arctan(r_mesh/f)
delta = 2*e*np.cos(i_mesh)*1e-3
I1_I0_mesh = 1 + np.cos(2*np.pi*delta/(lambda1*1e-9))
I2_I0_mesh = 1 + np.cos(2*np.pi*delta/(lambda2*1e-9))
I_I0_tot_mesh = I1_I0_mesh + I2_I0_mesh

#%% #SOURCE MONOCHROMATIQUE

fig, ax = plt.subplots(1,2, gridspec_kw={'width_ratios': [3, 2]}, figsize=(35*cm,20*cm))  # création du cadre qui contiendra le sinus
plt.subplots_adjust(top=0.55) # position de la ligne inférieure du cadre
								 # 0=bas de la figure, 1=haut de la figure
# Tracé de la courbe et enregistrement dans "ligne" pour pouvoir la modifier
ligne1, = ax[0].plot(r*1e3, I1_I0, lw=2, color='firebrick', alpha=0.5)
ax[0].set_title('Intensité lumineuse\n $e = ${:6.2f} mm, $\lambda = $ {:6.2f} nm\n'.format(e, lambda1)) 
ax[0].set_ylabel("$I/I_0$")
ax[0].set_xlabel("$r$ (mm)")
ax[0].axis([np.min(r*1e3), np.max(r*1e3), -0.2, 2.2])

img0 = ax[1].imshow(I1_I0_mesh,  extent=[np.min(r)*1e3, np.max(r)*1e3, np.min(r)*1e3, np.max(r)*1e3], cmap="copper", alpha=0.9)

# GLISSIERE
axe = plt.axes([0.15, 0.80, 0.75, 0.05], facecolor='ivory') # les coordonnées [position coin inférieur gauche, longueur, hauteur] 
se = Slider(axe, 'e (mm)', 0, 0.5, valinit=e, color="pink") # création de la glissière dans ce cadre

# fonction qui sera appelée lorsqu'on déplace la glissière
def miseAjour(val):
    e = se.val
    
    #Plot 1D
    delta = 2*e*np.cos(i)*1e-3 #différence de marche
    I1_I0 = 1 + np.cos(2*np.pi*delta/(lambda1*1e-9))
    
    #Plot 2D
    x,y = np.meshgrid(r,r)
    r_mesh = np.sqrt(x**2 + y**2)
    i_mesh = np.arctan(r_mesh/f)
    delta = 2*e*np.cos(i_mesh)*1e-3
    I1_I0_mesh = 1 + np.cos(2*np.pi*delta/(lambda1*1e-9))

 		 	
    #Mise à jour de plots
    ligne1.set_ydata(I1_I0) # on met à jour la ligne
    ax[0].set_title('Intensité lumineuse\n $e = ${:6.2f} mm, $\lambda = $ {:6.2f} nm\n'.format(e, lambda1))  
    img0.set_data(I1_I0_mesh)
    fig.canvas.draw_idle()
    
se.on_changed(miseAjour)

# BOUTON 'Remise à zéro'
resetax = plt.axes([0.1, 0.9, 0.20, 0.04])
bouton = Button(resetax, 'Remise à zéro',  hovercolor='lightblue',color='red')

def miseAzero(event):
    se.reset()
bouton.on_clicked(miseAzero)
plt.show()



#%% SOURCE = SODIUM

fig, ax = plt.subplots(1,2, gridspec_kw={'width_ratios': [3, 2]}, figsize=(35*cm,20*cm))  # création du cadre qui contiendra le sinus
plt.subplots_adjust(top=0.55) # position de la ligne inférieure du cadre
								 # 0=bas de la figure, 1=haut de la figure
# Tracé de la courbe et enregistrement dans "ligne" pour pouvoir la modifier
ligne1, = ax[0].plot(r*1e3, I1_I0, lw=2, color='firebrick', alpha=0.5, label="$I_1$")
ligne2, = ax[0].plot(r*1e3, I2_I0, lw=2, color='darkblue', alpha=0.5, label="$I_2$")
ligne3, = ax[0].plot(r*1e3, I_I0_tot, lw=2, color='k', ls="--", alpha=1, label="$I_1+I_2$")
ax[0].set_title('Intensité lumineuse\n $e = ${:6.2f} mm, $\lambda1 = $ {:6.2f} nm, $\lambda2 = $ {:6.2f} nm'.format(e, lambda1, lambda2)) 
ax[0].set_ylabel("$I/I_0$")
ax[0].set_xlabel("$r$ (mm)")
ax[0].axis([np.min(r*1e3), np.max(r*1e3), -0.2, 4.2])
img0 = ax[1].imshow(I_I0_tot_mesh,  extent=[np.min(r)*1e3, np.max(r)*1e3, np.min(r)*1e3, np.max(r)*1e3], cmap="copper", alpha=0.9)
ax[0].legend(ncol=3, loc=2)

# GLISSIERE
axe = plt.axes([0.15, 0.80, 0.75, 0.05], facecolor='ivory') # les coordonnées [position coin inférieur gauche, longueur, hauteur] 
se = Slider(axe, 'e (mm)', 0, 0.5, valinit=e, color="pink") # création de la glissière dans ce cadre
axdlam = plt.axes([0.15, 0.73, 0.75, 0.05], facecolor='ivory') 
sdlam = Slider(axdlam, '$\Delta \lambda$ (nm)', 0, 10, valinit=dlam, color="pink")

# fonction qui sera appelée lorsqu'on déplace la glissière
def miseAjour(val):
    e = se.val
    dlam = sdlam.val
    lambda2 = lambda1 + dlam
    
    #Plot 1D
    delta = 2*e*np.cos(i)*1e-3 #différence de marche
    I1_I0 = 1 + np.cos(2*np.pi*delta/(lambda1*1e-9))
    I2_I0 = 1 + np.cos(2*np.pi*delta/(lambda2*1e-9))
    I_I0_tot = I1_I0 + I2_I0
    
    #Plot 2D
    x,y = np.meshgrid(r,r)
    r_mesh = np.sqrt(x**2 + y**2)
    i_mesh = np.arctan(r_mesh/f)
    delta = 2*e*np.cos(i_mesh)*1e-3
    I1_I0_mesh = 1 + np.cos(2*np.pi*delta/(lambda1*1e-9))
    I2_I0_mesh = 1 + np.cos(2*np.pi*delta/(lambda2*1e-9))
    I_I0_tot_mesh = I1_I0_mesh + I2_I0_mesh
 		 	
    #Mise à jour de plots
    ligne1.set_ydata(I1_I0) # on met à jour la ligne
    ligne2.set_ydata(I2_I0) # on met à jour la ligne
    ligne3.set_ydata(I_I0_tot) # on met à jour la ligne
    ax[0].set_title('Intensité lumineuse\n $e = ${:6.2f} mm, $\lambda_1 = $ {:6.1f} nm, $\lambda_2 = $ {:6.1f} nm\n'.format(e, lambda1, lambda2)) 
    img0.set_data(I_I0_tot_mesh)
    fig.canvas.draw_idle()
    
se.on_changed(miseAjour)
sdlam.on_changed(miseAjour)

# BOUTON 'Remise à zéro'
resetax = plt.axes([0.1, 0.9, 0.20, 0.04])
bouton = Button(resetax, 'Remise à zéro',  hovercolor='lightblue',color='red')
def miseAzero(event):
    se.reset()
    sdlam.reset()
bouton.on_clicked(miseAzero)
plt.show()
