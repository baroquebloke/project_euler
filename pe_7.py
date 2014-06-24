# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.  What is the 10 001st prime number?
#
# Answer: 104743
# Time: 3m34.229s
# ...very long, but it works!  Will try a different method...

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    count = 0
    num = 2
    while True:
        if is_prime(num):
            print num
            num += 1
            count += 1
            if count == 10001:
                break
        else:
            num += 1


main()
