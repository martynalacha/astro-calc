import pytest
import pint
from astro_calc.physics import calculate_planetary_weight, calculate_first_cosmic_velocity, ureg

def test_calculate_planetary_weight():
    """
    Test weight calculation for standard Earth gravity.
    """
    mass = 10 * ureg.kilogram
    gravity = 9.81 * ureg.meter / ureg.second ** 2
    
    result = calculate_planetary_weight(mass, gravity)
    
    assert result.magnitude == pytest.approx(98.1)
    assert result.units == ureg.newton

def test_calculate_first_cosmic_velocity():
    """
    Test first cosmic velocity calculation for Earth.
    """
    gravity = 9.81 * ureg.meter / ureg.second ** 2
    radius = 6371 * ureg.kilometer
    
    result = calculate_first_cosmic_velocity(gravity, radius)
    
    assert result.magnitude == pytest.approx(7905.8, rel=1e-3)
    assert result.units == (ureg.meter / ureg.second)

def test_invalid_units_raise_error():
    """
    Verify that passing incorrect dimensions raises a DimensionalityError.
    """
    mass = 10 * ureg.meter
    gravity = 9.81 * ureg.meter / ureg.second ** 2
    
    with pytest.raises(pint.errors.DimensionalityError):
        calculate_planetary_weight(mass, gravity)