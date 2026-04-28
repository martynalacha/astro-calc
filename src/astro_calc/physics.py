import pint

ureg = pint.UnitRegistry()

def calculate_planetary_weight(mass: pint.Quantity, gravity: pint.Quantity) -> pint.Quantity:
    """
    Calculate the weight of an object on a specific planet.
    """
    weight = mass * gravity
    return weight.to(ureg.newton)

def calculate_first_cosmic_velocity(gravity: pint.Quantity, radius: pint.Quantity) -> pint.Quantity:
    """
    Calculate the first cosmic velocity (orbital velocity) for a celestial body.
    """
    velocity = (gravity * radius) ** 0.5
    return velocity.to(ureg.meter / ureg.second)