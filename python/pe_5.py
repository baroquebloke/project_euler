# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?
#
# Answer: 232792560
# Run time: 1m29.739s
#
# Not sure yet how to improve run time yet.  work in progress.

def main():
    d = 2
    num = 1
    while d < 21:
        if num % d == 0:
            d += 1
        else:
            num += 1
            d = 2
    return num

print main()
