# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def palind_num():
    is_pal = None
    for x in range(100, 1000):
        for y in range(100, 1000):
            num = x * y
            if str(num) == str(num)[::-1]:
                if is_pal is None or num > is_pal:
                    is_pal = num
    return is_pal

print palind_num()
