#!/usr/bin/env python

# Question 1
# Calculate the area of the rectangle
print("Question 1")

length = 25
width = 20
area = length * width
print(f"The area for this rectangle is {area}\n")
# => The area for this rectangle is 500
 
# Question 2
# Calculate the volume of the cuboid
print("Question 2")

length = 6
width = 5
height = 4
volume = length * width * height
print(f"The volume of this cuboid is {volume}\n")
# => The volume of this cuboid is 120
 
# Question 3
# Calculate the average of 3 numbers
print("Question 3")

n1 = 8
n2 = 10
n3 = 12
avg = (n1 + n2 + n3) /3
print(f"The average for the 3 numbers is {avg}\n")
# => The average for the 3 numbers is 10.0

# Question 4
# Calculate the BMI
print("Question 4")

weight = 80
height = 1.62
bmi = weight / (height ** 2)
bmi_dec_point=  format(bmi, ".2f")
print(f"The BMI is {bmi}")
print(f"The BMI in 2 decimal points in {bmi_dec_point}\n")
# => The BMI is 30.48315805517451
# => The BMI in 2 decimal points in 30.48

# Question 5
# Calculate the total
print("Question 5")

amt = 5
price = 4.50
total = amt * price
print(f"The total is {total}\n")
# => The total is 22.5
 
# Question 6
# Calculate the amount of days
print("Question 6")

week = 5 
day_count = week * 7 
print(f"There are {day_count} days in 5 weeks\n") 
 
# Question 7
# Calculate the power of 2 of a number
print("Question 7")

number = 5
power_of_2 = number ** 2
print(f"The power of 2 of 5 is {power_of_2}\n")
# => The power of 2 of 5 is 25

# Question 8
# Calculate the speed
print("Question 8")

distance = 15
time = 3
speed = distance / time
print(f"The speed is {speed}\n")
# => The speed is 5.0

# Question 9
# The area of a trapezium
print("Question 9")

a = 5
b = 3
height = 6
area = 1 / 2 * (a + b) * height
print(f"The are for this trapezium is {area}\n")
# => The are for this trapezium is 24.0

# Question 10
# Calculate the volume of a sphere
print("Question 10")

radius = 5 
volume = 4 / 3 * __import__("math").pi * radius ** 3
print(f"The volume of this sphere is {volume}")
# => The volume of this sphere is 523.5987755982989