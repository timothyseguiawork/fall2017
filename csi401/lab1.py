# Lab 1
# Group 1: Timothy, Junna, Brian, and Deanna.
# 08.31.17

# Task 0.5.1
# Use Python to find the number of minutes within a week.
print (("There are: ") + str(7*24*60) + (" minutes in a week."))
# must call str() procedure when concatenating ints and strings

# Task 0.5.2
# Use python to find the remainder of 2304811 divided by 47 without modulus.
# Hint: use //
# print (2304811 % 47)
x = int(2304811-(2304811//47)*47)
print ("The remainder of 2304811/47 is: "+str(x))

# Task 0.5.3
# Enter a boolean expression to test whether the sum of 673 and 909 is divisible
# by 3.
x = 673+909
# print (x)
if (x%3 == 0):
    print (str(x) + " is divisible by three.")
else:
    print (str(x) + " is not divisible by three.")

# Task 0.5.4
# Assign the value -9 to x and 1/2 to y. Predict the value of the expression and then enter it ot check your prediction.
x = -9
y = 1/2
print(2**(y+1/2) if x+10<0 else 2**(y-1/2))
# python evaluates the first condition; depending on whether it is true or false.
#   then evaluates first or second and then uses the result as the result of the entire
#   conditional expression

# Set Creation
#   This is a set:
#       {1, 2, 3} or {1+2, 2, 3, "a"}
#   Just like in set theory, duplicates are deleted.
#   Cardinality or length is represented as the procedure:
#       len({insert set elements})
#   sum of a set:
#       sum({insert set values})
#       sum({1,2,3}, 10)
#   Checking memberships: in
#       S={1,2,3}
#         2 in S
#         True
#   Union: |
#   Intersection: &
#   Mutating a set:
#       Removing:
#           S.remove(2)
#       Adding:
#           S.add(4)
#       Adding another set:
#           S.update({4,5,6})
#       Intersecting a set with another collection, removing from the set all elements not in the collection.
#           S.intersection_update({5,6,7,8,9})
#           S becomes {5,6}
#       Two variables can point to the same value and can both manipulate the set.
#           T=S
#           T.remove(5)
#           S becomes {6}
#       Python has the ability to copy a set rather than having it point to the same data
#           U=S.copy()
#           U.add(5)
#           U becomes {5,6}
#              Now changes to U won't change S at all.
#       Set Comprehensions:
#           {2*x for x in {1,2,3}}
#           This results in {2, 4, 6}

# Task 0.5.5
# Write a comprehension over {1,2,3,4,5} whose value is the set containing the squares of the first 5 positive integers.
print("A comprehension over {1,2,3,4,5} whose value is the set containing")
print("     the squares of the first 5 positive integers: "+ str({x**2 for x in {1,2,3,4,5}}))

# Task 0.5.6
# Write a comprehension over {0,1,2,3,4} whose value is the set consiting of the first five powers of 2, starting with 2^0
print ("A comprehension over {0,1,2,3,4} whose value is the set consisting")
print ("     of the first five powers of 2, starting with 2^0: "+str({2**x for x in {0,1,2,3,4}}))

#   Using the union (|) and intersection (&) operators you can write set expressions for the union or intersection of two sets
#   and use the expressions in a comprehension.
S = {1,3}
print({x*x for x in S | {5,7}})
#   prints out {1, 49, 9, 25}

#   By adding the phrase if <condition> at the end of the comprehension (before the closing brace "}") you can skip some of the
#       values being iterated over.
print({x*x for x in S | {5,7} if x > 2})
#   In this case the conditional clause acts as a filter.

#   The cartesian product of two sets.
print({x*y for x in {1,2,3} for y in {2,3,4}})

# Continue from page 7 Tomorrow
# WORK 
