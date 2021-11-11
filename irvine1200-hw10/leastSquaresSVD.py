#Matthew Irvine


import numpy as np

def lsSVD(data, tol) :
    """
        student code goes here
        
        I don't know what the heck I am doing wrong here
        I never get close to the results and I can't see what I'm doing wrong.
    """
    
    # first n-1 columns are A, and column n is b
    b = data[:,-1]
    A = data[:,:-1]
    
    U, E, VT = np.linalg.svd(A, full_matrices = False)
    r = np.argwhere(E>=tol).size
    
    X = VT.T            #To get the right sizing
    n = 0
    while(n<=r):
        numerator = np.dot(U.T[n],b)
        scalar = numerator/E[n]
        X[n] = scalar * VT.T[n]
        n =n+1
    x = np.zeros(4)
    n =0
    while(n<=r):
        x[n] =np.add(np.add(X[0,n],X[1,n]),np.add(X[2,n],X[3,n]))
        n = n+1
    
    residual = b-np.dot(A,x)
    norm = np.linalg.norm(residual)
        
    
    return x, E, r, norm
    
    

#############################  main  #############################
#
#    DO NOT CHANGE ANYTHING BELOW THIS
#
if __name__ == "__main__" :
    data = np.genfromtxt("waterUsage.csv", dtype=None, delimiter=',', skip_header=5)
    
    # function leastSquaresSvdStudent
    #      parameters:  2D numpy array, int
    #   return values:  1D numpy array, 1D numpy array, float
    #
    
    tolerance = 2.5
    x, S, r, norm = lsSVD(data, tolerance)
    
    print("singular values")
    print(S)
    
    print("\neffective rank = %d when tolerance is %.1f" % (r, tolerance))
    
    print("\nEstimates")
    print("    laundry = %5.1f gallons" % x[0])         #258.2
    print(" dishwasher = %5.1f gallons" % x[1])         #-121.3
    print("     shower = %5.1f gallons" % x[2])         #110.2
    print(" sprinklers = %5.1f gallons" % x[3])         #121.8
    
    print("\nthe norm of the residual is %.1f" % norm)      #1715.9

