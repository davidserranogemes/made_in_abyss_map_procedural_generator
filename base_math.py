# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:25:07 2020

@author: david
"""
import numpy as np

import matplotlib.pyplot as plt 



#GEnerate n poins of a r radius circle.
def circle(r,n):
    #Generate the arrays
    X = np.zeros((n))
    Y = np.zeros((n))


    #Generate n random numbers
    for i in range(0,n):
        phase=np.random.rand(1)[0]*np.pi*2
        X[i]=r*np.math.cos(phase)
        Y[i]=r*np.math.sin(phase)
        
 
    
    
    #Order the dots sequentially so when ploting the lines it appears a circle
    X_y_pos = X[Y>=0]
    X_y_neg = X[Y<0]
    
    Y_y_pos = Y[Y>=0]
    Y_y_neg = Y[Y<0]
    
    x_pos_y_index = np.argsort(X_y_pos)
    x_neg_y_index = np.argsort(-X_y_neg)
   
    X_final=np.concatenate((np.take_along_axis(X_y_pos,x_pos_y_index,axis=0),np.take_along_axis(X_y_neg,x_neg_y_index,axis=0)))
    Y_final=np.concatenate((np.take_along_axis(Y_y_pos,x_pos_y_index,axis=0),np.take_along_axis(Y_y_neg,x_neg_y_index,axis=0)))
    
    
    #Append at the end the last dot so its a complete circle.
    X_final= np.append(X_final,X_final[0])
    Y_final= np.append(Y_final,Y_final[0])
    

    return X_final, Y_final



#Adds noise to the points in the circle.
def procedural_generation(r,n,X,Y,n_iter,gain,debug):
    max_distance = n/(2*r)
    i=0
    
    pivot=np.random.randint(2,n-2)
    runner=pivot + pow(-1,np.random.randint(1,2)) * np.random.randint(1,max_distance)
    while(n_iter>i):
        #Modify the pivot and the runner
        X[pivot] = X[pivot] + (0.5 -np.random.rand()) * r/n * gain
        Y[pivot] = Y[pivot] + (0.5 -np.random.rand()) * r/n * gain
        
        X[runner] = X[runner] + (0.5 -np.random.rand()) * r/n * gain
        Y[runner] = Y[runner] + (0.5 -np.random.rand()) * r/n * gain
        
        if pivot == runner or pivot == (runner +1) or pivot == (runner-1):
            pivot=np.random.randint(2,n-2)
            runner=pivot + pow(-1,np.random.randint(1,2)) * np.random.randint(1,max_distance)
        else:
            if pivot > runner:
                pivot = pivot -1
                runner = runner +1
            else:
                pivot = pivot +1
                runner = runner -1
        
        if pivot ==0:
            pivot = 1
        if pivot == n-1:
            pivot =pivot -1
        
        if runner ==0:
            runner = 1
        if runner == n-1:
            runner =runner -1
        
        
        
        i=i+1
        if debug:
            print('Nº iter:',i)
            plt.plot(X,Y, label='linear')
            plt.show()
            
    return X,Y
            
def simplified_euclidean_distance(x1,x2,y1,y2):
    return (x1-x2)**2+(y1-y2)**2         


#Apply the comercy problem solution with a local greedy search to reorder the points.
def reorder_points(X,Y,n_changes,debug):
    i=0
    fitness=np.zeros(n_changes)
    for j in range(0,len(X)-1):
            fitness[i] = fitness[i] + simplified_euclidean_distance(X[j],X[j+1],Y[j],Y[j+1]) 
            
    j=1
    while i<n_changes-1 and j<len(X)-4:
                
        
            current_distance = simplified_euclidean_distance(X[j],X[j+1],Y[j],Y[j+1]) + simplified_euclidean_distance(X[j+2],X[j+3],Y[j+2],Y[j+3])  
            proposed_distance = simplified_euclidean_distance(X[j],X[j+2],Y[j],Y[j+2]) + simplified_euclidean_distance(X[j+1],X[j+3],Y[j+1],Y[j+3])  
            #print(current_distance,'  vs   ', proposed_distance)
            #print('i:',i,' j:',j,' len:',len(X),' n_chg:',n_changes)
            #print()
            if proposed_distance < current_distance:
                fitness[i+1] = fitness[i] - current_distance + proposed_distance
            
                X[j+1],X[j+2] = X[j+2],X[j+1]
                Y[j+1],Y[j+2] = Y[j+2],Y[j+1]
                
               
                
                if debug:
                    print(current_distance,'  vs   ', proposed_distance)
                    print('i:',i,' j:',j,' len:',len(X),' n_chg:',n_changes)
                    print()
                    
                    plt.plot(X,Y, label='linear')
                    
                    plt.show()
                    print('Fitness:',fitness[i])
                    print(i,'/',n_changes)
                    #input("Press Enter to continue...")
                i=i+1
                j=0
            
            j=j+1

        
    fitness = fitness[fitness>0]
    
    return X,Y,fitness    
        


def generate_border(radius = 10,n_dots = 100,n_iter = 50,gain = 13,n_changes = 10000, debug = False):
    X,Y = circle(radius,n_dots)
    
    X,Y = procedural_generation(radius,n_dots,X,Y,n_iter,gain,debug)
    
    X,Y,fitness = reorder_points(X,Y,n_changes, debug =debug)
    
    if debug:
        plt.plot(range(len(fitness)),fitness, label = 'linear')
        
        plt.show()
        
        plt.plot(X,Y, label='linear')
        
        plt.show()
    
    return X,Y,fitness

        
            
        
    
    
    
    

