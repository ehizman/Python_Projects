import sys

list_of_inputs = list()
counter: int = 0
while counter < 3:
    try:
        user_input: int = int(input(f"Enter a number {counter + 1}: "))
        print("number added to list successfully!")
    except ValueError as e:
        print("Oops!", e.__class__, "occurred")
        print("please re- enter input!")
    else:
        list_of_inputs.append(user_input)
        counter = counter + 1

print(f"The maximum of {list_of_inputs} is {max(list_of_inputs)}")
