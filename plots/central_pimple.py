# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------------------
#Dados rhoCentralFoam 10000 células:
arq1 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/CentralFoam/shockTube_10000/data_shockTube_central_10000.csv','r')
magU_CF_10000,p_CF_10000,rho_CF_10000,x_CF_10000 = np.loadtxt(arq1, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq1.close()

#Dados rhoPimpleFoam 10000 células:
arq2 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_10000/data_shockTube_10000.csv','r')
magU_PF_10000,p_PF_10000,rho_PF_10000,x_PF_10000 = np.loadtxt(arq2, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq2.close()

#Dados rhoCentralFoam 1000 células:
arq3 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/CentralFoam/shockTube_1000/data_shockTube_central_1000.csv','r')
magU_CF_1000,p_CF_1000,rho_CF_1000,x_CF_1000 = np.loadtxt(arq3, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq3.close()

#Dados rhoPimpleFoam 1000 células:
arq4 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_1000/data_shockTube_1000.csv','r')
magU_PF_1000,p_PF_1000,rho_PF_1000,x_PF_1000 = np.loadtxt(arq4, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq4.close()

#Dados rhoCentralFoam 100 células:
arq5 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/CentralFoam/shockTube_100/data_shockTube_central_100.csv','r')
magU_CF_100,p_CF_100,rho_CF_100,x_CF_100 = np.loadtxt(arq5, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq5.close()

#Dados rhoPimpleFoam 100 células:
arq6 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_100/data_shockTube_100.csv','r')
magU_PF_100,p_PF_100,rho_PF_100,x_PF_100 = np.loadtxt(arq6, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq6.close()

#Dados rhoPimpleFoam 100 células:
#Dados solução anlítica:
arq7 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/shockTube_python/sod-shocktube/examples/dados.csv','r')
x_py,p_py,rho_py,magU_py = np.loadtxt(arq7, delimiter=',', dtype='float', comments='#', usecols=(0, 1, 2, 3), unpack=True, skiprows=1)
arq7.close()

#-------------------------------------------------------
#rhoCentralFoam x rhoPimpleFoam:
plt.figure(1)
plt.plot(x_CF_10000, p_CF_10000, label='rhoCentralFoam')
plt.plot(x_PF_10000, p_PF_10000, label='rhoPimpleFoam')
plt.plot(x_py, p_py, label='Analítica')
plt.title(r'10000 células')
plt.ylabel(r'Pressão [$Pa$]')
plt.xlabel('Comprimento [$m$]')

plt.grid()
plt.legend()

plt.figure(2)
plt.plot(x_CF_1000, p_CF_1000, label='rhoCentralFoam')
plt.plot(x_PF_1000, p_PF_1000, label='rhoPimpleFoam')
plt.plot(x_py, p_py, label='Analítica')
plt.title(r'1000 células')
plt.ylabel(r'Pressão [$Pa$]')
plt.xlabel('Comprimento [$m$]')

plt.grid()
plt.legend()

plt.figure(3)
plt.plot(x_CF_100, p_CF_100, label='rhoCentralFoam')
plt.plot(x_PF_100, p_PF_100, label='rhoPimpleFoam')
plt.plot(x_py, p_py, label='Analítica')
plt.title(r'100 células')
plt.ylabel(r'Pressão [$Pa$]')
plt.xlabel('Comprimento [$m$]')

plt.grid()
plt.legend()

plt.show()
