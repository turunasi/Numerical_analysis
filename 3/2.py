import math
import numpy as np
from matplotlib import pyplot as plt

def main():
    x_p = 0
    x = float(input("Input initial value:"))
    x_list = []
    y_list = []
    c = 0
    diff = 1
    fig = plt.figure()
    while diff != 0:
        x_n = x-(x-x_p)*(math.cos(x)-x**2)/(math.cos(x)-x**2-math.cos(x_p)+x_p**2)
        diff = abs(x_n-x)
        x_p = x
        x = x_n
        c += 1
        x_list += [c]
        y_list += [diff]
        print("{0}:{1}".format(c,diff))
    print("Number of trials:{}".format(c))
    print("Limiting value:{}".format(x_n))
    x_list = np.array(x_list)
    y_list = np.array(y_list)
    plt.plot(x_list, y_list, label='diff')
    plt.title('Diff Graph')
    plt.xlabel('Count')
    plt.ylabel('Diff')
    plt.legend()
    plt.show()
    fig.savefig("2.png")

if __name__ == "__main__":
    main()
