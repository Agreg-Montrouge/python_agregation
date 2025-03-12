#! /usr/bin/env python3
# -*- Encoding: utf-8 -*-

r"""Équation implicite pour une poutre

Description
-----------
Ce programme permet de résoudre l'équation implicite reliant la fréquence
propre d'oscillation d'une poutre et son module d'Young'

Informations
------------
Auteurs : Arnaud Raoux et la prépa agreg de Montrouge
Année de création : 2025
Version : 1.0
Version de Python : 3.12
Licence : Creative Commons Attribution - Pas d'utilisation Commerciale 4.0 International

Liste des modifications :
    * v 1.0 : 2023-03-12 Première version complète
"""
import numpy as np
from scipy.optimize import brentq # Pour trouver les zeros d'une fonction

# =============================================================================
# --- Reference ------------------------------------------------
# =============================================================================

## EJP 37 (2016) 015001

# =============================================================================
# --- Définitions ------------------------------------------------
# =============================================================================

rho=9e3 # Masse volumique
e=8.2e-4 # épaisseur du réglet
L=0.2 # longueur du réglet

## Mesure de la première fréquence de résonance
freq1=13.12

# =============================================================================
# --- Fonctions intermediaires ------------------------------------------------
# =============================================================================

def eq_impl(x):
    """
    Fonction dont les zeros donnent les fréquences de résonance
    """
    return np.cos(x)+1/np.cosh(x)


# =============================================================================
# --- Fonction principal (main loop) ------------------------------------------
# =============================================================================

def main():
    N=1000

    x = np.linspace(0, 100, N)
    val = eq_impl(x) # Vecteur avec toutes les valeurs de la fonction eq_impl sur le tableau x
    all_zeroes=[] # Liste qui comprendra tous les zéros de la fonction sur l'intervalle x
    
    for i in np.arange(N-1):
        if val[i]*val[i+1]<0: # Si une valeur est >0 et l'autre <0, il y a un zéro au milieu
            zero = brentq(eq_impl, x[i], x[i+1])
            all_zeroes.append(zero) # On rajoute le zéro dans la liste
    
    young=4*np.pi**2/all_zeroes[0]**4*12*rho/e**2*freq1**2*L**4
    f2=young*e**2*all_zeroes[1]**4/(48*3.14**2*rho*L)
    f3=young*e**2*all_zeroes[2]**4/(48*3.14**2*rho*L)
    return young/1e9, f2,f3#, all_zeroes[0],all_zeroes[1]
    
print(main())

#input()



