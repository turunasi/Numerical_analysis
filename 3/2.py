import math

def main():
    x_p = 0
    x = float(input("Input initial value:"))
    c = 0
    diff = 1
    while diff != 0:
        x_n = x-(x-x_p)*(math.cos(x)-x**2)/(math.cos(x)-x**2-math.cos(x_p)+x_p**2)
        diff = abs(x_n-x)
        x_p = x
        x = x_n
        c += 1
        print("{0}:{1}".format(c,diff))
    print("Number of trials:{}".format(c))
    print("Limiting value:{}".format(x_n))

if __name__ == "__main__":
    main()