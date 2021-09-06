from functools import reduce


# 'my_add': function to be applied to the iterable object
# with which 'reduce' is called.
def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


# Iterable object
numbers = [0, 1, 2, 3, 4]

reduce(my_add, numbers)
"""
Logs
a + b
0 + 1 = 1 -> This '1' become 'a' in the next iteration
1 + 2 = 3 -> This '3' become 'a' in the next iteration
3 + 3 = 6 -> This '6' become 'a' in the next iteration
6 + 4 = 10
10

What's happening here?
1. 'reduce' receives two mandatory arguments and one optional
    First, it will receive the function to be applied to the 
    iterable object.
    Second, receives the iterable object.
    Finally, it could or could not receive an Initializer value
2.  As you can see from the Logs above, 'my_add' function will take
    the two values of 'numbers' at each time. Not only that. Each 
    iteration produce a result. This result becomes one of the two values
    for the next iteration. That means we are building up at the result
    of the previous iteration
"""
