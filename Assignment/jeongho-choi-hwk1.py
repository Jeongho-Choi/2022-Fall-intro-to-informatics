#Question 1
#Assigning values
print("Question 1: Calculate the maximum number of small rectangles that can fit into a larger rectangle")

large_length = input("Please input the length of a large rectangle: ")
large_length = float(large_length)

large_height = input("Please input the height of a large rectangle: ")
large_height = float(large_height)

small_length = input("Please input the length of a small rectangle: ")
small_length = float(small_length)

small_height = input("Please input the height of a small rectangle: ")
small_height = float(small_height)

#Calculate the maximum number of small rectangles
num_length = large_length//small_length
num_height = large_height//small_height

num_rec = num_length * num_height

#Print the result
print('Answer: The number of small rectangles of length {:.2f}'.format(small_length) \
      +' inches and height {:.2f}'.format(small_height) \
      +' inches that fit into a large rectangle of length {:.2f}'.format(large_length) \
      +' inches and height {:.2f}'.format(large_height) \
      +' inches is {:.0f}'.format(num_rec))

#Question2
import math
print("Question 2: Find the length of the hypotenuse given the base and the height of a right-angled triangle")

base = input("Please input the base of a right-angled triangle: ")
base = float(base)

height = input("Please input the height of a right-angled triangle: ")
height = float(height)

#Calculate the hypothenuse
hypo_2 = base**2+height**2
hypo = math.sqrt(hypo_2)

#Print the result
print('Answer: The hypotenuse of a right-angled triangle of base {:.2f}'.format(base) \
      +' feet and height {:.2f}'.format(height) \
      +' feet is {:.4f}'.format(hypo) \
      +' feet')

input("Press enter to exit ")
