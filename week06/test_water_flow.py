from pytest import approx
import pytest
from water_flow import (
    water_column_height, 
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction
    )

def test_water_column_height():
    """
    Test function for water_column_height
    """
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == 7.5
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == 57.9


def test_pressure_gain_from_water_height():
    """
    Test function for pressure_gain_from_water_height
    """
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.001) 
    
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001) 
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=0.001) 


def test_pressure_loss_from_pipe():
    # Test numbers: an array of tuple => (Pipe Diameter,	Pipe Length, Friction Factor, Fluid Velocity, Expected Pressure Loss, approx Absolute Tolerance)
    test_numbers = [
                    (0.048692,	0,	0.018,	1.75,	0,	0.001),
                    (0.048692,	200,	0,	1.75,	0,	0.001),
                    (0.048692,	200,	0.018,	0,	0,	0.001),
                    (0.048692,	200,	0.018,	1.75,	-113.008,	0.001),
                    (0.048692,	200,	0.018,	1.65,	-100.462,	0.001),
                    (0.28687,	1000,	0.013,	1.65,	-61.576,	0.001),
                    (0.28687,	1800.75,	0.013,	1.65,	-110.884,	0.001)
                    ]
    for test in test_numbers:
        assert pressure_loss_from_pipe(test[0], test[1], test[2], test[3]) == approx(test[4], abs=test[5])


def test_pressure_loss_from_fittings():
    """
    Test function pressure_loss_from_fittings
    """
    # (Fluid Velocity,	Quantity  of Fittings,	Expected Pressure Loss,	approx Absolute Tolerance)
    test_numbers = [
        (0, 3, 0, 0.001),
        (1.65, 0, 0, 0.001),
        (1.65,	2,	-0.109,	0.001),
        (1.75,	2,	-0.122,	0.001),
        (1.75,	5,	-0.306,	0.001)
    ]
    for test in test_numbers:
        assert pressure_loss_from_fittings(test[0], test[1]) == approx(test[2], abs=test[3])


def test_reynolds_number():
    """
    Test function for reynolds_number
    """
    # (Hydraulic Diameter,	Fluid Velocity,	Expected Reynolds Number, approx Absolute Tolerance)
    test_numbers = [
        (0.048692,	0,	0,	1),
        (0.048692,	1.65,	80069,	1),
        (0.048692,	1.75,	84922,	1),
        (0.28687,	1.65,	471729,	1),
        (0.28687,	1.75,	500318,	1)
    ]

    for test in test_numbers:
        assert reynolds_number(test[0], test[1]) == approx(test[2], abs=test[3])


def test_pressure_loss_from_pipe_reduction():
    """
    Test function for pressure_loss_from_pipe_reduction
    """
    # (Larger Diameter,	Fluid Velocity, Reynolds Number, Smaller Diameter,
    # Expected Pressure Loss, approx Absolute Tolerance)
    test_numbers = [
        (0.28687,	0,	1,	0.048692,	0,	0.001),
        (0.28687,	1.65,	471729,	0.048692,	-163.744,	0.001),
        (0.28687,	1.75,	500318,	0.048692,	-184.182,	0.001)
    ]

    for test in test_numbers:
        assert pressure_loss_from_pipe_reduction(test[0], test[1], test[2], test[3]) == approx(test[4], abs=test[5])
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
