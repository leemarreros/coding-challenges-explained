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
