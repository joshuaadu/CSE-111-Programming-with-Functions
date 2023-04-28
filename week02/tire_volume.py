from math import pi
from datetime import datetime


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

    volume = round((pi * (width ** 2) * (aspect_ratio * ((width * aspect_ratio) + (2540 * diameter)))) / 10000000000)

    print(f"\nThe approximate volume is {volume, 2} liters")
    save_data(width, aspect_ratio, diameter, volume)
    # print(width, aspect_ratio, diameter)


def save_data(width: int, aspect_ratio: int, diameter: int, volume: float):
    """
    Appends to the end of the volumes.txt file one line of text that contains the following five values:
current date
width of the tire
aspect ratio of the tire
diameter of the wheel
volume of the tire
    """
    with open("volumes.txt", "+a") as file:
        if len(list(file)) == 0:
            file.write("Date, Width, Aspect ratio, Diameter, Volume\n")
        date = datetime.today()
        file.write(f"{str(date)}, {width}, {aspect_ratio}, {diameter}, {volume},")


if __name__ == "__main__":
    calculate_tire_volume()
    # print(heart_rate_calculator.__doc__)