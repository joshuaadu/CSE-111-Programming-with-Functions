
# ρ is the density of water (998.2 kilogram / meter3)
density_of_water = 998.2


def water_column_height(tower_height, tank_height):
    """
    Calculates the height of a column of water from a tower height and a tank wall height
    Parameters:
        tower_height: height of the tower
        tank_height: height of the tank
    Returns: height of a column of water
    """
    column_height = tower_height + ((3 * tank_height) / 4)
    return column_height


def pressure_gain_from_water_height(height: float):
    """
    Calculates the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank.
    Parameters:
        height: the height of the water columns in meters
    Returns: the pressure calculated

    P = ρgh/1000
    where
        P is the pressure in kilopascals
        ρ is the density of water (998.2 kilogram / meter3)
        g is the acceleration from Earths gravity (9.80665 meter / second2)
        h is the height of the water column in meters
    """
    
    pressure = (density_of_water * 9.80665 * height) / 1000
    return pressure


def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """
    Calculates the water pressure lost because of the friction between the water and the walls of a pipe
    that it flows through
    Parameters:
        pipe_diameter
        pipe_length
        friction_factor
        fluid_velocity
    Returns: pressure loss
    """
    pressure_loss = -(friction_factor * pipe_length * density_of_water * (fluid_velocity ** 2)) / (2000 * pipe_diameter)
    return pressure_loss