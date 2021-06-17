import math

def main():
    x0 = 0
    y0 = 1
    h  = 1
    n  = int(input("Input n :"))
    xn = x0+h*n
    true_value = y0*math.sqrt(xn+1)
    ans = euler_method(func,x0,y0,h,n)
    print('f({0}) :{1}'.format(xn,true_value))
    print('f({0}) caluculated with euler method :{1}'.format(xn,ans))
    print('diff :{}'.format(abs(true_value-ans)))
    ans = heun_method(func,x0,y0,h,n)
    print('f({0}) caluculated with heun method :{1}'.format(xn,ans))
    print('diff :{}'.format(abs(true_value-ans)))
    ans = runge_kutta_method(func,x0,y0,h,n)
    print('f({0}) caluculated with runge kutta method :{1}'.format(xn,ans))
    print('diff :{}'.format(abs(true_value-ans)))

def func(x,y):
    return y/(2*(x+1))

def euler_method(func, x0, y0, h, n):
    x_p = x0
    y_p = y0
    for j in range(n):
        x = x_p + h
        y = y_p + h*func(x_p, y_p)
        x_p = x
        y_p = y
    return y

def heun_method(func, x0, y0, h, n):
    x_p = x0
    y_p = y0
    for j in range(n):
        s1 = func(x_p,y_p)
        s2 = func(x_p+h,y_p+s1*h)
        x = x_p + h
        y = y_p + h*(s1+s2)/2
        x_p = x
        y_p = y
    return y

def runge_kutta_method(func, x0, y0, h, n):
    x_p = x0
    y_p = y0
    for j in range(n):
        k1 = func(x_p,y_p)
        k2 = func(x_p+h/2,y_p+k1*h/2)
        k3 = func(x_p+h/2,y_p+k2*h/2)
        k4 = func(x_p+h,y_p+k3*h/2)
        x = x_p + h
        y = y_p + h*(k1+2*k2+2*k3+k4)/6
        x_p = x
        y_p = y
    return y

if __name__ == '__main__':
    main()
