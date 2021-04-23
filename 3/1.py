import numpy as np
from matplotlib import pyplot as plt

def main():
    a = float(input("Input a:"))
    b = float(input("Input b:"))
    x = []
    y = []
    count = 0
    fig = plt.figure()
    if f(a)*f(b) >= 0:
        print("a or b is invalid value.\n")
        return 1
    while a != b:
        c = (a+b)/2
        s = f(a)*f(c)
        if s < 0:
            b = c
        else:
            a = c 
        count += 1
        x += [count]
        y += [abs(a-b)]
        print("{0}:{1}".format(count,a-b))
    print("Number of trials:{}".format(c))
    print("Limiting value:{}".format(a))
    x = np.array(x)
    y = np.array(y)
    plt.plot(x, y, label='diff')
    plt.title('Diff Graph')
    plt.xlabel('Count')
    plt.ylabel('Diff')
    plt.legend()
    plt.show()
    fig.savefig("1.png")

def f(x):
    return x**2-x-1

if __name__ == "__main__":
    main()
