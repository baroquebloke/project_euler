# The sum of the squares of the first ten natural numbers is, 385.
# The square of the sum of the first ten natural numbers is, 3025.
# Hence the difference between the sum of the squares of the first ten 
# natural numbers and the square of the sum of the first ten natural numbers
# is: 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.

# solution: 25164150
# Time: real 0m0.033s
#       user 0m0.018s
#       sys  0m0.012s


def sqr_of_sum():
    total_sum = 0
    for i in range(1, 101):
        total_sum += i
    total_sqr = total_sum**2
    return total_sqr

def sum_of_sqr():
    total_sum_of_sqr = 0
    for i in range(1, 101):
        x = i**2
        total_sum_of_sqr += x
    return total_sum_of_sqr

def difference_of():
    x = sqr_of_sum()
    y = sum_of_sqr()
    z = x - y
    return z

print difference_of() 
