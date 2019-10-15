"""
Created on Tue Oct 15 14:03:15 2019
@author: Reza Kakooee, kakooee@arch.ethz.ch
"""
#%% # Import dependencies
import logging 
import numpy as np 
import pandas as pd

#%% # logging 
# Create and configure the logging
LOG_FORMAT = "%(message)s"
logging.basicConfig(filename="logs.log", level=logging.DEBUG, 
                    format=LOG_FORMAT, filemode="w")
logger = logging.getLogger()

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

#%% # Plotting: set the defualt flag to 1 if you want to see the plots
def plotting(points_list, rotation_list, flag=0):
    """
    inputs:
        points_list => a list containing all points in float format
        rotation_list => a list containing the rotation status for all datapoint
        flag => a binary variable to enable plotting. Set to 1 if you want to see the plots
    """
    if flag:
        import matplotlib.pyplot as plt
        for points, rotation in zip(points_list, rotation_list):
            A, B, C = points[0], points[1], points[2]
            X = [A[0], B[0], C[0]]
            Y = [A[1], B[1], C[1]]
            fig, ax = plt.subplots()
            ax.plot(X, Y)
            ax.plot(A[0], A[1], 'o')
            ax.annotate("A", xy=(A[0], A[1]), xytext=(A[0]+0.001, A[1]+0.001))
            ax.annotate("B", xy=(B[0], B[1]), xytext=(B[0]+0.001, B[1]+0.001))
            ax.annotate("C", xy=(C[0], C[1]), xytext=(C[0]+0.001, C[1]+0.001))
            rotation_position = [np.mean([min(X), max(X)]), np.mean([min(Y), max(Y)])]
            ax.annotate(rotation, xy=(rotation_position[0], rotation_position[1]))
            plt.show()
            plt.pause(1.5)
            plt.close()

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
        # save rotation status to logs
        MESSAGE = "The rotation from [{0:9.4f} , {1:9.4f}] to [{2:9.4f} , {3:9.4f}] and then to [{4:9.4f} , {5:9.4f}] is: {6}"
        logger.info(MESSAGE.format(A[0],A[1], B[0], B[1], C[0], C[1], rotation))
    # plot the points and see the rotation
    plotting(points_list, rotation_list)
