# Filename: hw1pr1.py

#declare variables
pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

#TUTORIAL

#LIST INDEXING, e.g., h[0]
# pi[0]
# 3
# The index of list always starts with 0
# pi[2]
# 4

# LIST SLICING
# print(pi[0:6])
# [3, 1, 4, 1, 5, 9]
# pi[0:6] is the same list because it creates a new list with the element 0 to element 5 from pi without skipping any element.
# 
# print(pi[0:6:1])
# The same result is produced because it creates a new list with the element 0 to element 5 from pi by going through all the element one by one.
# 
# print(pi[0:6:2])
# [3, 4, 5]
# The produced list contains the #0, #2, #4 element from pi because pi[0:6:2] is a list that contains every other element from element 0 through 5.
# 
# print(pi[::-1])
# [9, 5, 1, 4, 1, 3]
# The produced list is a reverse of the original list
# 
# print(pi[-3:-1])
# [1, 5]
# The produced list is a list with the 6-3=#3 element to the 6-1=#5 element from pi without skipping any element
#
# Try other variation after you run ipython!

#LIST CONCATENATION, +
#
# print(pi+e)
# [3, 1, 4, 1, 5, 9, 2, 7, 1]
#
#LIST REPETITION, *,
#
# print(e*2)
# [2, 7, 1, 2, 7, 1]

# TASK: Solve 10 problems below.
# Check the answer by running the file using ipython and run hw1pr1.py
# if there is "AssertionError", the answer with arrow is incorrect. Fix them
# if everything is correct, there will be no "AssertionError".

#PART 1: List of numbers

# 0. Use pi and e (or just one!) to create the list [2, 7, 5, 9]. 
# Example problem (problem 0):  [2, 7, 5, 9]

answer0 = e[0:2] + pi[-2:] #This is already correct! Try the next ones.
print("answer0:", answer0)

# 1. Use pi and/or e to create the list [7, 1]. Store this list in the variable answer1.
#How to begin? Again, you're using one or both of pi and e    in this case, to create the list [7, 1]. Similar to above, store this list in the variable answer1. Here is a starting point, to copy and paste:
# Problem 1: creating [7, 1]
answer1 = e[1:2]           # it's not the right answer, but a start...
print("answer1:", answer1)

# 2. Use pi and/or e to create the list [9, 1, 1]. Store this list in the variable answer2.
answer2 = e + pi
print("answer2:", answer2)

# 3. Use pi and/or e to create the list [1, 4, 1, 5, 9]. Store this list in the variable answer3.
answer3 = 0

# 4. Use pi and/or e to create the list [1, 2, 3, 4, 5]. Store this list in the variable answer4.
answer4 = 0

#PART 2: String or list of characters

h = 'harvey'
m = 'mudd'
c = 'college'

# 5. (The example from above)    Create hey and store this string in the variable answer5.   (our best: 3 ops.)
answer5 = 0
# 6. Create collude and store this string in the variable answer6.   (Our best: 5 ops.)
answer6 = 0
# 7. Create arveyudd and store this string in the variable answer7.   (Our best: 3 ops.)
answer7 = 0
# 8. Create hardeharharhar and store this string in the variable answer8.   (Our best: 7 ops.)    using the crazy construction (h+m)[-2:3:-4]
answer8 = 0
# 9. Create legomyego and store this string in the variable answer9.   (Our best: 8 ops.)
answer9 = 0
# 10. Create clearcall and store this string in the variable answer10.   (Our best: 8 ops.)
answer10 = 0

assert answer0 == [2, 7, 5, 9]
assert answer1 == [7, 1]
assert answer2 == [9, 1, 1]
assert answer3 == [1, 4, 1, 5, 9]
assert answer4 == [1, 2, 3, 4, 5]
assert answer5 == "hey"
assert answer6 == "collude"
assert answer7 == "arveyudd"
assert answer8 == "hardeharharhar"
assert answer9 == "legomyego"
assert answer10 == "clearcall"