# -*- coding: utf-8 -*-
#

import numpy as np
import matplotlib.pyplot as plt


#Coleta dos dados:

#Dados OpenFoam malha com 100 células:
arq1 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_100/data_shockTube_100.csv','r')

magU_100,p_100,rho_100,x_100 = np.loadtxt(arq1, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)

arq1.close()


#Dados solução anlítica:
arq2 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/shockTube_python/sod-shocktube/examples/dados.csv','r')

x_py,p_py,rho_py,magU_py = np.loadtxt(arq2, delimiter=',', dtype='float', comments='#', usecols=(0, 1, 2, 3), unpack=True, skiprows=1)

arq2.close()


#Dados OpenFoam malha com 1000 células:
arq3 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_1000/data_shockTube_1000.csv','r')

magU_1000,p_1000,rho_1000,x_1000 = np.loadtxt(arq3, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)

arq3.close()


#Dados OpenFoam malha com 10000 células:
arq4 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_10000/data_shockTube_10000.csv','r')

magU_10000,p_10000,rho_10000,x_10000 = np.loadtxt(arq4, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)

arq4.close()


#-------------------------------------------------------------------#
#Gráficos:

#Pressão:
plt.figure(1)
plt.plot(x_100, p_100, label='OpenFoam malha 100')
plt.plot(x_1000, p_1000, label='OpenFoam malha 1000')
plt.plot(x_10000, p_10000, label='OpenFoam malha 10000')
plt.plot(x_py, p_py, label='Analítica')
plt.title(r'Pressão no Tubo de Choque')
plt.ylabel('Pressão [$Pa$]')
plt.xlabel('Comprimento [$m$]')

plt.grid()
plt.legend()


#Magnitude da Velocidade:
plt.figure(2)
plt.plot(x_100, magU_100, label='OpenFoam malha 100')
plt.plot(x_1000, magU_1000, label='OpenFoam malha 1000')
plt.plot(x_10000, magU_10000, label='OpenFoam malha 10000')
plt.plot(x_py, magU_py, label='Analítica')
plt.title(r'Velocidade no Tubo de Choque')
plt.ylabel(r'Velocidade [$m/s^2$]')
plt.xlabel('Comprimento [$m$]')

plt.grid()
plt.legend()


#Densidade:
plt.figure(3)
plt.plot(x_100, rho_100, label='OpenFoam malha 100')
plt.plot(x_1000, rho_1000, label='OpenFoam malha 1000')
plt.plot(x_10000, rho_10000, label='OpenFoam malha 10000')
plt.plot(x_py, rho_py, label='Analítica')
plt.title(r'Densidade no Tubo de Choque')
plt.ylabel(r'Densidade [$kg/m^3$]')
plt.xlabel('Comprimento [$m$]')

plt.grid()
plt.legend()


plt.show()
