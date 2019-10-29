"""
Created on Mon Oct 28 23:22:05 2019
@author: Reza Kakooee, kakooee@arch.ethz.ch
"""
import random
import numpy as np

#%%
def generate_two_random_arrays(size=5, start=-10, stop=10):
    arr1 = [[random.uniform(start,stop) for _ in range(3)] for _ in range(size)]
    arr2 = [[random.uniform(start,stop) for _ in range(3)] for _ in range(size)]
    return arr1, arr2

#%% Calculating the cross product of two arrays of vector in pure Python 
# Define cross product of two vectors
def cross_product_of_two_vectors(a, b):    
    """
    This function calculates the cross product of two 3d vectors
    
    inputs: a => the first vector
            b => the second vector
    output: the cross product of the two input vectores
    """
    return list([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])

# Define cross product of two arrays of vectors
def cross_product_of_two_arrays_python(arr1, arr2):
    cross_products = []
    for a in arr1:
        for b in arr2:
            cross_products.append(cross_product_of_two_vectors(a, b))
    return cross_products

#%% Calculating the cross product of two arrays of vector in numpy with for
def numpy_cross_product_of_two_arrays_with_for(arr1, arr2):
    cross_products_numpy = [np.cross(arr1, a2) for a2 in arr2]
    return cross_products_numpy

#%% Calculating the cross product of two arrays of vector in numpy without for  
def numpy_cross_product_of_two_arrays_without_for(n):
    global arr1, arr2, cross_prod_np_without_for
    if n == 0:
        return cross_prod_np_without_for
    else:
        cp = np.cross(arr1, arr2[n-1])
        cross_prod_np_without_for.append(cp)
        numpy_cross_product_of_two_arrays_without_for(n-1)

#%% Compare the results of three methods
def are_equal(cross_prod_py, cross_prod_np_with_for, cross_prod_np_without_for):
    cross_prod_py_arr = np.array(cross_prod_py)
    cross_prod_np_with_for_arr = np.reshape(np.array(cross_prod_np_with_for), (25,3))
    cross_prod_np_without_for_arr  = np.reshape(np.array(cross_prod_np_without_for), (25,3))
    
    cross_prod_py_arr_sort = np.sort(cross_prod_py_arr, axis=0)
    cross_prod_np_with_for_arr_sort = np.sort(cross_prod_np_with_for_arr, axis=0)
    cross_prod_np_without_for_arr_sort = np.sort(cross_prod_np_without_for_arr, axis=0)
    
    return np.equal(cross_prod_py_arr_sort, cross_prod_np_with_for_arr_sort, cross_prod_np_without_for_arr_sort).all()

#%% Run
if __name__ == '__main__':
    # generating two random arrays of vector
    arr1, arr2 = generate_two_random_arrays()
    # calculating cross product in pure python
    cross_prod_py = cross_product_of_two_arrays_python(arr1, arr2)
    # calculating cross product in numpy with for
    cross_prod_np_with_for = numpy_cross_product_of_two_arrays_with_for(arr1, arr2)
    # calculating cross product in numpy without for
    cross_prod_np_without_for = []
    numpy_cross_product_of_two_arrays_without_for(n=len(arr1))
    # compare the three results
    print('Equality status is: ', are_equal(cross_prod_py, cross_prod_np_with_for, cross_prod_np_without_for))
    
