# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------------------
#Dados solver 1, 10000 células:
arq1 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_10000/data_shockTube_10000.csv','r')
magU_sol1_10000,p_sol1_10000,rho_sol1_10000,x_sol1_10000 = np.loadtxt(arq1, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq1.close()


#Dados solver 2, 10000 células:
arq2 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_fvSol_10000/data_shockTube_fvSol_10000.csv','r')
magU_sol2_10000,p_sol2_10000,rho_sol2_10000,x_sol2_10000 = np.loadtxt(arq2, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq2.close()


#Dados solver 1, 1000 células:
arq3 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_1000/data_shockTube_1000.csv','r')
magU_sol1_1000,p_sol1_1000,rho_sol1_1000,x_sol1_1000 = np.loadtxt(arq3, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq3.close()


#Dados solver 2, 1000 células:
arq4 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_fvSol_1000/data_shockTube_fvSol_1000.csv','r')
magU_sol2_1000,p_sol2_1000,rho_sol2_1000,x_sol2_1000 = np.loadtxt(arq4, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq4.close()


#Dados solver 1, 100 células:
arq5 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_100/data_shockTube_100.csv','r')
magU_sol1_100,p_sol1_100,rho_sol1_100,x_sol1_100 = np.loadtxt(arq5, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq5.close()


#Dados solver 2, 100 células:
arq6 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/PimpleFoam/shockTube_fvSol_100/data_shockTube_fvSol_100.csv','r')
magU_sol2_100,p_sol2_100,rho_sol2_100,x_sol2_100 = np.loadtxt(arq6, delimiter=',', dtype='float', comments='#', usecols=(4, 5, 6, 9), unpack=True, skiprows=1)
arq6.close()

#Dados solução anlítica:
arq7 = open('/home/gabrielmarconcini/Documentos/TCC/PTCC/ShockTube/SodShockTube/shockTube_python/sod-shocktube/examples/dados.csv','r')
x_py,p_py,rho_py,magU_py = np.loadtxt(arq7, delimiter=',', dtype='float', comments='#', usecols=(0, 1, 2, 3), unpack=True, skiprows=1)
arq7.close()

#-------------------------------------------------------
#rhoCentralFoam x rhoPimpleFoam:
plt.figure(1)
plt.plot(x_sol2_10000, p_sol2_10000, label='solver 2')
plt.plot(x_sol1_10000, p_sol1_10000, label='solver 1')
plt.plot(x_py, p_py, label='Analítica')
plt.title(r'10000 células')
plt.ylabel(r'Pressão [$Pa$]')
plt.xlabel('Comprimento [$m$]')

plt.grid()
plt.legend()

plt.figure(2)
plt.plot(x_sol2_1000, p_sol2_1000, label='solver 2')
plt.plot(x_sol1_1000, p_sol1_1000, label='solver 1')
plt.plot(x_py, p_py, label='Analítica')
plt.title(r'1000 células')
plt.ylabel(r'Pressão [$Pa$]')
plt.xlabel('Comprimento [$m$]')

plt.grid()
plt.legend()

plt.figure(3)
plt.plot(x_sol2_100, p_sol2_100, label='solver 2')
plt.plot(x_sol1_100, p_sol1_100, label='solver 1')
plt.plot(x_py, p_py, label='Analítica')
plt.title(r'100 células')
plt.ylabel(r'Pressão [$Pa$]')
plt.xlabel('Comprimento [$m$]')

plt.grid()
plt.legend()

plt.show()
