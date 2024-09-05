#! /usr/bin/env python3
# -*- Encoding: utf-8 -*-
r"""Filtrage numérique

Description
-----------
Ce programme représente l'effet du filtrage numérique sur une sommes de fréquences. 

Informations
------------
Auteurs : Thoams Dupuis, Arnaud Raoux et la prépa agreg de Montrouge
Année de création : 2023
Version : 1
Version de Python : 3.11
Licence : Creative Commons Attribution - Pas d'utilisation Commerciale 4.0 International

Liste des modifications :
    * v 1.00 : 2023-07-16 Première version complète
"""

import numpy as np
from math import *
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20, 10]

f1 = 10
phi1 = np.pi/2
A1=1
f2 = 500
phi2 = np.pi/2
A2=1
t0 = 0
tfin = 1
Te = 0.00005
temps = np.arange(t0,tfin,Te)
entree = A1*np.cos(2*np.pi*f1*temps+phi1)+A2*np.cos(2*np.pi*f2*temps+phi2)

########################## Tracé initial ##########################################

t0fig1 = 0.
tfinfig1 = 0.07
f=plt.figure(1)
plt.plot(temps[int(t0fig1/Te):int(tfinfig1/Te)],entree[int(t0fig1/Te):int(tfinfig1/Te)],'r-',label="Entrée")
# plt.show()

######################## Filtrage passe bas ordre 1 et passe haut ordre 2 #############
##########################

fc1 = 100
sortie1 = np.zeros(len(entree))
sortie2 = np.zeros(len(entree))
for i in range(len(entree)-1):
    sortie1[i+1] = sortie1[i]+2*pi*fc1*Te*(entree[i]-sortie1[i])
    sortie2[i+1] = entree[i+1]-entree[i]+sortie2[i]*(1-2*pi*fc1*Te)

plt.plot(temps[int(t0fig1/Te):int(tfinfig1/Te)],sortie1[int(t0fig1/Te):int(tfinfig1/Te)],'b-',label="Passe bas ordre 1")
plt.plot(temps[int(t0fig1/Te):int(tfinfig1/Te)],sortie2[int(t0fig1/Te):int(tfinfig1/Te)],'g-',label="Passe haut ordre 1")
plt.legend(fontsize="20")
plt.show()
