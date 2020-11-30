#!/usr/bin/python
# -*- coding: utf-8 -*- 
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
#plt.rc('xtick',labelsize=6)
#	plt.rc('ytick',labelsize=6)


#Caso SWHD
#Iteracion
x = np.array(np.arange(0,100))
#Fitness
z = np.array([4.19855118e-05,4.15367365e-03,8.25567245e-03,1.23482251e-02
,1.64446831e-02,2.05206966e-02,2.46069074e-02,2.86882877e-02
,3.27801704e-02,3.68586206e-02,4.09413314e-02,4.50399137e-02
,4.91215348e-02,5.32235169e-02,5.73348761e-02,6.14481044e-02
,6.55482483e-02,6.96367407e-02,7.37285805e-02,7.78206515e-02
,8.19071603e-02,8.59928203e-02,9.00815964e-02,9.41757822e-02
,9.82595825e-02,1.02345598e-01,1.06438270e-01,1.10523121e-01
,1.14655073e-01,1.18737667e-01,1.22826202e-01,1.26897752e-01
,1.30988958e-01,1.35078166e-01,1.39177802e-01,1.43266578e-01
,1.47344301e-01,1.51438072e-01,1.55537038e-01,1.59648087e-01
,1.63753066e-01,1.67844224e-01,1.71929111e-01,1.76036091e-01
,1.80148606e-01,1.84279127e-01,1.88372626e-01,1.92484238e-01
,1.96590230e-01,2.00737753e-01,2.04840162e-01,2.08936543e-01
,2.13022425e-01,2.17098720e-01,2.21182554e-01,2.25274143e-01
,2.29356232e-01,2.33447375e-01,2.37537696e-01,2.41633813e-01
,2.45710037e-01,2.49799771e-01,2.53884838e-01,2.57960389e-01
,2.62035561e-01,2.66127489e-01,2.70206826e-01,2.74285688e-01
,2.78364048e-01,2.82442894e-01,2.86530652e-01,2.90611508e-01
,2.94693916e-01,2.98784556e-01,3.02870572e-01,3.06946516e-01
,3.11034439e-01,3.15124240e-01,3.19205914e-01,3.23304334e-01
,3.27401440e-01,3.31496556e-01,3.35597479e-01,3.39691141e-01
,3.43776524e-01,3.47879660e-01,3.51962976e-01,3.56048312e-01
,3.60150945e-01,3.64241507e-01,3.68331501e-01,3.72413065e-01
,3.76501148e-01,3.80580750e-01,3.84670334e-01,3.88759108e-01
,3.92841773e-01,3.96939032e-01,4.01047847e-01,4.05157719e-01])
#Tiempo
y = np.array([22,4,7,9,11,14,18,21,25,29,32,37,40,42,43,46,49,55,60,62,66,69,72,75,76,77,80,82,85,88,91,94,96,98,102,104,107,110,111,113,117,119,120,122,126,128,130,131,134,136,136,137,140,141,143,145,148,151,152,154,156,159,161,164,167,169,170,171,173,175,177,180,180,183,183,183,186,188,189,190,191,195,196,198,200,201,203,206,210,211,214,215,219,219,222,224,227,229,231,234,
])

x, y = np.meshgrid(x, y)		
#z = z.reshape(x.shape)

finalZ = []

for i in range(0,100):
	finalZ.append(z)
	


fig = plt.figure()

#ax = fig.add_subplot(2, 2, 1, projection='3d')
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, np.array(finalZ), cmap=cm.coolwarm,
                       linewidth=0, antialiased=True, label="SWBest")


plt.xlabel(u"Iteración", fontsize=7)
plt.ylabel(u"Fitness", fontsize=7)                       
#fig.colorbar(surf, shrink=1,orientation='horizontal', aspect=20)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_title(u'Estrategias swbest', fontsize=8)


plt.show()
#plt.savefig("Generadosw50.png")
