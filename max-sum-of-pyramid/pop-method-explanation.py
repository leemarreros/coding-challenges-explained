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
