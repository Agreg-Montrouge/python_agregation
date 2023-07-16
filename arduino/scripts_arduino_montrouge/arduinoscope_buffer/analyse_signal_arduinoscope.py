import numpy as np

import matplotlib.pyplot as plt

from scipy.signal.windows import flattop


t = [] # le temps (en us)
u = [] # la tension (en V0

f = open("donnees.txt", "r")
for i in range(250):
	l = f.readline()
	t.append(int(l.split('\t')[0]))
	u.append(int(l.split('\t')[1]))


t = np.array(t, dtype=float)
u = np.array(u, dtype = float)

t -= t[0] # On enleve le temps initial (pas de signification physique)
u *= 5 / 1023 # on transforme la tension en volts

deltat = np.mean(t[1:] - t[:-1]) # intervalle moyen entre les mesures (en us)
facqu = 1/deltat * 1000000 # frequence d'acquisition (en Hz)

print(f'Intervalle moyen entre les mesures = {deltat} us')
print(f'Frequence d\'acquisition = {facqu} Hz')

u_pourfft = u.copy()
u_pourfft -= np.mean(u_pourfft) # pour enlever l'offset
u_pourfft *= flattop(len(u_pourfft)) # fenetrage pour la FFT

f = np.fft.rfftfreq(len(t), d = deltat/1000000) # les frequences en Hz
u_chapeau = np.fft.rfft(u_pourfft) # la TF de la tension


plt.figure(1)
plt.plot(t, u)

ax = plt.gca()
ax.set_xlabel('Temps (us)')
ax.set_ylabel('Tension u (V)')
ax.set_title('Signal lu par la carte Arduino')
plt.show()


plt.figure(2)
plt.plot(f[1:], np.abs(u_chapeau)[1:]**2)
plt.yscale('log') # pour mettre l'axe des y en log
# plt.xscale('log') # pour mettre l'axe des x en log

ax = plt.gca()
ax.set_xlabel('Frequence (Hz)')
ax.set_ylabel('Densite spectrale de puissance |û|² (V²/Hz)')
ax.set_title('Spectre de puissance du signal')
plt.show()


