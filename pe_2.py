# this will find the sum of all even numbers in the fibonacci sequesnce
#whose values do not exceed 4,000,000

def main():
    old = 1
    new = 1
    old_new = 0
    total = 0
    while new <= 4000000:
        old_new = new
        new = old + new
        if new % 2 == 0:
            total = total + new
        old = old_new
    print total
            

main()
