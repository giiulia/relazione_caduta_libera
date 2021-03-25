import numpy as np
import math
from matplotlib import pyplot as plt

import dati
from strumenti_utili_v2 import *


x = dati.tempi
y = dati.altezze

s_t = np.array([
    deviazione(dati.tempo_caduta1, np.mean(dati.tempo_caduta1)),
    deviazione(dati.tempo_caduta2, np.mean(dati.tempo_caduta2)),
    deviazione(dati.tempo_caduta3, np.mean(dati.tempo_caduta3)),
    deviazione(dati.tempo_caduta4, np.mean(dati.tempo_caduta4)),
    deviazione(dati.tempo_caduta5, np.mean(dati.tempo_caduta5)),
    deviazione(dati.tempo_caduta6, np.mean(dati.tempo_caduta6))
])/np.sqrt(10) #divido ogni deviazione per la radice di N (misurazioni)

s_x = 2*dati.tempi*s_t 
s_y = np.array([
    deviazione(dati.h1, np.mean(dati.h1)),
    deviazione(dati.h2, np.mean(dati.h2)),
    deviazione(dati.h3, np.mean(dati.h3)),
    deviazione(dati.h4, np.mean(dati.h4)),
    deviazione(dati.h5, np.mean(dati.h5)),
    deviazione(dati.h6, np.mean(dati.h6))
])/np.sqrt(dati.h1.size)


#calcolo il coefficiente B
coefficiente_non_pesato = (6*sum(x*y) - sum(x)*sum(y))/(6*sum(np.power(x, 2)) - np.power(sum(x), 2))
s_y_eq = np.sqrt(s_y**2 + (coefficiente_non_pesato*s_x)**2)

pesi = 1/np.power(s_y_eq, 2)

delta = (sum(pesi*np.power(x, 2))*sum(pesi))-np.power(sum(pesi*x),2) 
coefficiente = ((sum(pesi)*sum(pesi*x*y))-(sum(pesi*x)*sum(pesi*y)))/delta

print("il coefficiente è: B={0:.3f}".format(coefficiente))

#calcolo l'intercetta A 
intercetta = ((sum(pesi*np.power(x,2))*sum(pesi*y))-(sum(pesi*x)*sum(pesi*x*y)))/delta

print("l'intercetta è: A={} dunque non posso trascurarla".format(intercetta))

#calcolo sigma intercetta
sigma_A = np.sqrt(sum(pesi*np.power(x, 2)))/math.sqrt(delta)
print("l'incertezza su A è: sigma_A={}".format(sigma_A))

#calcolo sigma coefficiente
sigma_B = np.sqrt(sum(pesi))/math.sqrt(delta)
print("l'incertezza su B è: sigma_B={}".format(sigma_B))

#calcolo sigma g con la propagazione degli errori e il valore di g
sigma_g = 2*sigma_B
print("incertezza su g: sigma_g={}".format(sigma_g))

g = 2*coefficiente
print('accelerazione di gravità: g = {0:.3f}±{1:.3f} '.format(g, sigma_g))


#retta interpolata
plt.errorbar(x, y, s_y_eq, fmt='o', ls='none', label='data')

plt.xlim(left=0)
plt.ylim(bottom=0)

xmin = 0
xmax = max(x)+0.1*(max(x)-min(x))

t = np.linspace(xmin,xmax) # stessa funzione ad alta densità
plt.plot(t,line(t,coefficiente, intercetta),label=r"$y = {0:.2f}x+{1:.2f}$".format(coefficiente, intercetta), color="darkOrange")
plt.plot(t,line(t,coefficiente, intercetta))
plt.legend() # aggiungo una legenda
#plt.savefig('computed_data/retta.pgf')
plt.savefig('computed_data/retta.png')
plt.show()
