import numpy as np
import matplotlib.pyplot as plt

def processPoints(ps, pc, points) :
    """
        student code goes in this section
        
        Matthew Irvine
    """
    #print(ps.T)
    #print(pc.T)
    #print(points)
    ps = ps.T
    pc = pc.T
    
    
    #H = [[ps[...,0],ps[...,1],ps[...,2]][ps[...,3],pc[...,0],pc[...,1]][pc[...,2],pc[...,3],1]]
    #H = [ps[0:3],ps[3:6],np.concatenate[ps[6:8],[[1]]]
    '''
    print(ps.item(0))
    print(ps.item(1))
    print(ps.item(2))
    print(ps.item(3))
    print(ps.item(4))
    print(ps.item(5))
    print(ps.item(6))
    print(ps.item(7))
    
    
    H = np.array([[ps.item(0),ps.item(1),ps.item(2)],
         [ps.item(3),ps.item(4),ps.item(5)],
         [ps.item(6),ps.item(7),1]])
    
    print(H)
    '''
    BigBoi = np.array([[ps.item(0),ps.item(1),1,0,0,0,0,0,-pc.item(0),0,0,0],
                        [0,0,0,ps.item(0),ps.item(1),1,0,0,-pc.item(1),0,0,0],
                        [0,0,0,0,0,0,ps.item(0),ps.item(1),-1,0,0,0],
                        [ps.item(2),ps.item(3),1,0,0,0,0,0,0,-pc.item(2),0,0],
                        [0,0,0,ps.item(2),ps.item(3),1,0,0,0,-pc.item(3),0,0],
                        [0,0,0,0,0,0,ps.item(2),ps.item(3),0,-1,0,0],
                        [ps.item(4),ps.item(5),1,0,0,0,0,0,0,0,-pc.item(4),0],
                        [0,0,0,ps.item(4),ps.item(5),1,0,0,0,0,-pc.item(5),0],
                        [0,0,0,0,0,0,ps.item(4),ps.item(5),0,0,-1,0],
                        [ps.item(6),ps.item(7),1,0,0,0,0,0,0,0,0,-pc.item(6)],
                        [0,0,0,ps.item(6),ps.item(7),1,0,0,0,0,0,-pc.item(7)],
                        [0,0,0,0,0,0,ps.item(6),ps.item(7),0,0,0,-1],])
    
    ThinBoi = np.array([[0],
                        [0],
                        [-1],
                        [0],
                        [0],
                        [-1],
                        [0],
                        [0],
                        [-1],
                        [0],
                        [0],
                        [-1]])
    
    x = np.linalg.solve(BigBoi,ThinBoi)
    #print(x)
    
    H = np.array([[x.item(0),x.item(1),x.item(2)],
                  [x.item(3),x.item(4),x.item(5)],
                  [x.item(6),x.item(7),1]])
    #print(H)
    v1 = np.array([[points.item(0)],
                  [points.item(13)],
                  [1]])
    #print(v1)
    
    corr1 = np.dot(H,v1)
    corr1 = corr1/corr1.item(2)
    #print(corr1)
    
    v2 = np.array([[points.item(1)],
                  [points.item(14)],
                  [1]])
    #print(v2)
    corr2 = np.dot(H,v2)
    corr2 = corr2/corr2.item(2)
    #print(corr2)
    
    v3 = np.array([[points.item(2)],
                  [points.item(15)],
                  [1]])
    #print(v3)
    corr3 = np.dot(H,v3)
    corr3 = corr3/corr3.item(2)
    #print(corr3)
    
    v4 = np.array([[points.item(3)],
                  [points.item(16)],
                  [1]])
    #print(v4)
    corr4 = np.dot(H,v4)
    corr4 = corr4/corr4.item(2)
    #print(corr4)
    
    v5 = np.array([[points.item(4)],
                  [points.item(17)],
                  [1]])
    #print(v5)
    corr5 = np.dot(H,v5)
    corr5 = corr5/corr5.item(2)
    #print(corr5)
    
    v6 = np.array([[points.item(5)],
                  [points.item(18)],
                  [1]])
    #print(v6)
    corr6 = np.dot(H,v6)
    corr6 = corr6/corr6.item(2)
    #print(corr6)
    
    v7 = np.array([[points.item(6)],
                  [points.item(19)],
                  [1]])
    #print(v7)
    corr7 = np.dot(H,v7)
    corr7 = corr7/corr7.item(2)
    #print(corr7)
    
    v8 = np.array([[points.item(7)],
                  [points.item(20)],
                  [1]])
    #print(v8)
    corr8 = np.dot(H,v8)
    corr8 = corr8/corr8.item(2)
    #print(corr8)
    
    v9 = np.array([[points.item(8)],
                  [points.item(21)],
                  [1]])
    #print(v9)
    corr9 = np.dot(H,v9)
    corr9 = corr9/corr9.item(2)
    #print(corr9)
    
    v10 = np.array([[points.item(9)],
                  [points.item(22)],
                  [1]])
    #print(v10)
    corr10 = np.dot(H,v10)
    corr10 = corr10/corr10.item(2)
    #print(corr10)
    
    v11 = np.array([[points.item(10)],
                  [points.item(23)],
                  [1]])
    #print(v11)
    corr11 = np.dot(H,v11)
    corr11 = corr11/corr11.item(2)
    #print(corr11)
    
    v12 = np.array([[points.item(11)],
                  [points.item(24)],
                  [1]])
    #print(v12)
    corr12 = np.dot(H,v12)
    corr12 = corr12/corr12.item(2)
    
    v13 = np.array([[points.item(12)],
                  [points.item(25)],
                  [1]])
    #print(v13)
    corr13 = np.dot(H,v13)
    corr13 = corr13/corr13.item(2)
    #print(corr12)
    
    projected = np.array([[corr1.item(0),corr2.item(0),corr3.item(0),corr4.item(0),corr5.item(0),corr6.item(0),corr7.item(0),corr8.item(0),corr9.item(0),corr10.item(0),corr11.item(0),corr12.item(0),corr13.item(0)],
                           [corr1.item(1),corr2.item(1),corr3.item(1),corr4.item(1),corr5.item(1),corr6.item(1),corr7.item(1),corr8.item(1),corr9.item(1),corr10.item(1),corr11.item(1),corr12.item(1), corr13.item(1)]])
    #print(projected)
    return H, projected


def plotPoints(projected, test_points) :
    #
    #  DO NOT MODIFY THIS SECTION
    #
    
    plt.plot(test_points[0, :], test_points[1, :], '-o')
    plt.title('skewed points')
    # from https://stackoverflow.com/questions/16183462/saving-images-in-python-at-a-very-high-quality
    #plt.savefig('homographySkewed.eps', format='eps', dpi=1000)

    plt.figure(2)
    plt.plot(projected[0, :], projected[1, :], 'r-o')
    plt.title('corrected points')
    #plt.savefig('homographyCorrected.eps', format='eps', dpi=1000)

    plt.show()
    
###################  main  ###################
if __name__ == "__main__" :
    #
    #  DO NOT MODIFY THIS SECTION
    #
    
    
    # points in skewed picture to use for mapping
    # each column is a vector representing the x/y coordinates of a point
    #   in the skewed picture
    # row 1 is the x-values
    # row 2 is the y-values
    points_skewed = np.array([[0,   0, 50, 50],
                              [0, 100, 75, 25]])
    
    # points in corrected picture to use for mapping
    # each column is a vector representing the x/y coordinates of a point
    #   in the corrected picture
    # row 1 is the x-values
    # row 2 is the y-values
    points_corrected = np.array([[0,   0, 200, 200], 
                                 [0, 100, 100,   0 ]])
    
    # each column is the set of x/y coordinates of a point that should be corrected
    test_points = np.array([[42.8571, 38.4615, 33.3333, 27.2727, 20, 11.1111, 20, \
                             27.2727, 33.3333, 38.4615, 42.8571, 46.6667, 42.8571],
                            [50,      65.3846, 66.6667, 68.1818, 50, 27.7778, 30, \
                             31.8182, 33.3333, 34.6154, 35.7143, 36.6667, 50],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
      
    H, projected = processPoints(points_skewed, points_corrected, test_points)
    print('part a: H matrix\n')
    print(H)
    print('\npart b: projected test points (not as homogeneous coordinates)\n')
    print(projected)
    
    plotPoints(projected, test_points) 
