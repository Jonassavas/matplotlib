import numpy as np
from numpy.testing import assert_array_almost_equal
import pytest
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import image_comparison
import matplotlib.transforms as mtransforms
import matplotlib.lines as mlines 
    
'''
Untested requirement: 
raising ValueError if shape of color and grid doesn't match

Testing that the function streamplot() raises a value error if
the 2D array color given doesn't match the shape of the grid 
(created by the x and y input arrays).
'''
def test_streamplot_color_grid_shapes_not_matching():
    with pytest.raises(ValueError) as excinfo:
        plt.streamplot(np.arange(3), np.arange(3),
                       np.full((3, 3), np.nan), np.full((3, 3), np.nan),
                       color=np.random.rand(5, 5))
    assert str(excinfo.value) == "If 'color' is given, it must match the shape of the (x, y) grid"

'''
Untested requirement: 
raising ValueError if shape of linewidth and grid doesn't match

Testing that the function streamplot() raises a value error if
the 2D array linewidth given doesn't match the shape of the grid 
(created by the x and y input arrays).
'''
def test_streamplot_linewidth_grid_shape_not_matching():
    with pytest.raises(ValueError) as excinfo:
        plt.streamplot(np.arange(3), np.arange(3),
                       np.full((3, 3), np.nan), np.full((3, 3), np.nan),
                       color=np.random.rand(3, 3), linewidth= np.full((5, 5), np.nan))
    assert str(excinfo.value) == "If 'linewidth' is given, it must match the shape of the (x, y) grid"

'''
Untested requirement: 
raising ValueError if shape of u (or v) and grid doesn't match

Testing that the function streamplot() raises a value error if
the 2D arrays u or v given doesn't match the shape of the grid
(created by the x and y input arrays), here it is the u that 
doesn't match.
'''
def test_streamplot_linewidth_check_u_grid_shape_not_matching():
    with pytest.raises(ValueError) as excinfo:
        plt.streamplot(np.arange(3), np.arange(3),
                       np.full((5, 5), np.nan), np.full((3, 3), np.nan),
                       color=np.random.rand(3, 3))
    assert str(excinfo.value) == "'u' and 'v' must match the shape of the (x, y) grid"

'''
Untested requirement: 
raising ValueError if starting points outside of grid

Testing that the function streamplot() raises a value error if
the values in the start_points ndarray of the kind (N, 2) 
contains points from outside the data boundaries.
'''
def test_streamplot_():
    with pytest.raises(ValueError) as excinfo:
        plt.streamplot(np.arange(3), np.arange(3),
                       np.full((3, 3), np.nan), np.full((3, 3), np.nan),
                       color=np.random.rand(3, 3), start_points=np.full((3, 2), 10))
    assert str(excinfo.value) == "Starting point (10.0, 10.0) outside of data boundaries"
