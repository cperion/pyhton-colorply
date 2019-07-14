import  numpy as np

def fimage(F, M, R, S) :
    """ Compute the image formula : 
        
    """
    k=np.ndarray([0,0,1])
    R_inv=np.linalg.inv(R)
    top = k.transpose().dot(F).dot(R).dot(M - S)
    bottom = k.transpose.dot(R).dot(M -S)
    return F - top/bottom

def radialStd(point, pps, a, b, c) :
    """ Corrects the postion of the point according to the standard radial distorsion model"""
    r = np.linalg.norm(point-pps)
    rsquared= r*r
    """ We use HORNEEERRRRRRRR to evluate ar2+br4+cr6"""
    poly = c
    poly = poly*rsquared + b
    poly = poly*rsquared + a
    poly = poly*rsquared
    """ HORNEEEEERRRRR DONE """
    dr = poly*(point-pps) # correction vector
    return point + dr

def cimage(F, M, R, S, pps, a, b, c,) :
    return radialStd(fimage(F, M, R, S), pps, a, b ,c)

