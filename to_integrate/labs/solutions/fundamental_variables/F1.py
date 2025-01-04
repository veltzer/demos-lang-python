#! /usr/local/bin/python

# This race requires 45 laps. How much fuel is required?
fuel_per_lap = 2.25
laps = 45
fuel_requirement = laps * fuel_per_lap

# Typically, a car will carry an extra 50% for contingency.
fuel = fuel_requirement * 1.5
print("Full fuel load:", fuel, "kg")

# The qualifying lap time was 80.45 seconds.
# However, that was with only 5kg of fuel.
# Each 10 kg of fuel decreases the lap time by 0.35 seconds.

q_lap_time = 80.45

# Theoretical initial lap time.
t_lap_time = q_lap_time - (0.35/10) * 5

print("Theoretical initial lap time:", t_lap_time)

lap_one_time = t_lap_time + ((fuel/10) * 0.35)
print("Lap one time:", lap_one_time, "seconds")



