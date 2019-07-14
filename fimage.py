import  numpy as np

def fimage(F, M, R, S) :
    """ Compute the image formula : 
        
    """
    k=np.ndarray([0,0,1])
    R_inv=np.linalg.inv(R)
    top = k.transpose().dot(F).dot(R).dot(M - S)
    bottom = k.transpose.dot(R).dot(M -S)
    return F - top/bottom

def radialStd 