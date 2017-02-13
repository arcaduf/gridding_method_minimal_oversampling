###########################################################
###########################################################
####                                                   ####
####                     TEST ROUTINE                  ####
####                                                   ####
###########################################################
###########################################################




####  PYTHON MODULES
from __future__ import division , print_function
import sys
import numpy as np

sys.path.append( '../common/' )
import my_image_io as io
import my_image_display as dis

import class_projectors_grid as cpj




####  MY VARIABLE FORMAT
myfloat = np.float32




###########################################################
###########################################################
####                                                   ####
####                       TEST 1                      ####
####                                                   ####
###########################################################
########################################################### 

##  Check whether each backprojector is really adjoint to the
##  corresponding forward projector by using the definition of
##  adjoint operator.
##  A: U --> V  thus A^{T}: V --> U
##  A is the linear operator, A^{T} is the adjoint operator, 
##  U and V are vector spaces.
##  For all x in U and y in V, it holds that:
##  < y , Ax > = < A^{T}y , x >

def test1():
    ##  Pick up a random number in [0,256] and make sure it is even
    n = np.int( np.random.rand( 1 ) * 1024 )
    if n == 0:
        n = 20
    if n % 2 != 0:
        n += 1
    print( 'Number of pixels: ' , n )

    ##  Construct an array of random angles in rad
    a  = np.random.random( n ).astype( myfloat )

    ##  Construct a random object
    y1 = np.random.random( ( n , n ) ).astype( myfloat )

    ##  Construct a random sinogram
    x2 = np.random.random( ( n , n ) ).astype(myfloat)
    
    ##  Load gridding projectors
    tp = cpj.projectors( n , a , ctr=0.0 )

    ##  Create A^{T}y
    x1 = tp.At( y1 )

    ##  Create Ax
    y2 = tp.A( x2 )

    ##  Compute inner product < A^{T}y , x >
    inn_prod = np.sum( np.conjugate( x2 ) * x1 )

    ##  Compute inner product < y , Ax >
    inn_prod = np.sum( np.conjugate( y2 ) * y1 )

    print( '< b , Tt( a ) >  = ', inn_prod )
    print( '< T( b ) , a >  = ', inn_prod )  




###########################################################
###########################################################
####                                                   ####
####                       TEST 2                      ####
####                                                   ####
###########################################################
###########################################################

##  Test forward projector only

def test2():
    ##  Read Shepp-Logan image in folder "../data/"
    image = io.readImage( '../data/shepp_logan_pix0256.DMP' )
    n = image.shape[0]

    ##  Create array of 200 angularly equispaced angles in [0,180) (degrees)
    nang = 402
    a = np.arange( nang ) * 180.0 / nang

    ##  Compute forward projection
    tp = cpj.projectors( n , a , ctr=0.0 )
    sino = tp.A( image )

    return sino




###########################################################
###########################################################
####                                                   ####
####                       TEST 3                      ####
####                                                   ####
###########################################################
###########################################################

##  Test backprojector only

def test3( sino ):
    ##  Get sinogram size
    nang , n = sino.shape

    ##  Create array of 200 angularly equispaced angles in [0,180) (degrees)
    a = np.arange( nang ) * 180.0 / nang

    ##  Compute non-filtered backprojection
    tp = cpj.projectors( n , a , ctr=0.0 )
    reco = tp.At( sino )

    return reco




###########################################################
###########################################################
####                                                   ####
####                       TEST 4                      ####
####                                                   ####
###########################################################
###########################################################

##  Test reconstruction

def test4( sino ):
    ##  Get sinogram size
    nang , n = sino.shape

    ##  Create array of 200 angularly equispaced angles in [0,180) (degrees)
    a = np.arange( nang ) * 180.0 / nang

    ##  Compute non-filtered backprojection
    tp = cpj.projectors( n , a , ctr=0.0 , filt='hann' )
    reco = tp.fbp( sino )

    return reco




###########################################################
###########################################################
####                                                   ####
####                         MAIN                      ####
####                                                   ####
###########################################################
###########################################################  

def main():
    ##  Initial print
    print( '''\nThe program will execute in order 4 tests for the gridding implementation of the forward and backprojector''' )

    print( '''\nEvery time an image is displayed the code is temporarily halted. To the successive tests close the image''')


    #############################################################
    ##  Test n.1
    #############################################################
    inp = raw_input( '\n\nProceed with test n.1? (y/n) ' )
    if inp == 'n':
        exit()

    print( '###################################################' )
    print( '###                                             ###' )
    print( '###        TEST 1: Test adjoint operator        ###' )
    print( '###                                             ###' ) 
    print( '###################################################' ) 

    test1()




    #############################################################
    ##  Test n.2
    #############################################################
    inp = raw_input( '\n\nProceed with test n.2? (y/n) ' )
    if inp == 'n':
        exit()

    print( '###################################################' )
    print( '###                                             ###' )
    print( '###        TEST 2: Test forward operator        ###' )
    print( '###                                             ###' ) 
    print( '###################################################' ) 

    sino = test2()

    dis.plot( sino , 'Forward projection 402 views X 256 pixels' )




    #############################################################
    ##  Test n.3
    ############################################################# 
    inp = raw_input( '\n\nProceed with test n.3? (y/n) ' )
    if inp == 'n':
        exit()

    print( '###################################################' )
    print( '###                                             ###' )
    print( '###          TEST 3: Test Backprojector         ###' )
    print( '###                                             ###' ) 
    print( '###################################################' ) 

    reco = test3( sino )

    dis.plot( reco , 'Non-filtered backprojection' )  
    
    
    
    
    #############################################################
    ##  Test n.4
    ############################################################# 
    inp = raw_input( '\n\nProceed with test n.4? (y/n) ' )
    if inp == 'n':
        exit()

    print( '###################################################' )
    print( '###                                             ###' )
    print( '###              TEST 4: Test FBP               ###' )
    print( '###                                             ###' ) 
    print( '###################################################' ) 

    reco = test4( sino )

    dis.plot( reco , 'Reconstruction with Hanning filter' )  




###########################################################
###########################################################
####                                                   ####
####                    CALL TO MAIN                   ####
####                                                   ####
###########################################################
###########################################################

if __name__ == '__main__':
    main()
