# Maximun sum of pyramid of numbers

Imagine that you have a pyramid built of numbers, like this one here:   

`````python
"""
   /3/
  \7\ 4
 2 \4\ 6
8 5 \9\ 3
"""
`````



The maximum sum of consecutive numbers from the top to the bottom of the pyramid  is `3 + 7 + 4 + 9 = 23`. Your job is to develop an algorithm that finds the maximun sum of a path within the pyramid.

**Important: ** forget about brute force. That is not the goal with this exercise.

Here is a test you would need to pass:

`longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) #23`



**How to solve this challenge without brute force?**

One may think that the best starting point for solving this challenge, would be the tip of the pyramid. From there, we'll find all possible paths, from top to bottom, with their respective sums. At each sum, will keep the greatest one. 

Well, this approach will make use of recursion. If the pyramid is very long, there are going to be lots of paths that could lead to nowhere. Hence, making this approach not optimal. Let's explore a different approach.

Instead of going top to bottom, we could start from the bottom. We'll keep only the paths that from the very bottom indicate that have a greater sum than their counterparts. Let's see it more clearly:

`````python
"""
   3
  7 4
 2 4 6
8 5 9 3

Step 1:

                       3            ...
                      7 4           (n - 2)
start here -->       2 4 6          (n - 1)
                    8 5 9 3         (n)

From that starting point, we'll calculate the greatest sum path between
the array of (n-1) and the array of (n).

                       3            ...
                      7 4           (n - 2)
start here -->       2 4 6          (n - 1)
            (10 7), (9 13), (15 9)    (n)

Here, we just made a sum of elements from (n-1) with (n). For instance,
2 --> 2 + 8 = 10; 2 + 5 = 7
4 --> 4 + 5 = 9; 4 + 9 = 13
6 --> 6 + 9 = 15; 6 + 3 = 9

For each possible solution, we need to keep the greatest sum. Hence, the
pyramid will become:

                       3            ...
                      7 4           (n - 2)
                   10 13 15          (n - 1)

Now repeat the same procedure. Let's find the sum of elements first:

                       3            ...
                      7 4           (n - 2)
                (17 20), (17 19)

7 -> 7 + 10 = 17; 7 + 13 = 20
4 -> 4 + 13 = 17; 4 + 15 = 19

After selecting the greatest sum, the pyramid becomes:

                       3            ...
                     20 19           (n - 2)

Las step with same procedure. First, let's find the sum:

                       3            ...
                     20 19           (n - 2)
                    (23 22)

Selecting the greatest sum:

                       23

Going from bottom to top, we sum the elements and keep the path
that give us the greatest sum. Doing that repetitively, we achieve
an efficient solution, recursionless.
"""
`````



Let's continue with the code implementation.

**Solutions**

We'll follow three different approaches to solve this challenge. The first solution would be memory intensive. The second one will reuse the arrays given as arguments, which is more efficient that the first solutions. Finally, we'll see how using the `reduce` method this could be easily solved. Let's begin

*First approach*

We'll start from the array before the last one and, from there, calculate the sum to the top, keeping the greatest sum paths between arrays.

`````python
def longest_slide_down(pyramid):
    # Starting position pointing to the array before the last one
    start = len(pyramid) - 2

    # help us to keep of the sum of two arrays at each iteration
    temp = []

    # Array before the last one, using start calculated above
    curr = pyramid[start]

    # Represents the last array
    # 'curr' and 'below' arrays will effectuate the sum, keeping the greatest
    below = pyramid[start + 1]

    # start == 0 means we reach the top
    while start >= 0:

        # 'enumerate' is a useful tool in such that give us an index 'i'
        # as well as the value of the array that being iterated
        for i, val in enumerate(curr):
            # within 'temp' array, we keep the maximum sum between
            # the last two arrays being compared. We do this with
            # every element of curr
            temp.append(max(val + below[i], val + below[i+1]))

        # we'll help us escalating to the top
        start -= 1
        # 'curr' is one array above the previous one
        curr = pyramid[start]

        # 'below' becomes the new array that has the sum of two previous arrays
        # for which the max has been kept
        below = temp

        temp = []

    # since 'below' will end up as an array of one element
    # we retrieve it by calling index 0
    return below[0]
`````





*Second approach*

For this approach to be fully understood, let's see how `.pop()` works:

`````python
"""
arr = [1, 2, 3]
print(arr.pop()) #3
print(arr) # [1, 2]

As you can see, '.pop()' will remove the last element of the array.
In addition to that, it will return the removed element.

If you have an empty array that does '.pop()', it will throw an error:

[].pop() # IndexError: pop from empty list

Surprisingly, if we put a '.pop()' inside a while loop, that error will be prevented.

arr = [1, 2, 3]
while arr:
    print(arr.pop())
print(arr)

# 3
# 2
# 1
# []

That is because after the 3rd iteration, 'arr' will become an empty array '[]'.
For the while loop, [] is like False. Hence, leaving the loop.
"""
`````



Whit that in mind, let's proceed with the 2nd-approach solution:

`````python
def longest_slide_down(pyramid):

    # since 'pyramid' is an array of arrays, with '.pop()'
    # we get the last array.
    # It will represent the last array at each iteration
    res = pyramid.pop()

    # keep iterating until 'pyramid' becomes an empty array
    # 'pyramid' will become empty since '.pop()' is applied several times
    while pyramid:

        # 'tmp' will hold the data of one array above 'res'
        tmp = pyramid.pop()

        # This line has two parts: one iterated over temp and the other one
        # sums the greatest path between two arrays within the pyramid.
        # First part is: [... for i in range(len(tmp))] By doing this in Python,
        # we are able to create a new array as the result of iterating over 'range(len(temp))'
        # Second part is: [tmp[i] + max(res[i], res[i + 1]) ...] This specifies what is going
        # inside the newly created array after iterating the through the First part.
        # Important: 'res' keeps the greatest sum between arrays 'tmp' and 'res'.
        # 'res' keeps that greatest sum for the next iteration. At the next iteration, 'tmp'
        # will get one array up within the 'pyramid' of arrays. Do that enough times to reach the top.
        res = [tmp[i] + max(res[i], res[i + 1]) for i in range(len(tmp))]

    # 'res' will keep the shape of an array. After reaching the top
    # 'res' has one single element that need to be '.pop()' to get it.
    return res.pop()
`````



*Third approach*

Let's review a bit about `reduce(function, iterable)` function before proceeding with the solutions. This approach could be the most the elegant if we get the concepts right. Let's see:

`````python
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
`````



With the foundations explained, let's proceed with the most elegant solution of this coding challenge:

`````python
from functools import reduce


# The returned value of 'back_slide' will become 'prev_array'
# in the next iteration.
# At first, we only take the last two arrays of 'pyramid'.
# After we calculate the greatest path between those two
# arrays, that same result is represented by 'prev_array'
# and computed again
# The 'reduce' method will keep iterating from left to right
# over all elements of 'pyramid'
def back_slide(last_array, prev_array):
    return [
        prev_array[i] + max(last_array[i], last_array[i + 1])
        # Once we have two arrays of 'pyramid' we iterate over
        # the above array from left to right.
        for i in range(len(prev_array))
    ]


def longest_slide_down(pyramid):
    # 'reversed' method reverses 'pyramid'. Required since
    # 'reduce' method goes from left to right.
    # Since all elements of 'pyramid' are arrays, reduce also
    # will produce an array. Its first value is obtained via [0].
    return reduce(back_slide, reversed(pyramid))[0]
`````
