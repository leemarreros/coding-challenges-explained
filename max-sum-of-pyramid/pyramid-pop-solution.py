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
