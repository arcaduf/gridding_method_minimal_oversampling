GRIDDING PROJECTORS WITH MINIMAL OVERSAMPLING
=============================================



##  Brief description
This repository contains a mixed Python/C implementation of the gridding
projectors with minimal oversampling.

For more information on the algorithm, please refer to the following 
publications:

* F.Arcadu et al., "A Forward Regridding Method With Minimal Oversampling for
  Accurate and Efficient Iterative Tomographic Algorithms.", IEEE Trans. on Imag.
  Proc., 25(3), 2016.
           
* F. Arcadu et al., "Fast gridding projectors for analytical and iterative
  tomographic reconstruction of differential phase contrast data.", Optics
  Express, 24(13), 2016.           



##  Installation
Basic compilers like gcc and g++ are required.
The simplest way to use the code is with an Anaconda environment equipped with
python-2.7, scipy, scikit-image and Cython.

Procedure:

1. Create the Anaconda environment (if not created yet): `conda create -n iter-rec python=2.7 anaconda`.

2. Install required Python packages: `conda install -n iter-rec scipy scikit-image Cython`.

3. Activate the environment: `source activate iter-rec`.

4. `git clone git@github.com:arcaduf/gridding_method_min_oversampl.git`.
 
5. Install routines in C: `python setup.py`.

If `setup.py` runs without giving any error all subroutines in C have been installed and
your python version meets all dependencies.

If you run `python setup.py 1` (you can use any other character than 1), the 
all executables, temporary and build folders are deleted, the test data are 
placed in .zip files. In this way, the repository is restored to its original
status, right after the download.



##  Test the package
Go inside the folder "scripts/" and run: `python run_all_tests.py`

