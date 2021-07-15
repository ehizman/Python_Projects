current_world_population: float = 7900000000
current_world_population_growth_rate: float = 1.05/100
print("Current world population: {:,}".format(current_world_population))
print("Current population growth rate: 1.05%")

for i in range(100):
    current_world_population = (current_world_population * ((current_world_population_growth_rate + 1) ** (i + 1)))
    print("World population after {} years is {:,.2f}".format(i+1, current_world_population))