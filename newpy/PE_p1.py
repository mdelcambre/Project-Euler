def p1():
        sum_mult = 0
        for i in range(1,1000):
            if i%5 == 0 or i%3 == 0:
                sum_mult += i
        print sum_mult

if __name__ == "__main__":
    p1()
