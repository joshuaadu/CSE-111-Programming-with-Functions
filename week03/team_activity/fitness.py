# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ")
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight in U.S. pounds: "))
    height = float(input("Enter your height in U.S. inches: "))

    # Call the compute_age, kg_from_lb, cm_from_in,
    years = compute_age(birth_str)
    weight_in_kg = kg_from_lb(pounds)
    height_in_cm = cm_from_in(height)

    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    bmx = body_mass_index(weight=weight_in_kg, height=height_in_cm)
    bmr = basal_metabolic_rate(age=years, gender=gender, height=height_in_cm, weight=weight_in_kg)

    # Print the results for the user to see.
    print(f"Age (years): {years}")
    print(f"Weight (kg): {weight_in_kg:.2f}")
    print(f"Height (cm): {height_in_cm:.1f}")
    print(f"Body mass index: {bmx:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")


def compute_age(birth_str: str):
    """Compute and return a person's age in years.

    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD

    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    print(birthdate)
    print(today)

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds: float):
    """Convert a mass in pounds to kilograms (1 lb = 0.45359237 kg).

    Parameter pounds: a mass in U.S. pounds.

    Return: the mass in kilograms.
    """
    kg = pounds * 0.45359237
    return kg


def cm_from_in(inches: float):
    """Convert a length in inches to centimeters (1 in = 2.54 cm).

    Parameter inches: a length in inches.

    Return: the length in centimeters.
    """
    cm = inches * 2.54
    return cm


def body_mass_index(weight: float, height: float):
    """Compute and return a person's body mass index.

    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.

    Return: a person's body mass index.
    """
    return weight / (height ** 2) * 10000


def basal_metabolic_rate(gender: str, weight: float, height: float, age: int ) -> float:
    """Compute and return a person's basal metabolic rate.

    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.

    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.lower() == "f":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height )- (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    return bmr
# Call the main function so that
# this program will start executing.
if __name__ == "__main__":
    main()
    print(basal_metabolic_rate.__annotations__)