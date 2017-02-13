from __future__ import division , print_function
import os
import sys
import shutil


if len( sys.argv ) == 1:
    compile = True
else:
    compile = False

curr_dir = os.getcwd()

for path , subdirs , files in os.walk( './' ):
    for i in range( len( subdirs ) ):
        folderin = subdirs[i]
        if folderin == 'build' or folderin == 'debug':
            shutil.rmtree( os.path.join( path , folderin ) )
    
    for i in range( len( files ) ):
        filein = files[i] 
        
        if filein.endswith( '.pyc' ) is True or \
           filein.endswith( '.pyo' ) is True or \
           filein.endswith( '.o' )   is True or \
           filein.endswith( '.so' )  is True:
            os.remove( os.path.join( path , filein ) )


if compile is True:
    path = 'gridding_module/pymodule_gridrec_v4/'
    os.chdir( path )
    os.system( 'python compile.py' )
    os.chdir( curr_dir )
