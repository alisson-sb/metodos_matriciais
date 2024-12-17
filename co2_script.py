import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import linalg
import pandas as pd
# Ler arquivo txt
file = pd.read_table('co2_maunaloa.txt', sep=" ",header=None) 

tempo = file[1]
b = file[4]
fig = plt.plot(file[3],file[4])
plt.xlabel("Tempo")
plt.ylabel("CO2 médio [ppm]")



#variacao de quantidade de c02 entre o ultimo e primeiro ano 

amplitude=(max(file[4])-min(file[4]))/65

# Variação nos últimos 50 anos
# Primeiro ano será 1973 e ultimo ano será 2023

Var_1973 = file.loc[(file[1] == 1973) & (file[2] == 8)].values[0,4]
Var_2023 = file.loc[(file[1] == 2023) & (file[2] == 8)].values[0,4]
Var_50 = (Var_2023 - Var_1973)/50

#Montar matriz A de uns para realizar o cálculo de tendência 

a = np.array([np.ones(len(tempo)), tempo])
A=np.transpose(a)

x, resid, rank,sigma =  np.linalg.lstsq(A,b)
mod = np.dot(A,x)

# Plotar gráfico com linha de tendência 
plt.plot(tempo,b, label =  "Concentração de C02")
plt.plot(tempo,mod, label = 'Linha de Tendência ')
plt.ylabel('Concentração de CO2')
plt.xlabel('Tempo')
plt.grid(True)
plt.legend()
plt.savefig('CO2_CONC_TREND.png')
plt.show()
plt.close()

# Calcular C02 sem tendência linear 
CO2_st = b - mod
plt.plot(tempo,CO2_st, label =  "Concentração de C02 sem tendência")
plt.ylabel('Concentração de CO2')
plt.xlabel('Tempo')
plt.grid(True)
plt.legend()
plt.savefig('CO2_CONC_SEM_TREND.png')
plt.show()
plt.close()

# Calcular segunda curva de tendência
A2 = np.array([np.ones(len(tempo)),tempo,tempo**2])
A2 = np.transpose(A2)

# Resolver problema de mínimos quadrados
x2, resid, rank, sigma = linalg.lstsq(A2,b)
mod2 = np.dot(A2,x2)

# Plotar curvas e série temporal
plt.plot(tempo,b, color = 'black', label =  "Concentração de C02")
plt.plot(tempo,mod2, color='red', label = 'Curva de Tendência ')
plt.ylabel('Concentração de CO2')
plt.xlabel('Tempo')
plt.grid(True)
plt.legend()
plt.savefig('CO2_CONC_TREND2.png')
plt.show()
plt.close()

# Calcular C02 sem curva de tendência 
CO2_st2 = b - mod2
plt.plot(tempo,CO2_st2, label =  "Concentração de C02 sem curva de tendência")
plt.ylabel('Concentração de CO2')
plt.xlabel('Tempo')
plt.grid(True)
plt.legend()
plt.savefig('CO2_CONC_SEM_TREND2.png')
plt.show()
plt.close()

# Construção do modelo harmônico
T = 1/365.25
w = 2*np.pi*T

# Matriz A
A3 = np.array([np.ones(len(tempo)),np.sin(w*tempo),np.cos(w*tempo),np.sin(2*w*tempo),np.cos(2*w*tempo)])
A3 = np.transpose(A3)

# Cálculo dos mínimos quadrados aplicado ao CO2 sem tendência
x3, resid, rank, sigma = linalg.lstsq(A3,CO2_st2)
mod3 = np.dot(A3,x3)

#Plotar gráfico de CO2 sem tendencia com o modelo harmonico
plt.plot(tempo,CO2_st2, label = "Concentração de CO2 sem curva de tendência")
plt.plot(tempo,mod3, label = "Modelo harmônico de tendência")
plt.ylabel('Concentração de CO2')
plt.xlabel('Tempo')
plt.legend()
plt.grid(True)
plt.savefig('CONC_CO2_TREND3.png')
plt.show()

# Cálculo de CO2 sem tendência 
CO2_st3 = CO2_st2 - mod3
plt.plot(tempo,CO2_st3, label = "Concentração de CO2 sem curva de tendência")
plt.ylabel('Concentração de CO2')
plt.xlabel('Tempo')
plt.legend()
plt.grid(True)
plt.savefig('CONC_CO2_SEM_TREND3.png')
plt.show()
