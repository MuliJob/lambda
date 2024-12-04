# A lambda function is a small
# anonymous function defined using the lambda key word.
# It's often used for short, throwaway functions 
# that are only needed temporarily

# Basic Syntax - The syntax of a lambda function is: "lambda arguments:expression"

# arguments: A comma-separated list of parameters.
# expression: An expression that is evaluated and returned.

from functools import reduce

# Basic Lambda Function:
add = lambda x, y:x+y
print(add(2,3))
# Output = 5

# Here ,lambda x, y:x+y is a lambda function that adds two numbers

# Lambda with map()
numbers = [1,2,3,4,5]
squared = list(map(lambda x:x ** 2, numbers))
print(squared)
# Output = [1, 4, 9, 16, 25]

# map() applies the lambda function to each item in the numbers list.

# Lambda with filter()
numbers = [1,2,3,4,5]
even = list(filter(lambda x:x % 2 == 0, numbers))
print(even)
# Output = [2, 4]

# filter() applies the lambda function to filter even numbers

# Lambda with reduce()
numbers  = [1,2,3,4,5]
product = reduce(lambda x, y:x * y, numbers)
print(product)
# Output = 120

# reduce() applies the lambda function cumulatively to the items in the list

# Pros and Cons

# Pros:
# > Concise and readable
# > Useful for small, simple functions.
# > Handy for functional programming(e.g. map, filter, reduce)

# Cons:
# > Limited to single expression
# > Can the less readable if overused
# > Lack of function name can make debugging harder 

