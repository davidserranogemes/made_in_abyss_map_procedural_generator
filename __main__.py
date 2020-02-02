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

plt.plot(range(len(fitness)),fitness, label = 'linear')

plt.show()

plt.plot(X,Y, label='linear')

plt.show()