import difflib

import numpy as np
import sys
from pathlib import Path

import pytest

from matplotlib.figure import Figure
import matplotlib as mpl
from matplotlib.testing import subprocess_run_for_testing
from matplotlib import pyplot as plt
from matplotlib._api import MatplotlibDeprecationWarning

# test if we give subplots' arguments to subplot that an error is raised.
# the third argument of subpltos is a boolean while the third argument of suplot (without s) is an integer
# Thus an error is thrown indicating that the third argument should be an integer
# and a warning is thrown too
def test_subplot_confused_with_subplots():
    with pytest.raises(ValueError) as excinfo:
         with pytest.warns(MatplotlibDeprecationWarning) as warninginfo:
            ax = plt.subplot(1, 2, False)
         assert warninginfo.expected_warning == "The subplot index argument to subplot() appears to be a boolean. Did you intend to use subplots()?"
    assert "num must be an integer" in str(excinfo.value)

# test if we the num argument of figure is a figure not managed by pyplot
def test_figure_not_managed_by_pyplot():
    with pytest.raises(ValueError) as excinfo:
        fig = plt.figure()
        fig.canvas.manager = None
        plt.figure(num=fig)
    assert str(excinfo.value) == "The passed figure is not managed by pyplot"

# if num is an instance of str and str = "all" then we should throw a warning
def test_figure_with_num_str():
     with pytest.warns(UserWarning) as warninginfo:
        plt.figure("all")
     assert len(warninginfo) == 1
     assert "close('all') closes all existing figures." in str(warninginfo[0].message)

# check if the label of the figure is properly attributed
def test_figure_label_attributed():
    fig = plt.figure("name")
    assert fig.get_label() == "name"


