# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:59:58 2020

@author: david
"""

import matplotlib.pyplot as plt 

import base_math as bm

radius = 10
n_dots = 400
n_iter = 1000
gain = 13

n_changes = 10000

X,Y = bm.circle(radius,n_dots)

plt.plot(X,Y, label='linear')

plt.show()


X,Y = bm.procedural_generation(radius,n_dots,X,Y,n_iter,gain)

X,Y,fitness = bm.reorder_points(X,Y,n_changes, debug =True)

plt.plot(range(n_changes),fitness, label = 'linear')

plt.show()