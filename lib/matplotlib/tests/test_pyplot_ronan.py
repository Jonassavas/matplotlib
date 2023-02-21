import difflib

import numpy as np
import sys
from pathlib import Path

import pytest

import matplotlib as mpl
from matplotlib.testing import subprocess_run_for_testing
from matplotlib import pyplot as plt
from matplotlib._api import MatplotlibDeprecationWarning

# test if we give subplots' arguments to subplot that an error is raised.
# the third argument of subpltos is a boolean while the third argument of suplot (without s) is an integer
# Thus an error is thrown indicating that the third argument should be an integer
def test_subplot_confused_with_subplots():
        with pytest.raises(ValueError) as excinfo:
            with pytest.warns(MatplotlibDeprecationWarning) as warninginfo:
                ax = plt.subplot(1, 2, False)
            assert warninginfo.expected_warning == "The subplot index argument to subplot() appears to be a boolean. Did you intend to use subplots()?"
        assert "num must be an integer" in str(excinfo.value)
