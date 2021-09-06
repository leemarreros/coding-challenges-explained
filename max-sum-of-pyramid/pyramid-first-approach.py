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
