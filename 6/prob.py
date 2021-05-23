import numpy as np

def main():
    A = init_A()
    B = init_B()
    true_value = np.array([2/57,-9/38,25/38])
    if (not is_diagonal_dominant_matrix(A)):
        print("Matrix A is not a diagonally dominant matrix, so the Jacobi method cannot be used")
        return 1
    print("Since matrix A is a diagonally dominant matrix, the Jacobi method can be used")
    ans = Jacobi(A,B)
    print('Answer by Jacobi method is {}'.format(ans))
    print_diff(true_value,ans)
    ans = Gauss_Seidel(A,B)
    print('Answer by Gauss Seidel method is {}'.format(ans))
    print_diff(true_value,ans)

def init_A():
    return np.array([[3,-1,1],[3,6,2],[3,3,7]])

def init_B():
    return np.array([1,0,4])

def is_diagonal_dominant_matrix(matrix):
    for i, value in enumerate(matrix):
        if(abs((np.sum(value)-value[i])/value[i]) >= 1): return False
    return True

def is_array_diff(a,b,c):
    if (c == 0) : return True
    for i in range(a.size):
        if(abs(a[i-1]-b[i-1]) > 0): return True
    return False

def print_diff(ans,true_value):
    print ('Difference between answer and true value : {}'.format(abs(ans-true_value)))

def Jacobi(A,B):
    ans = np.zeros(B.size)
    ans_p = np.zeros(B.size)
    c = 0
    while(is_array_diff(ans,ans_p,c)):
        ans_p = ans.copy()
        for i, array in enumerate(A):
            ans[i] = (B[i]-array@ans_p+array[i]*ans_p[i])/A[i][i]
        c += 1
    print('Trial Num : {}'.format(c))
    return ans

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
    print('Trial Num : {}'.format(c))
    return ans

if __name__ == '__main__':
    main()
