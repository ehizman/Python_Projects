if __name__ == "__main__":
    total_miles_driven_per_day: float = float(input("Enter the total number of miles driven per day: "))
    cost_per_gallon_of_gasoline = float(input("Enter the cost per gallon of gasoline: "))
    average_miles_per_gallon: float = float(input("Enter the average miles covered per gallon of gasoline: "))
    parking_fees_per_day: float = float(input("Enter the parking fees per day: "))
    tolls_per_day: float = float(input("Enter the tolls per day: "))

    average_number_of_gallons_of_gasoline_used_per_day: float = total_miles_driven_per_day / average_miles_per_gallon
    cost_per_day_of_driving_to_work: float = (average_number_of_gallons_of_gasoline_used_per_day * cost_per_gallon_of_gasoline) + parking_fees_per_day + tolls_per_day

    print("user's cost per day of driving to work: %.2f" % cost_per_day_of_driving_to_work)