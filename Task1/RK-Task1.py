# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:03:15 2019

@author: Reza Kakooee, kakooee@arch.ethz.ch
"""
# Import dependencies
import numpy as np 
import pandas as pd
#%% # Loading the text data contaning all points
def load_data(text_path):
    """
    input: text_path => the text file name, if it is in the current directory, 
                        or the text file path, if it is not
    output: a readable text file containing all points  in string format
    """
    return open(text_path, "r")

#%% # Converting the loaded text to a numeric list
def stringText_to_numericList(points_txt):
    """
    input: points_txt => the text file containing all points in string format
    output: points_list => a list containing all points in float format
    """
    # define a line redear object
    line_reader = points_txt.readlines()
    # defining a list to keep data points
    points_list = []
    # going through the lines of the text, and extracting the points
    for line in line_reader:
        # remove parentheses from the text
        line = line.replace(')', ' ')
        line = line.replace('(', ' ')
        # convert a line of string to a vector of float points
        line_list = np.fromstring(line, dtype=float, sep=',')
        # 
        line_list_ABC = np.reshape(line_list, (3, 2))
        points_list.append(line_list_ABC)
    return points_list

#%% # Indentifying the rotation from the first point to the third point 
def rotation_detector(first_point, second_point, third_point):
    """
    input: first_point, second_point, third_point => three points on interest
    output: rotation => the rotation status from the first point to the third one
    """
    # the below line "somehow" compare the angle of A-to-B vector with the angle of B-to-C vector
    flag_value = (second_point[1] - first_point[1])*(third_point[0] - second_point[0])\
    - (third_point[1] - second_point[1])*(B[0] - first_point[0])
    if flag_value > 0:
        rotation = "Clockwise"
    elif flag_value < 0:
        rotation = "CounterClockwise"
    else:
        rotation = "None"
    return rotation

#%% # Run
if __name__ == "__main__":
    # load the text data
    points_txt = load_data("points.txt")
    # convert text of string points, to the list of float points
    points_list = stringText_to_numericList(points_txt)
    # definign an empty list to keep the rotation status for all points
    rotation_list = []
    # going through all points in the list
    for points in points_list:
        A, B, C = points[0], points[1], points[2]
        # detect the rotation from A to C
        rotation = rotation_detector(A, B, C)
        rotation_list.append(rotation)