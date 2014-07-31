# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# result: 906609
# time: 0.433s
#
# *edit: optimized*

def palind_num():
    is_pal = 0
    for x in range(999, 99, -1):
        for y in range(x, 99, -1):
            num = x * y
            if str(num) == str(num)[::-1]:
                if is_pal < num:
                    is_pal = num
    return is_pal

print palind_num()
