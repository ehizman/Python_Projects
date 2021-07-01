import sys


def calculate_bmi_using_american_standards():
    weight_in_kilogram = float(input("Enter your weight in kilograms: "))
    height_in_meters = float(input("Enter your height in meters: "))
    bmi = weight_in_kilogram / (height_in_meters ** 2)
    print(f"Your bmi is %.2f" % bmi)
    display_bmi_chart()
    main()


def display_bmi_chart():
    print("""
        BMI VALUES
        Underweight : less than 18.5
        Normal : between 18.5 and 24.9
        Overweight: between 25 and 29.9
        Obese: 30 or greater""")
    main()


def calculate_bmi_using_english_standards():
    weight_in_pounds = float(input("Enter your weight in pounds: "))
    height_in_inches = float(input("Enter your height in inches: "))
    bmi = (weight_in_pounds * 703) / (height_in_inches ** 2)
    print(f"Your bmi is %.2f" % bmi)
    display_bmi_chart()


def application_options(user_input):
    switcher = {
        1: calculate_bmi_using_american_standards,
        2: calculate_bmi_using_english_standards,
        3: sys.exit
    }
    return switcher.get(user_input, "Invalid user input")()


def main():
    user_input: int = int(input("""
    Welcome to BMI Calculator
    Press 1 to calculate BMI using American standards
    Press 2 to calculate BMI using English standards
    Press 3 to exit application -> """))
    application_options(user_input)


if __name__ == "__main__":
    main()
