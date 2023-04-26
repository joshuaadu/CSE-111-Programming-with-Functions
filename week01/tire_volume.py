from math import pi


def calculate_tire_volume():
    """
    Calculate the volume of space inside a tire
    v is the volume in liters,
    π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
    w is the width of the tire in millimeters,
    a is the aspect ratio of the tire, and
    d is the diameter of the wheel in inches.

    """

    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = (pi * (width ** 2) * (aspect_ratio * ((width * aspect_ratio) + (2540 * diameter)))) / 10000000000
    
    print(f"\nThe approximate volume is {round(volume, 2)} liters")
    # print(width, aspect_ratio, diameter)




if __name__ == "__main__":
    calculate_tire_volume()
    # print(heart_rate_calculator.__doc__)