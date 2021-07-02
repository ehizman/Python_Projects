list_of_floats = list()
i: int = 0
print("Enter three float point numbers")
while i < 3:
    try:
        user_input = float(input(f"Enter number {i + 1}: "))
    except Exception as error:
        print(error)
    else:
        list_of_floats.append(user_input)
        i = i + 1
print(f"The list is ascending order is {sorted(list_of_floats)}")

