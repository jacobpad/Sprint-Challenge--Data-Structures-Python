"""
It doesn't say how, but it says how not to!
"""


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

duplicates = []  # Return the list of duplicates in this data structure
# duplicates = numpy.intersect1d(names_1, names_2)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# After submission, there's this way to do it - improving the for loop, 
#   but it still isn't as fast as the intersect1d method from numpy.
# 
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

# ----------------------------------------------------------------------------
b_s_tree = BSTNode(names_1[0]) # Instantiate a tree/node with the first name in 
                               # the `name_1` file

# Put all the names in the file in the tree
for n in names_1:
    b_s_tree.insert(n)

duplicates = [n for n in names_2 if b_s_tree.contains(n)]
# ----------------------------------------------------------------------------


print('\nTime complexity: O(n log n)\n')
print('How many are common:', len(duplicates), '\n')
print('What\'s_common', duplicates)

end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"\nRuntime: {end_time - start_time:.03} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
