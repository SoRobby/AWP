'''
AWP | Astrodynamics with Python by Alfonso Gonzalez
https://github.com/alfonsogonzalez/AWP
https://www.youtube.com/c/AlfonsoGonzalezSpaceEngineering

Numerical Tools Library Unit Tests
'''

# 3rd party libraries
import pytest

# AWP library
import numerical_tools as nt

# Treat all warnings as errors
pytestmark = pytest.mark.filterwarnings( 'error' )

def test_norm_zero_vector():
	assert nt.norm( [ 0, 0, 0 ] ) == 0.0
