#!/usr/bin/env python3
# -*- Encoding: utf-8 -*-
#
"""
Created on Sun May 03 10:43:50 2021

@author: Hubert COSTE
    L2 AV - CMI - DCLAM
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button

"""
Permet d'afficher une figure interactive représentant un miroir sphérique (concave ou convexe)
Les widgets proposés permettent de modifier les données du propblème (l'angle d'incidence et l'origine des rayons et les dimensions, l'emplacement et la nature du miroir)

"""

#Création des Class miroir et rayon
#----------------------------------  

class miroir :
    """
    création d'un objet miroir ayant comme attributs les coordonnées de chaque point  du miroir et avec une méthode (datas) permettant de regrouper les caractéristiques du miroir
    """
    def __init__(self, xc, yc, R, do, nature="concave") :
        
        #Centre, Rayon, Diamètre d'ouverture et nature
        self.xc=xc
        self.yc=yc
        self.R=R
        self.do = do
        self.nature = nature #Concave ou convexe
        
        #activation des 2 méthodes dès l'instanciation de l'objet
        self.coordonnées()
        self.datas()
        
    def coordonnées(self) :
        """
        Permet de calculer l'angle d'ouverture et les coordonnée pour tracer le miroir 
        """
        self.theta_max = 2*np.arcsin(self.do/(2*self.R)) #arcsin(theta) est def pour theta inclu dans -1,1 donc do compris dans -2R, 2R, ce qui est cohérent     
        if self.nature =="concave" :
            self.theta=np.linspace(-self.theta_max,self.theta_max,10000)
        elif self.nature=="convexe": 
            self.theta=np.linspace(-self.theta_max+2*np.pi,self.theta_max+2*np.pi,10000)
        
        #Coordonnées permettant de tracer le miroir
        self.x_miroir=self.R*np.cos(self.theta/2) + self.xc
        self.y_miroir=self.R*np.sin(self.theta/2) + self.yc
    
    def datas(self) :
        return self.xc, self.yc, self.R, self.do, self.x_miroir, self.y_miroir, self.nature
        
        

class rayon:
    """
    création d'un objet rayon ayant pour attributs les coordonnées de N (point d'inetrsection du rayon avec le miroir) et M (deuxième extrémité du rayon réfléchi)
    """
    def __init__(self, xp, yp, alpha, datas_miroir) :
        
        #Rayon incident : coordonnées du point de départ et angle formé par rapport à l'axe optique
        self.xp=xp 
        self.yp=yp
        self.alpha=alpha
        
        #récupération de toutes les données concernant le miroir utilisé
        self.xc, self.yc, self.R, self.do, self.x_miroir, self.y_miroir, self.nature = datas_miroir

        #activations des 2 méthodes dès l'instanciation de l'objet
        self.intersection()
        self.reflexion()
        
    def intersection(self):
        """
        Permet de calculer le point d'inetersection du miroir avec le rayon incident (point N)
        """
        
        #Calcul des coordonnées du point d'intersection du rayon incident avec le cercle portant le miroir
        self.a = 1+np.tan(self.alpha)**2
        self.b = -2*self.xc-2*self.xp*np.tan(self.alpha)**2 + 2*np.tan(self.alpha)*self.yp-2*self.yc*np.tan(self.alpha)
        self.c = self.xc**2 + (self.xp*np.tan(self.alpha))**2 - 2*self.xp*np.tan(self.alpha)*(self.yp-self.yc)+(self.yp-self.yc)**2-self.R**2
       
        self.delta = self.b**2 - 4*self.a*self.c
            
       #Conditions sur la nature du miroir 
        if self.nature =="concave" :
            self.xN = ( - self.b + np.sqrt(self.delta))/(2*self.a) 
        elif self.nature == "convexe" :
            self.xN = ( - self.b - np.sqrt(self.delta))/(2*self.a)
                
        #si le rayon ne touche pas le miroir
        if min(self.x_miroir)>self.xN or self.xN >max(self.x_miroir) or self.delta<0  :
            self.xN=10 #le rayon continu vers un point extérieur à la figure tracée

        self.yN = (self.xN-self.xp)*np.tan(self.alpha)+self.yp

        
    def reflexion(self):
        """
        Permet de calculer les coordonnées xM et yM du point d'arrivée du rayon réfléchi
        """
       
        #expression de l'angle formé par le rayon réfléchi avec l'axe optique
        self.betha =  np.arctan((self.yN-self.yc)/(self.xN-self.xc))
        self.lam= -np.pi + 2*self.betha - self.alpha
        
        # Définition du signe de xM en fonction de la valeur lambda :
        if -np.pi/2<self.lam <np.pi/2 or -5*np.pi/2<self.lam <-3*np.pi/2 or 3*np.pi/2<self.lam <5*np.pi/2:
            self.xM=10
        else :self.xM=-10
            
        self.yM = (self.xM - self.xN)*np.tan(self.lam) +self.yN
        
        #si le rayon ne touche pas le miroir, les coordonnées du point M sont les mêmes que ceux de N afin d'éviter le tracé d'un rayon réfléchi.
        if self.delta<0 or min(self.x_miroir)>=self.xN or self.xN >=max(self.x_miroir) :
            self.xM=self.xN
            self.yM=self.yN




def N_rayons(nombrederayons, nature="parallèles", alpha=0, d=1, xp=-3, yp=2, mdatas=miroir(2,0,3,4, "concave").datas()) :
    """
    Parameters
    ----------
    nombrederayons : integer
        Nombre de rayons générés
        
    nature : string, optional 
        rayons parallèles ou pas (parallèle par défaut)
        
    alpha : float, optional (The default is 0.)
        angle formé entre le rayon incident et l'axe optique si nature == parallèles
        angle d'ouverture si nature != parallèles
        
        
    d : float, optional
        distance maximale entre les rayons. (The default is 1.)
        
    xp : float, optional
        coordonné d'origine des rayons incidents suivant x. (The default is -3.)
        
    yp : float, optional
        coordonné moyen des rayons incidents suivant y. (The default is 2.)
        
    mdatas : optional
        datas du miroir. (The default is miroir(2,0,3,4, "concave").datas().)

    Returns
    -------
    rayons : list
        liste contenant les N rayons générés.

    """
    
    rayons=[]
    ouverture_angulaire = np.linspace(-alpha/2, alpha/2, nombrederayons)
    
    d=np.arange(-d/2, d/2, d/nombrederayons)
    for i in range(nombrederayons) :
        if nature=="parallèles":
            r=rayon(xp, yp+d[i], alpha, mdatas)
        else : 
            r=rayon(xp, yp+d[i], ouverture_angulaire[i], mdatas)

        rayons.append(r)
    return rayons


N=5

#instanciation de N rayons incidents et du miroir
rayons = N_rayons(N, "_")
m = miroir(2,0,3,4, "concave")


#Figure
#-------

fig , ax = plt.subplots(figsize=(15,8))
plt.subplots_adjust(left=0.4)
ax.set_aspect('equal') #graph orthonormé

#Création de 2 listes de plots (rayons incidents et réfléchis)
lignesr=[]
lignesi=[]
for i in range(len(rayons)) :
    ligner, = ax.plot([rayons[i].xM, rayons[i].xN],[rayons[i].yM,rayons[i].yN], "b",  linewidth=2)
    lignei, = ax.plot([rayons[i].xp, rayons[i].xN],[rayons[i].yp,rayons[i].yN], "r", linewidth=2)
    lignesr.append(ligner) 
    lignesi.append(lignei) 
    
lignem, = ax.plot(m.x_miroir,m.y_miroir,"k",linewidth=6, label ="miroir" )
lignec, = ax.plot(m.xc,m.yc, "go")
ax.plot([0,0],[0,0], "b", label='rayon réfléchi', linewidth=2) #pour que une seule légende soit affichée quelque soit le nombre de rayons
ax.plot([0,0],[0,0], "r", label='rayon incident', linewidth=2)
ax.set_ylabel("y")
ax.set_xlabel("x")
ax.grid()
ax.legend(fontsize=13)
ax.set_xlim(-6,6)
ax.set_ylim(-6,6)
ax.text(-13, -1.4, "Miroir",fontweight='bold', fontsize=18)
ax.text(-14.5, 4.1, "Rayons incidents",fontweight='bold', fontsize=18)

plt.show()
        

#Widgets
#--------

# GLISSIERE de alpha
axalpha = plt.axes([0.1, 0.7, 0.25, 0.04], facecolor='seashell') 
salpha = Slider(axalpha, r'$\alpha$', -np.pi/2, np.pi/2, valinit=0, color="pink")

# GLISSIERE de xp
axxp = plt.axes([0.1, 0.65, 0.25, 0.04], facecolor='seashell') 
sxp = Slider(axxp, r'$x_0$', -5, 0, valinit=-3, color="pink")

# GLISSIERE de yp
axyp = plt.axes([0.1, 0.6, 0.25, 0.04], facecolor='seashell') 
syp = Slider(axyp, r'$y_{moy}$', -m.do/2-1, m.do/2+1, valinit=2, color="pink")

# GLISSIERE de d
axd = plt.axes([0.1, 0.55, 0.25, 0.04], facecolor='seashell') 
sd = Slider(axd, 'distance max\n entre rayons', 0.01, 6, valinit=1, color="pink")

# GLISSIERE de rayons incidents parallèle ou ouverture angulaire
axnat = plt.axes([0.2, 0.5, 0.05, 0.04], facecolor='seashell') 
snat = Slider(axnat, r"parallèles / ouverture angulaire fct($\alpha$)", -1, 1, valinit=0, color="pink")

# GLISSIERE de do
axdo = plt.axes([0.1, 0.35, 0.25, 0.04], facecolor='seashell') 
sdo = Slider(axdo, "diamètre\nd'ouverture", 1, 6, valinit=4, color="pink")

# GLISSIERE de R
axR = plt.axes([0.1, 0.3, 0.25, 0.04], facecolor='seashell') 
sR = Slider(axR, "rayon", 3, 6, valinit=3, color="pink")

# GLISSIERE de xc
axxc = plt.axes([0.1, 0.25, 0.25, 0.04], facecolor='seashell') 
sxc = Slider(axxc, r"$x_{centre}$", -3, 6, valinit=2, color="pink")

# GLISSIERE de concave/convexe
axconc = plt.axes([0.1, 0.2, 0.05, 0.04], facecolor='seashell') 
sconc = Slider(axconc, "concave / convexe", -1, 1, valinit=0, color="pink")

#Fonction mettant à jour la figure en fonction des valeurs des glissières
def miseAjour(val):
    alpha = salpha.val 
    xp=sxp.val
    yp=syp.val
    d=sd.val
    do = sdo.val
    xc=sxc.val
    R=sR.val
    conc=sconc.val
    nat=snat.val
    
    if conc<=0 : 
        nature="concave"
    else : nature ="convexe"
    
    if nat<=0 : 
        nat="parallèles"
    else : 
        nat ="_"

    
    #on instancie un nouveau miroir et plusieurs nouveaux rayons avec les nouvelles valeurs
    m=miroir(xc,0,R,do, nature)
    rayons = N_rayons(N, nat, alpha, d, xp, yp, m.datas())

    #on modifie le miroir et les rayons
    for i in range(len(rayons)) :
        lignesi[i].set_data([rayons[i].xp,rayons[i].xN],[rayons[i].yp,rayons[i].yN]) # on met à jour le trajet du rayon incident
        lignesr[i].set_data([rayons[i].xM,rayons[i].xN],[rayons[i].yM,rayons[i].yN])# on met à jour le trajet du rayon réfléchi
    lignem.set_data(m.x_miroir,m.y_miroir)
    lignec.set_data(m.xc,m.yc)

# on attribue la fonction précédente à une modification de la valeur de la glissière
salpha.on_changed(miseAjour)
sxp.on_changed(miseAjour)
syp.on_changed(miseAjour)
sd.on_changed(miseAjour)
sdo.on_changed(miseAjour)
sconc.on_changed(miseAjour)
sxc.on_changed(miseAjour)
sR.on_changed(miseAjour)
snat.on_changed(miseAjour)

# BOUTON 'Remise à zéro'
resetax = plt.axes([0.18, 0.86, 0.10, 0.04])
bouton = Button(resetax, 'Remise à zéro',  hovercolor='seashell',color='pink')

def miseAzero(event):
    salpha.reset()  
    sxp.reset()
    syp.reset()
    sd.reset() 
    sconc.reset()
    sxc.reset()
    sR.reset()
    snat.reset()

# on attribue la fonction précédente à un clic sur le bouton
bouton.on_clicked(miseAzero)
