import math

def main():
    x = 2
    h = 0.2
    true_value = ddf(x)
    value = myddf(f,x,h)
    print('ddf/ddx :{}'.format(value))
    print('diff    :{}'.format(abs(value-true_value)))

def f(x):
    return x**2

def ddf(x):
    return 2

def myddf(f,x,h):
    return (f(x+2*h)-2*f(x+h)+f(x))/(h**2)

if __name__ == '__main__':
    main()
