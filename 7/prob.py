import numpy as np

def main():
    X = np.array([-2,2])
    k = 0
    while k < 5:
        A = get_A(X)
        b = get_b(X)
        dk = Jacobi(A,b)
        X = X+dk
        print('X^{0}:{1}'.format(k+1,X))
        k += 1

def get_A(X):
    x_1 = X[0]
    x_2 = X[1]
    return np.array([[120*x_1**2-40*x_2+2,-40*x_1],[-40*x_1,20]])

def get_b(X):
    x_1 = X[0]
    x_2 = X[1]
    return -np.array([40*x_1**3-40*x_1*x_2+2*x_1-2,20*x_2-20*x_1**2])

def is_array_diff(a,b,c):
    if (c == 0) : return True
    for i in range(b.size):
        if(abs(a[i-1]-b[i-1]) > 10**-14): return True
    return False

def Jacobi(A,b):
    ans = np.zeros(b.size)
    ans_p = np.zeros(b.size)
    c = 0
    while(is_array_diff(ans,ans_p,c)):
        ans_p = ans.copy()
        for i, array in enumerate(A):
            ans[i] = (b[i]-array@ans_p+array[i]*ans_p[i])/A[i][i]
        c += 1
    print('Trial Num : {}'.format(c))
    return ans

if __name__ == '__main__':
    main()
