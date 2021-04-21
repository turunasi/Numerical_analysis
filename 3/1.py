def main():
    x_p = float(input("Input initial value:"))
    c = 0
    diff = 1
    while diff != 0:
        x = (x_p**2+1)/(2*x_p-1)
        diff = abs(x-x_p)
        x_p = x
        c += 1
        print("{0}:{1}".format(c,diff))
    print("Number of trials:{}".format(c))
    print("Limiting value:{}".format(x))


if __name__ == "__main__":
    main()