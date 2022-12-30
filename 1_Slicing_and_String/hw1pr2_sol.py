# Using built-in functions
# First, try out some of Python's many built-in functions. These will not go into your hw1pr2.py file:

# In [1]: list(range(0, 100))
# Out[1]: [0, 1, 2, ..., 99]
# range returns an iterator (or generator) of integers. (Don't worry if you're not quite sure what an "iterator" is; the important thing is that list turns the iterator into a list of integers.)
# Note that when you use range, as with almost everything in Python, the right endpoint is omitted!

# In [2]: sum(range(3, 11))
# Out[2]: 52
# sum sums a list of numbers, and range creates a list of integers.

# In [3]: sum([40, 2])
# Out[3]: 42
# a roundabout way of adding 40 + 2

# In [3]: abs(-42)
# Out[3]: 42
# abs is built-in function that finds the absolute value: abs(-42) returns 42

# In [4]: help(abs)
# (an explanation of abs)
# help is a good thing—ask for it by name!
# Depending on your computer, you may need to hit the space bar to see all the help, and hit q to leave the help interface…

# In [5]: import math
# You do need to import math first...or else you'll get an error!

# In [6]: dir(math)
# (All of the functions in the math library...)

# This dir command is often useful—it lists everything from a particular library (or module, as it's often called).

# There are many modules (libraries) of functions available for you to use as part of Anaconda Python, and many more that are available for download beyond that foundation.

# Run your file
# When you run this file in the usual way:

# run hw1pr2.py
# you won't see anything! However, your newly defined function, dbl is now available for you to use.

# From here, try using the newly defined dbl function:

# In [1]: dbl(21)
# Out[1]: 42

# In [2]: dbl('wow! ')
# Out[2]: 'wow! wow! '

# Signature and Docstring
# The first line of a Python function is called its signature. The function signature includes the keyword def, the name of the function, and a parenthesized list of arguments to the function.

# Docstring Directly underneath the signature is a string inside triple quotes """—this is called the docstring, short for "documentation string."

# A docstring should describe the function's arguments and result (return value). As you see above, it may include other important information, too. Docstrings are how your functions become part of Python's built-in help system.

# To see this, type

# In [2]: help(dbl)

# and you will see that Python provides the docstring as the help! The language's help system is docstrings! This self-documenting feature in Python is especially important for making your functions understandable, both to others and to yourself. Remember to exit you want to hit q.

# Important Warning: the first set of triple quotes of a docstring needs to be indented underneath the function definition def line, at the same level of indentation as the rest of block of code that defines the function.



# Example problem: Write the function tpl(x), which accepts a numeric argument and returns three times that argument.
# Problem 0 (given):
def tpl(x):
  """
  output: tpl returns thrice its input
  input x: a number (int or float)
  """
  return 3*x

# Problem 1: Write the function sq(x) that should accept a numeric argument named x. Then, sq should return the square of its argument.
# Note that this is the square, not the square root. (The square is x times itself...)

def sq(x):
  """
  output: square of its input
  input x: a number (int or float)
  """
  return x ** x

# Problem 2
# The function interp(low, hi, fraction) accepts three numbers as its input arguments: low, hi, and fraction, and by definition,
#    interp(low, hi, fraction) should return the floating-point value that is fraction of the way between low and hi.

# You might use a pencil and paper to diagram this out; perhaps start by drawing a number line.

# As an example, consider interp(1, 9, .25), which means

# You started at location 1
# You will finish at location 9
# You have traversed one-quarter, 0.25, of the journey so far
# The interp function should return your location now,    one-quarter of the way from 1 to 9.

# Do you see why the correct result for interp(1, 9, .25) is 3 ?
# Take a moment to convince yourself—or ask & chat about it!

# Once you see why the correct result of interp(1, 9, .25) is 3 , then
# Try to describe the same process using the variable names:
# low, the "start point"
# hi, the "end point"
# fraction, the fraction traversed so far...
# From the above description, it might feel tempting to divide this function into several cases and use if, elif, and the like. Yet this function can be written using no conditional (if/elif/else) constructions at all! Try it without using if!

# With the examples below, try your function when fraction is less than zero or greater than one. In those cases, it's extrapolating rather than interpolating. We'll stick with the name interp anyway!


# Here are more examples to clarify how interp works:


# In [1]: interp(1.0, 9.0, 0.25)      # A quarter (.25) of the way from 1.0 to 9.0
# Out[1]: 3.0

# In [2]: interp(1.0, 3.0, 0.25)      # A quarter of the way from 1.0 to 3.0
# Out[2]: 1.5

# In [3]: interp(2, 12, 0.22)         # 22% of the way from 2 to 12
# Out[3]: 4.2

# Here are two more examples to try:


# In [1]: interp(24, 42, 0.0)         # 0% of the way from 24 to 42
# Out[1]: 24.0

# In [2]: interp(102, 117, -4.0)      # -400% of the way from 102 to 117 (whoa!)
# Out[2]: 42.0
# The next several functions involve strings of characters. Write each one in your hw1pr2.py file. 
# After you write each function, be sure to test it before moving on to the next one! 
# Also, be sure to include a docstring for each function that tells (very briefly) what it does.

def interp(low, hi, fraction):
  """
  output: floating-point value that is fraction of the way between low and hi
  input low: number
  input hi: number
  input fraction: floating-point value
  """
  return low + ((hi - low) * fraction)

# Problem 3
# Write a function checkends(s), which takes in a string s and returns True if the first character in s is the same as the last character in s. It returns False otherwise. The checkends function does not have to work on the empty string (the string '').

# There is a hint below, but read through the examples first!

# These examples will help explain checkends—read them over now, and be sure to try them once you have a first draft of your function. Notice that the fourth, final example below is the string of one space character, which is different from the empty string, which contains no characters:

# In [1]: checkends('no match')
# Out[1]: False

# In [2]: checkends('hah! a match')
# Out[2]: True

# In [3]: checkends('q')
# Out[3]: True

# In [4]: checkends(' ')
# Out[4]: True
# Make sure to check that this last example (the string of a single space) works for your checkends function. The empty string does not need to work.

# Warning! Your function should not return strings! Rather, it should return a boolean value, either True or False, without any quotes around them. True and False are keywords recognized by Python as representing one bit of information.

# You'll see these Booleans turn a different color (blue in VSCode's default color scheme) indicating that Python recognizes them as bool values. (If you'd accidentally made them strings, they'd be quoted, and they'd be orange in VSCode.) 
# In sum, Booleans and strings are different. For True and False you would almost always want the unquoted Boolean values.

#HINT
# For this function you could use an if and else construction...here is a start:

#     if s[0] == ______ :
#         return True
#     else:
#         return False

# Notice that the last character is missing above—you'll need to fill that in!
# You might find a solution that doesn't use the if and else at all—this is fine, too.

# The expression s[-1] represents the last element in the string s.

def checkends(s):
  """
  output: boolean indicating whether first and last characters are the same
  input s: string
  """
  return s[0] == s[-1]

# Problem 4
# Write a function flipside(s), which accepts a string s and returns a string whose first half is s's second half and whose second half is s's first half. If len(s) (the length of s) is odd, the "first half" of s is considered to have one fewer character than the second half. (Accordingly, the second half of the returned string will be one shorter than the first half in these cases.) There's also a hint after the examples below.

# Here you may want to use the built-in function len(s), which returns the length of its argument string, s.


# Examples:

# In [1]: flipside('homework')
# Out[1]: workhome

# In [2]: flipside('carpets')
# Out[2]: petscar
# Hint
# This function is simpler if you create a variable equal to len(s)//2 on the first line, e.g.,

# def flipside(s):
#     """Put your docstring here.
#     """
#     x = len(s)//2
#     return   _____________
# where the return statement has been left up to you. It will use the variable x twice , which is why it's nice to give it a name, rather than type and re-type it!
# Side comment: the name x is a pretty poor one in this case; l (for "length") might be better. We didn't suggest l because it looks too much like the number 1. What name might be better than both x and l? Remember that Python allows multi-letter names, and that len is already used!

def flipside(s):
  """
  output: string whose first half is s's second half and whose second half if s's first half
  input s: string
  """
  x = len(s) / 2
  return s[x:] + s[:x]

# Problem 5
# Here, s is an integer, not a string, argument.

# Write convertFromSeconds(s), which takes in a nonnegative integer number of seconds s and returns a list (we'll call it L) of four nonnegative integers that represents that number of seconds in more conventional units of time, such that:

# The initial element represents a number of days.
# The next element represents a number of hours.
# The next element represents a number of minutes.
# The final one represents a number of seconds.
# You should be sure that
# 0 ≤ seconds < 60
# (i.e., the maximum should be 59!)
# 0 ≤ minutes < 60
# 0 ≤ hours < 24
# There are no limits on the number of days.

# For instance,

# In [1]: convertFromSeconds(610)
# Out[1]: [0, 0, 10, 10]

# In [2]: convertFromSeconds(100000)
# Out[2]: [1, 3, 46, 40]
  

# How to do this?    Feel free to copy and paste this starter code that uses four variables:
# def convertFromSeconds(s):
#     days = s // (24*60*60)  # Number of days
#     s = s % (24*60*60)      # The leftover
#     hours = 
#     minutes = 
#     seconds = 
#     return [days, hours, minutes, seconds]

# The idea here is that when those four variables are all correctly set, you can return them all in a list, which is the final line:
#     return [days, hours, minutes, seconds]

# For instance, the line that sets days is
#     days = s // (24*60*60)

# What would be other lines be?
# It's possible to do this without changing the variable s at all. However, as the above starting code suggests, it's also possible to alter s as you go (and your code will be simpler as a result). Try this latter approach, just to get the hang of this powerful strategy.

def convertFromSeconds(s):
  """
  output: list of four nonnegative integers that represent the input in conventional units of time
  input s: nonnegative integer representing number of seconds
  """
  days = s / (24*60*60)  # # of days
  s = s % (24*60*60)     # the leftover
  hours = s / (60 * 60)
  s = s % (60 * 60)
  minutes = s / 60
  seconds = s % 60
  return [days, hours, minutes, seconds]