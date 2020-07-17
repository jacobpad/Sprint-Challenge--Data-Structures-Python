import time
from bst import BSTNode
import numpy

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []  # Return the list of duplicates in this data structure
# duplicates = list(set(names_1).intersection(set(names_2)))
duplicates = numpy.intersect1d(names_1, names_2)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

print('How many are common:', len(duplicates), '\n')
print('what\'s_common', duplicates)

end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"\nRuntime: {end_time - start_time:.03} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
