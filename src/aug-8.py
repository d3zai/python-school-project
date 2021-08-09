#!/usr/bin/env python

# Example 1
print("Example 1")
print("Hello")
print("World\n")
# => Hello
# => World

# Example 2
print("Example 2")
print("Hello", end=" ")
print("World\n")
# => Hello World

# Example 3
print("Example 3")
print("Mon\tTue\tWed")
print("Thu\tFri\tSat\n")
# => Mon     Tue     Wed
# => Thu     Fri     Sat

# Example 4
print("Example 4")
print("1.  2 + 5 = ?\n\nA. 7\nB. 9\nC. 6\n")
# => 1.  2 + 5 = ?
# =>
# =>
# => A. 7
# => A. 7
# => C. 6

# Example 5
print("Example 5")
print("Ali said, \"I want to learn mathematics\"")
print('Ali said, "I want to learn mathematics"\n') # (Single quotes)
# => Ali said, "I want to learn mathematics"
# => Ali said, "I want to learn mathematics"

# Example 6
print("Example 6")
day = 1
month = 19
year = 2015

print(day, month, year, sep="/", end="\n\n")
# => 1/19/2015

# Example 7
print("Example 7")
name = "Farish"

for i in name:
  print(i)

# => F
# => a
# => r
# => i
# => s
# => h