#1
import math

degree = 15
radian = degree * (math.pi / 180)

print("Output radian:", round(radian, 6))

#This program converts degrees to radians using the formula:
#radians = degrees × π / 180.
#math.pi provides the value of π.
#Output: 0.261799 (≈ 0.261904 depending on rounding)


#2
height = 5
base1 = 5
base2 = 6

area = (base1 + base2) * height / 2

print("Expected Output:", area)

#This program calculates trapezoid area using the formula.
#Output: 27.5


#3
import math

n = 4
s = 25

area = (n * s**2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", int(area))

#This program calculates the area of a regular polygon.
#Uses math.tan() and math.pi.
#Output: 625


#4
base = 5
height = 6

area = base * height

print("Expected Output:", float(area))

#This program calculates parallelogram area using base × height.
#Output: 30.0



# min() / max() — find smallest / largest value
# abs() — absolute value
# round() — round a number to nearest integer
# pow(a, b) — a raised to the power b

# sqrt() — square root
# ceil() / floor() — round up / down
# sin(), cos() — trigonometric functions
# pi, e — mathematical constants

# random() — random float 0 ≤ x < 1
# randint(a, b) — random integer between a and b
# choice(seq) — random element from sequence
# shuffle(seq) — shuffle a list in place
