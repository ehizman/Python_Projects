def main():
    current_world_population: int = int(input("Enter the current world population -> "))
    world_population_growth_rate: float = float(input("Enter the current world population -> "))

    for i in range(5):
        print("World population after year %d -> " % (i + 1), end=" ")
        print("%.2f" % (current_world_population * (100 + world_population_growth_rate) ** (i + 1)))


if __name__ == "__main__":
    main()
