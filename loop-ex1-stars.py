# Loops help us to do a particular task many times
# Example 1

# The range() function defaults to 0 as a starting value, however it is possible 
# to specify the starting value by adding a parameter: range(a, b, c) which means 
# values from 'a' to 'b' (but not including 'b') and increases by 3 each time

# Let's use a for-loop to create a pretty print:

# total will keep track of the sum of the numbers as they are 
# added

stars = ""
for x in range(1, 10, 1):
  stars = stars + "*" 
  print (stars)

 for x in range(1, 10, 1):
 	stars = stars +"*"
 	print (stars)