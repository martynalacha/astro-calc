Tutorial
========

This guide demonstrates how to perform astrophysical calculations using our library.

Prerequisites
-------------

Before starting, ensure you have a unit registry initialized:

.. code-block:: python

    import pint
    ureg = pint.UnitRegistry()

Calculating Planetary Weight
----------------------------

To calculate the weight of an object on a planet, you need its mass and the planet's surface gravity.

.. code-block:: python

    from astro_calc.physics import calculate_planetary_weight

    mass = 80 * ureg.kilogram
    gravity = 3.71 * ureg.meter / ureg.second**2  # Mars gravity
    
    weight = calculate_planetary_weight(mass, gravity)
    print(f"Weight on Mars: {weight}")

Calculating First Cosmic Velocity
---------------------------------

To find the orbital velocity required to stay in a circular orbit close to the celestial body:

.. code-block:: python

    from astro_calc.physics import calculate_first_cosmic_velocity

    gravity = 9.81 * ureg.meter / ureg.second**2  # Earth gravity
    radius = 6371 * ureg.kilometer                # Earth radius
    
    velocity = calculate_first_cosmic_velocity(gravity, radius)
    print(f"First cosmic velocity: {velocity}")