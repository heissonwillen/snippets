from math import pi

def estimate_pi(n):
	arctan_1 = 0
	for i in range(n):
		arctan_1 += ((-1)**i)/(i*2+1)

		# if i%100000 == 0:
		# 	print(i, abs(pi-4*arctan_1))

	return arctan_1*4

print(estimate_pi(int(10e5)))