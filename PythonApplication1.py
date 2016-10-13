#########################################
#               Functions               #
#########################################
###Review###
#Review: Functions
def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

###Review: Built-In Functions###
def distance_from_zero(arg1):
    print (type(arg1))
    if type(arg1) == int or type(arg1) == float:
        return abs(arg1)
    else:
        return "Nope"

print (distance_from_zero(-10))

#Introduction to Functions
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print ("With tax: %f" % bill)
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print ("With tip: %f" % bill)
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

###Function Syntax###
def square(n):
    #Returns the square of a number.
    squared = n**2
    print ("%d squared is %d." % (n, squared))
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)

def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print ("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)  # Add your arguments here!

def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2

#Practice Makes Perfect
def cube(number):
    return number ** 3
    
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print (by_three(3))

####Importing Modules####
##Generic Imports
# Ask Python to print sqrt(25) on line 3.
import math
print (math.sqrt(25))

##Function Imports
# Import *just* the sqrt function from math on line 3!
#from math import sqrt

# Import *everything* from the math module on line 3!
#from math import *

###Built-In Functions###
##On Beyond Strings##
def biggest_number(*args):
    print (max(args))
    return max(args)
    
def smallest_number(*args):
    print (min(args))
    return min(args)

def distance_from_zero(arg):
    print (abs(arg))
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

##max()
# Set maximum to the max value of any set of numbers on line 3!
maximum = max(1,2,3)
print (maximum)

##min()
# Set minimum to the min value of any set of numbers on line 3!
minimum = min(1,2,3)
print (minimum)

##abs()
absolute = abs(-42)
print (absolute)

##type()
# Print out the types of an integer, a float,
# and a string on separate lines below.
print (type(42))
print (type(4.2))
print (type('spam'))