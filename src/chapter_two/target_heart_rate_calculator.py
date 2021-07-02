user_age = int(input("Enter your age: "))
maximum_heart_rate = 220 - user_age
print(f"Maximum Heart rate: {maximum_heart_rate} ")
print("Target Heart rate: %.2f - %.2f" % (0.5 * maximum_heart_rate, 0.85 * maximum_heart_rate))

