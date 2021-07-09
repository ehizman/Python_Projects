def average_miles_per_gallon(number_of_gallons_used, number_of_miles) -> float:
    if number_of_miles < 1 or number_of_gallons_used < 1 or number_of_gallons_used is None or number_of_miles is None:
        raise Exception()
    return round(number_of_miles / number_of_gallons_used, 6)


if __name__ == "__main__":
    try:
        number_of_miles_driven: float = float(
            input("Enter number of miles driven: (Press - 1 to end application) "))
        total_average: float = 0
        count: int = 0
        average_miles_per_gallon_value: float = 0
        while number_of_miles_driven != -1:
            number_of_gallons: float = float(input("Enter the number of gallons utilized: "))
            average_miles_per_gallon_value: float = average_miles_per_gallon(number_of_gallons, number_of_miles_driven)
            total_average += average_miles_per_gallon_value
            count += 1
            print("{}{}".format("The average miles per gallon is: ", average_miles_per_gallon_value))
            print("_____________________________________________________________________________")
            number_of_miles_driven: float = float(
                input("Enter number of miles driven: (Press - 1 to end application) "))
        else:
            if total_average != 0:
                print("The overall average miles/ gallon over {} days is {:.6f}".format(count, total_average/count))

    except (ZeroDivisionError, ValueError) as error:
        print("Invalid parameter")

