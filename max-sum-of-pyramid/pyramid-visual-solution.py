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