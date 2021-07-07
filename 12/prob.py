import numpy as np
import matplotlib.pyplot as plt

x = 1
hs = [0.25, 0.1, 0.05, 0.025, 0.01]

def main():
    for index,h in enumerate(hs):
        num = int(x/h)+1
        A = init_A(num)
        B = init_B(num,h)
        xs = np.append(np.arange(0,x,h),x)
        ans = Gauss_Seidel(A, B)
        plt.plot(xs,ans,label="Numerical({})".format(num-1))
        plt.scatter(xs,ans,s=2)
    plt.plot(xs,list(map(lambda x: x**2/2-x,xs)),label="Analytical")
    plt.legend()
    plt.savefig('Poisson.png')

def init_A(num):
    A = np.zeros((num,num))
    for i, array in enumerate(A):
        if i == 0:
            array[i] = 1
        elif i == num-1:
            array[i-1] = -1
            array[i] = 1
        else:
            array[i] = -2
            array[i-1] = 1
            array[i+1] = 1
    return A

def init_B(num,h):
    B = np.zeros(num)
    for i,j in enumerate(B):
        if (i == 0) or (i == num-1):
            B[i] = 0
        else:
            B[i] = h**2
    return B

def Gauss_Seidel(A,B):
    ans = np.zeros(B.size)
    ans_p = np.zeros(B.size)
    ans_dot = np.zeros(B.size)
    c = 0
    while(is_array_diff(ans,ans_p,c)):
        ans_p = ans.copy()
        ans_dot = ans.copy()
        ans = np.zeros(B.size)
        for i, array in enumerate(A):
            ans[i] = (B[i]-array@ans_dot+array[i]*ans_dot[i])/A[i][i]
            ans_dot[i] = ans[i]
        c += 1
        if (c%1000 == 0) : print('step {}'.format(c))
    return ans

def is_array_diff(a,b,c):
    if (c == 0) : return True
    for i in range(a.size):
        if(abs(a[i-1]-b[i-1]) > 10**-10): return True
    return False

if __name__ == '__main__':
    main()
