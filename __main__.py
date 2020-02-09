# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:59:58 2020

@author: david
"""

import matplotlib.pyplot as plt 

import base_math as bm

radius = 10
n_dots = 150
n_iter = 200
gain = 10

n_changes = 10000


X,Y,fitness = bm.generate_border(radius,n_dots,n_iter,gain, n_changes, False)

#plt.plot(range(len(fitness)),fitness, label = 'linear')

#plt.show()

plt.plot(X,Y, label='linear')

#plt.show()


Xi,Yi, fitness_i = bm.generate_border(radius/2,n_dots-50,n_iter, gain/2, n_changes,False)

plt.plot(Xi,Yi, label='linear')



br_point_ex1,br_point_ex2, br_point_in1,br_point_in2 = bm.segment_get_break_points(X,Y,Xi,Yi,round(n_dots/4),round(n_dots/10))


plt.plot([X[br_point_ex1],Xi[br_point_in1]],[Y[br_point_ex1],Yi[br_point_in1]], label='linear')
plt.plot([X[br_point_ex2],Xi[br_point_in2]],[Y[br_point_ex2],Yi[br_point_in2]], label='linear')

plt.show()
