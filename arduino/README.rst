==========================
Programmes Arduino
==========================

* Le dossier '''documentation_arduino_montrouge''' contient toute la documentation sur les composants disponibles, notamment concernant le télémètre ultrasonore, l'accéléromètre et le baromètre.
* Le dossier '''bibliotheques_arduino_montrouge''' contient les bibliothèques fournies avec les capteurs. Notamment, la bibliothèque LIS3DHTR contenue dans
"Seeed_Arduino_LIS3DHTR-master.zip" est nécessaire pour faire fonctionner
l’accéléromètre.
* Le dossier '''scripts_arduino_montrouge''' contient les différents scripts arduino fournis par le centre de Montrouge.


Liste des scripts Arduino
================================

Mesures de charges de condensateurs
* charge_condensateur_affichage : Affiche la tension au cours du temps pendant la charge d'un condensateur.
* charge_condensateur_mesure : Fait plusieurs mesures du temps de charge d’un
condensateur et affiche le temps de charge moyen.

Mise en évidence de la résolution temporelle de l’arduino
* arduinoscope_buffer : Enregistre des valeurs de tension en fonction du temps puis les affiche. Le résultat peut être analysé à l’aide du script python analyse_signal_arduinoscope.py.
* arduinoscope_live : Communique en direct les valeurs de la tension. Permet d’enregistrer plus de points, au prix d’une plus faible fréquence d’acquisition.

Mesures de pressions
* pression_montrouge: Utilise le capteur de pression. Mesure la pression au niveau du
capteur.

Mesures de distances au télémètre ultrasonore
* ultrasons_montrouge: Utilise le télémètre ultrasonore. Permet de donner le temps d’aller-retour d’un burst d’ultrasons à 40 kHz, et d’en déduire une distance.

Mesures d’accélérations
* acceleration_ressort_montrouge : Utilise l'accéléromètre. Il permet d'afficher un graphe des accélérations en fonction du temps, ou d'en enregistrer des valeurs.
* acceleration_ressort_moyennage_montronge : Affiche une accélération moyennée pour
des courbes moins bruitées, il permet de mesurer des accélérations plus faibles.

Informations
============

Auteurs et autrices : Prépa agreg de Montrouge

Adresse : Département de physique de l'École Normale Superieure
		24 rue Lhomond
		75005 Paris

Licence : Cette oeuvre, création, site ou texte est sous licence Creative Commons Attribution - Pas d'Utilisation Commerciale 4.0 International. Pour accéder à une copie de cette licence, merci de vous rendre à l'adresse suivante http://creativecommons.org/licenses/by-nc/4.0/ ou envoyez un courrier à Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.

