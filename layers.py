# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:26:24 2020

@author: david
"""

class generic_layer():
       
    
    def __init__(self,X,Y,height=0,slope=0):
        self.__X = X
        self.__Y = Y
        self.__height = height
        self.__slope = slope
        
    
    def get_layer_points(self):
        return self.__X,self.__Y
    
    def get_layer_slope(self):
        return self.__slope
    
    def get_layer_height(self):
        return self.__height
        
x = generic_layer() 