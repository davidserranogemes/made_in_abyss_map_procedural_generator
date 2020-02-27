# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:26:24 2020

@author: david
"""

import numpy as np

class section():
       
    
    def __init__(self,X,Y,height=0,slope=0):
        self.__X = X
        self.__Y = Y
        self.__height = height
        self.__slope = slope
        
        
        self.__Z = np.zeros(len(X))
        
        max_x = np.max(X)
        
        for i in range(0,len(X)):
            self.__Z[i] = height - (max_x-X[i]) * np.tan(slope)
        
    
    def get_section_points(self):
        return self.__X,self.__Y,self.__Z
    
    def get_section_slope(self):
        return self.__slope
    
    def get_section_height(self):
        return self.__height
    



