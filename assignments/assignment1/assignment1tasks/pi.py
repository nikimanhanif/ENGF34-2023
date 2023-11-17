import random
import math

def estimate_pi(precision):
    inside_circle = 0
    total_points = 0

    while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            inside_circle += 1

        total_points += 1

        current_pi_approximation = 4 * inside_circle / total_points

        if math.isclose(current_pi_approximation, math.pi, rel_tol=10**(-precision)):
            return round(current_pi_approximation, precision)


precision = 10 # Set the desired precision (number of decimal places)
estimated_pi = estimate_pi(precision)
print(f"Estimated pi with {precision} decimal places: {estimated_pi}")
