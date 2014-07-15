##this will find the sum of all the multiples of three and five bellow 1000

def main():
    total = 0
    for x in range (0, 1000):
        if x % 3 == 0:
            total = total + x
        elif x % 5 == 0:
            total = total + x
    print total
main()
