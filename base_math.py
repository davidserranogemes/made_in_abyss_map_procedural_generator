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

        
            


def segment_get_break_points(X,Y,Xi,Yi,max_amplitude,min_amplitude):
    first_external_point = np.random.randint(1,len(X)-1)
    
    x_first_external_point = X[first_external_point]
    y_first_external_point = Y[first_external_point]
    
    distance_to_second_external = np.random.randint(min_amplitude,max_amplitude)
    
    second_external_point = (first_external_point+distance_to_second_external)%len(X)
    
    x_second_external_point = X[second_external_point]
    y_second_external_point = Y[second_external_point]

    
    #detect now near points
    
    distance_from_first_external_to_internals = np.zeros(len(Xi))
    
    for i in range(0,len(distance_from_first_external_to_internals)):
        x_first_internal_point  = Xi[i]
        y_first_internal_point  = Yi[i]
        distance_from_first_external_to_internals[i] = simplified_euclidean_distance(x_first_external_point,
                                                                                     x_first_internal_point,
                                                                                     y_first_external_point,
                                                                                     y_first_internal_point)
    
    candidates =np.argpartition(distance_from_first_external_to_internals,5)[0:5]
    first_internal_point = candidates[np.random.randint(0,5)]
    
    
    distance_from_second_external_to_internals = np.zeros(len(Xi))
    
    for i in range(0,len(distance_from_second_external_to_internals)):
        x_second_internal_point  = Xi[i]
        y_second_internal_point  = Yi[i]
        distance_from_second_external_to_internals[i] = simplified_euclidean_distance(x_second_external_point,
                                                                                     x_second_internal_point,
                                                                                     y_second_external_point,
                                                                                     y_second_internal_point)
        
    candidates =np.argpartition(distance_from_second_external_to_internals,5)[0:5]
    second_internal_point = candidates[np.random.randint(0,5)]
    
    
    return first_external_point,second_external_point,first_internal_point, second_internal_point
    
    
    
def get_n_segment_break_points(X,Y,Xi,Yi,max_amplitude,min_amplitude,n_segments, n_tries = 25,debug=False):
    
    external_list_first_point = np.ones(n_segments, dtype=int) * -1
    external_list_second_point = np.ones(n_segments, dtype=int) * -1
    internal_list_first_point = np.ones(n_segments, dtype=int) * -1
    internal_list_second_point = np.ones(n_segments, dtype=int) * -1
    
    
    
    i = 0
    k= 0
    keep_trying = True
    while(keep_trying):
        if i>=n_tries:
            keep_trying = False
            
        else:
            if k>=n_segments:
                keep_trying = False
            else:
                br_point_ex1,br_point_ex2, br_point_in1,br_point_in2 = segment_get_break_points(X,Y,Xi,Yi,max_amplitude,min_amplitude)
                
                valid = True
                
                for j in range(n_segments):
                    
                    if external_list_first_point[j] < br_point_ex1 and br_point_ex1 < external_list_second_point[j]:
                        valid = False
                    if external_list_first_point[j] < br_point_ex2 and br_point_ex2 < external_list_second_point[j]:
                        valid = False
                    if internal_list_first_point[j] < br_point_in1 and br_point_in1 < internal_list_second_point[j]:
                        valid = False
                    if internal_list_first_point[j] < br_point_in2 and br_point_in2 < internal_list_second_point[j]:
                        valid = False
                    
                    if debug:
                        print("----------------------------------------------------------------------------------------------")
                        print('EX1:',external_list_first_point[j],'    BR_EX1:',br_point_ex1,'    EX2:',external_list_second_point[j],)
                        print('EX1:',external_list_first_point[j],'    BR_EX2:',br_point_ex2,'    EX2:',external_list_second_point[j],)
                        print('IN1:',internal_list_first_point[j],'    BR_IN1:',br_point_in1,'    IN2:',internal_list_second_point[j],)
                        print('IN1:',internal_list_first_point[j],'    BR_IN1:',br_point_in2,'    IN2:',internal_list_second_point[j],)
                        print("----------------------------------------------------------------------------------------------")
                        
                    
                
                if valid:
                    external_list_first_point[k]=br_point_ex1
                    external_list_second_point[k]=br_point_ex2
                    internal_list_first_point[k]=br_point_in1
                    internal_list_second_point[k]=br_point_in2
                    k=k+1
                
                i=i+1
    external_list_first_point=external_list_first_point[:k]
    external_list_second_point=external_list_second_point[:k]
    internal_list_first_point=internal_list_first_point[:k]
    internal_list_second_point=internal_list_second_point[:k]
    
                
    return external_list_first_point,external_list_second_point,internal_list_first_point,internal_list_second_point


def split_section(X,Xi,Y,Yi,br_point_ex1,br_point_ex2, br_point_in1,br_point_in2):
     
    real_len_1st=0
    if br_point_ex1 < br_point_ex2:
        real_len_1st = br_point_ex2 - br_point_ex1 
    else:
        real_len_1st = len(X)-br_point_ex1 + br_point_ex2 
    
    real_len_2nd = 0
    if br_point_in1 < br_point_in2:
        real_len_2nd = br_point_in2 - br_point_in1 
    else:
        real_len_2nd = len(Xi)-br_point_in1 + br_point_in2 
        
    new_X = np.zeros(real_len_1st+real_len_2nd+1)
    new_Y = np.zeros(real_len_1st+real_len_2nd+1)
    
    
    
    if br_point_ex1 < br_point_ex2:
        new_X[0:real_len_1st] = X[br_point_ex1:br_point_ex2]
        new_Y[0:real_len_1st] = Y[br_point_ex1:br_point_ex2]
    else:
        new_X[0:real_len_1st] = np.concatenate((X[br_point_ex1:len(X)],X[0:br_point_ex2]),axis = 0)
        new_Y[0:real_len_1st] = np.concatenate((Y[br_point_ex1:len(X)],Y[0:br_point_ex2]),axis = 0)
    
    if br_point_in1 < br_point_in2:
        new_X[real_len_1st:real_len_1st+real_len_2nd] = Xi[br_point_in1:br_point_in2][::-1]
        new_Y[real_len_1st:real_len_1st+real_len_2nd] = Yi[br_point_in1:br_point_in2][::-1]
    else:
        new_X[real_len_1st:real_len_1st+real_len_2nd] = np.concatenate((Xi[br_point_in1:len(X)],Xi[0:br_point_in2]),axis = 0)[::-1]
        new_Y[real_len_1st:real_len_1st+real_len_2nd] = np.concatenate((Yi[br_point_in1:len(X)],Yi[0:br_point_in2]),axis = 0)[::-1]
    
    new_X[real_len_1st+real_len_2nd] = X[br_point_ex1]
    new_Y[real_len_1st+real_len_2nd] = Y[br_point_ex1]
    
    return new_X,new_Y
    
    

def get_all_splits(X,Xi,Y,Yi,min_amplitude, max_amplotide,n_segments,n_tries=100):
    
    external_list_first_point,external_list_second_point,internal_list_first_point,internal_list_second_point = bm.get_n_segment_break_points(X,Y,Xi,Yi,min_amplitude,max_amplitude,n_segments,n_tries)

    X_maxtrix = np.zeros(())

    for i in range(0,n_segments):
        new_X,new_Y = bm.split_section(X,Xi,Y,Yi,  external_list_first_point[i],
                                                external_list_second_point[i],
                                                internal_list_first_point[i],
                                                internal_list_second_point[i])
    
        

