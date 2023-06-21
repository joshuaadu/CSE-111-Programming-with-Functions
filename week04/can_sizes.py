"""Computes and prints the storage efficiency for steel can"""

import math

## Data list of tuples for steel cans: (Name, Radius(centimeters), height(centimeters), Cost per Can(U.S. dollars)) 
steel_cans = [
    ('#1 Picnic', 6.83, 10.16, 0.28),
    ('#1 Tall',	7.78, 11.91, 0.43),
    ('#2', 8.73, 11.59,	0.45),
    ('#2.5', 10.32, 11.91, 0.61),
    ('#3 Cylinder',	10.79, 17.78, 0.86),
    ('#5', 13.02, 14.29, 0.83),
    ('#6Z',	5.40,	8.89,	0.22),
    ('#8Z short', 6.83, 7.62, 0.26),
    ('#10',	15.72, 17.78, 1.53),
    ('#211', 6.83, 12.38, 0.34),
    ('#300', 7.62, 11.27, 0.38),
    ('#303', 8.10, 11.11, 0.42),
              ]


def main():
    """
    Main function to calculate and output the storage efficiency of a steel can
    """
    for can in steel_cans:
        volume = compute_volume(can[1], can[2])
        surface_area = compute_surface_area(can[1], can[2])
        storage_efficiency = round(volume / surface_area, 2)
        print(f'{can[0]} {storage_efficiency}')


def compute_volume(radius: float, height: float):
    """
    Computes the volume of a steel can
    Parameters:
        radius: the radius of the steel can
        height: the height of the steel can
    Return: volume of the steel can
    """
    volume = math.pi * (radius ** 2) * height
    return volume


def compute_surface_area(radius: float, height):
    """
    Computes the surface of area of a steel can
    Parameters:
        radius: the radius of the steel can
        height: the height of the steel can
    Return: surface area of the steel can
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


if __name__ == '__main__':
    main()