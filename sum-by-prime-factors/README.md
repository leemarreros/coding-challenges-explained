#  Sum By Factor
===========
**Description:** Given an array I of positive or negative integers such as `I = [i1, ..., in]`, you have to produce a sorted array in which each element is an array of two elements: `[prime number, sum of elements of array I divisible by prime number]`.

####Example
Given `I = [12, 15]` the output: `P = [[2, 12], [3, 27], [5, 15]]`  
Given `I = [15, 21, 24, 30, 45]` the output: `P = [[2, 54], [3, 135], [5, 90], [7, 21]]`  

P will be sorted by increasing order of the prime numbers.   

* * * 

**Solution:** To solve this problem, we'll need to find the prime numbers that are factors of the elements of the array I. Then we calculate the sum of the elements that have the found prime numbers as factors.

1. For this will be important to know how to calculate the prime numbers of a given **N** number. Let'a follow a naive approach at first:

`````python
def is_prime(n):
  # when n is 1 or less than 1:
  if (n <= 1):
    return False
  
  # range(2, n) will iterate until n - 1
  for div in range(2, n):
    # if the modulus of n % div is 0, it means that
    # n is divisible by a given div, which makes it not a prime number
    if (n % div == 0):
      return False

  # True if n was not divisible for the range between 2 to n - 1  
  return True
`````
Output:

`````python
print(isPrime(13)) # True
print(isPrime(15)) # False
print(isPrime(17)) # True
`````

Now it's time to optimize this code. Instead of building a `range(2, n)` we could use the **square root of n** as upper limit for the range - `range(range, n ** 0.5)`. This technique is called *trial division* and it's used for testing wether an integer could be divided by a smaller number.

We'll use this optimization and the previous code to get a list of prime numbers less than a given **n** number. However, this list of prime numbers must also be factors or **n**, because that's the key of the coding challenge.

`````python
def list_prime_factors(n):
  # n could be negatibe so we make it positive.
  # we don't care the sign, only the prime factors
  if (n < 0): n = -n

  # We'll use the data structure 'set'.
  # It will help us to get unique values by default.
  # 'set' uses the '.add' property for adding values to its set.
  # It does it in a way that does not repeat values.
  prime_factors = set()
  
  # If number is a multiple of 2, we only care knowing that its
  # factor is two, other than that we could simplify it.
  while n % 2 == 0:
    prime_factors.add(2)
    n = n / 2
  
  # Optimization technique: square root of 'n' rather than 'n'.
  # Use 'int()' for converting the value to an integer.
  for i in range(3, int(n ** 0.5) + 1):
    # if 'n' is divisible by 'i', 'i' would be a prime factor
    # that is because we are dividing 'n' by 'i' in a while loop leaving only
    # prime factors
    while n % i == 0:
      prime_factors.add(int(i))
      n = n / i
  
  # In case 'n = n / i' is not enough for simplifying 'n' until 1.
  # We conclude that that number 'n' must be a prime number factor
  if n > 2: prime_factors.add(int(n))
  
  # so far 'prime_factors' is a set that looks like this:
  # {3, 5, 7, ...}. To convert a set into an array we could
  # use 'sorted' and get the following [3, 5, 7, ...], which
  # will be more useful later on
  return sorted(prime_factors)  
`````

2. So far, with this function,  we are able to find not only prime numbers but also its factors if a given **n** number. We are half way through. The second part requires to sum all items of the array I that have the found prime numbers as factors. In the next function, (1) we find all prime number factors of the elements of the array **I**. Then, for each prime number factor, we make a sum of all elements of I that have that prime number as factor.

`````python
def sum_wth_prime_factors(I):
    # We are collecting all factor prime numbers from the array I.
    # Since we do not need to repeat the same values, we use a set.
    # Notice that we are passing and array into 'set'. Because of that,
    # we'll use '.update()' instead of '.add()'. '.update()' receive arrays.
    all_prime_factors = set()
    for n in I:
        if not n in all_prime_factors:
            # collecting all prime factors from the array I
            all_prime_factors.update(list_prime_factors(n))
    
    result = []
    for prime in all_prime_factors:
        # Find the sum of the elements of array I that have 'prime' as factor
        # To understand this part, know that with Python you can create
        # arrays in this way: Let's see what's happening here:
        # I.    'for val in I' iterates over all elements of array 'I'
        # II.   Since there is a conditional 'if val % prime == 0', it will select
        #       only those elements that meet that criteria
        # III.  The 'val' on the left of 'for val in I...' is what you will store in the array
        vals_with_prime_factor = [val for val in I if val % prime == 0]
        # IV.   The keyword 'sum()' allows you to sum a complete array
        sum_that_have_prime_factor = sum(vals_with_prime_factor)
        # V.    '[prime, sum]' is the format to return
        prime_and_sum = [prime, sum_that_have_prime_factor]
        # VI.   We append the previous array in the final array result
        result.append(prime_and_sum)
        # Steps from I to VI could be done in one like this:
#       # result.append([prime, sum(val for val in I if val % prime == 0)])
    
    # VII. The challenge ask us to return a sorted array. 'sort()' help us with that
    #      It will sort keeping in mind the first element of array of two elements
    result.sort()
    return result
`````

This is going to be the ouput:

`````python
I = [15, 21, 24, 30, 45]
print(sum_wth_prime_factors(I)) #[[2, 54], [3, 135], [5, 90], [7, 21]]
I = [12, 15]
print(sum_wth_prime_factors(I)) #[[2, 12], [3, 27], [5, 15]]
`````

