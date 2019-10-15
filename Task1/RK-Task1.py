# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:03:15 2019

@author: Reza Kakooee, kakooee@arch.ethz.ch
"""

import numpy as np 
import matplotlib.pyplot as plt

points = open("points.txt", "r")

print(points.readable())

line_reader = points.readlines()
points_list_tuple = []
i = 0
for line in line_reader:
    line = line.replace(')', ' ')
    line = line.replace('(', ' ')
    line_list = np.fromstring(line, dtype=float, sep=',')
    line_list_tuple = list([tuple(line_list[0:2]), tuple(line_list[2:4]), tuple(line_list[4:6])])
    points_list_tuple.append(line_list_tuple)
    
    A, B, C = line_list_tuple
    
    flag_value = (B[1] - A[1])*(C[0] - B[0]) - (C[1] - B[1])*(B[0] - A[0])
    
    if flag_value > 0:
        flag = "CW"
    elif flag_value < 0:
        flag = "C_CW"
    else:
        flag = "None"
    
    
#%%
#    fig, ax = plt.subplots()
#    X = [A[0], B[0], C[0]]
#    Y = [A[1], B[1], C[1]]
#    ax.plot(X, Y)
#    ax.plot([A[0]], [A[1]],'o')
#    ax.annotate(flag, xy=(A[0],A[1]), xytext=(A[0]+0.0001,A[1]+0.0001))
#    plt.show()
#
#    plt.pause(3)
#    
#    plt.close()

