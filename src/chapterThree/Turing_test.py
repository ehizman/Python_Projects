input("What is your problem?: ")

answer: str = input("Have you had this problem before (yes or no)?: ").upper()
if answer == "YES":
    print("Well, you have it again")
else:
    if answer == "NO":
        print("Well, you have it now")
    else:
        print("Invalid input")