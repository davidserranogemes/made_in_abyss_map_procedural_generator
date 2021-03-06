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


n_segments = 4
max_amplitude=round(n_dots/10)
min_amplitude=round(n_dots/4)

external_list_first_point,external_list_second_point,internal_list_first_point,internal_list_second_point = bm.get_n_segment_break_points(X,Y,Xi,Yi,min_amplitude,max_amplitude,n_segments,100)

 
for i in range(len(external_list_first_point)):
    plt.plot([X[external_list_first_point[i]],Xi[internal_list_first_point[i]]],[Y[external_list_first_point[i]],Yi[internal_list_first_point[i]]],label='linear')
    plt.plot([X[external_list_second_point[i]],Xi[internal_list_second_point[i]]],[Y[external_list_second_point[i]],Yi[internal_list_second_point[i]]],label='linear')
 
plt.show()

"""
br_point_ex1 = external_list_first_point[0]
br_point_ex2 = external_list_second_point[0]
br_point_in1 = internal_list_first_point[0]
br_point_in2 =internal_list_second_point[0]
"""

section_list, real_n_segment = bm.get_all_section_for_height(X,Xi,Y,Yi,min_amplitude, max_amplitude,n_segments,n_tries=100)


for i in range(real_n_segment):
    X_values,Y_values,Z_values = section_list[i].get_section_points()
    
    plt.plot(X_values,Y_values)

plt.show()






x,y,z = section_list[0].get_section_points()


import matplotlib.tri as tri
#https://matplotlib.org/3.1.3/gallery/mplot3d/trisurf3d_2.html




triang = tri.Triangulation(x, y)



fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tcf = ax1.tricontourf(triang, z)
#fig1.colorbar(tcf)
ax1.tricontour(triang, z, colors='k')
ax1.set_title('Contour plot of section of layer')