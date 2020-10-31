from random import uniform
from math import pi

def estimate_pi(n):
	num_points_circle = 0
	total_points = 0

	for i in range(n):
		x = uniform(0, 1)
		y = uniform(0, 1)

		distance = x**2 + y**2

		if distance <= 1:
			num_points_circle += 1
		total_points += 1

		if i%100000 == 0:
			print(i, abs(pi-4*num_points_circle/total_points))

	return 4*num_points_circle/total_points

print(estimate_pi(int(10e10)))