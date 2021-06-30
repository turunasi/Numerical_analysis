import math

def main():
    x = 2
    h = 0.2
    true_value = df(x)
    methods = ['forward_diff', 'backward_diff', 'central_diff']
    for method in methods:
        label = method.replace('_', ' ')
        value = globals()[method](f,x,h)
        print('{}'.format(label))
        print('    df/dx :{}'.format(value))
        print('    diff  :{}'.format(abs(value-true_value)))

def f(x):
    return x**2

def df(x):
    return 2*x

def forward_diff(f,x,h):
    return (f(x+h)-f(x))/h

def backward_diff(f,x,h):
    return (f(x)-f(x-h))/h

def central_diff(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

if __name__ == '__main__':
    main()
