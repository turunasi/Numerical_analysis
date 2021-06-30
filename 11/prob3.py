import math

def main():
    data = [[1.0,1.0], [2.0,2.718], [3.0,7.389], [4.0,20.08], [5.0,54.59]]
    dydxs = []
    h = 1
    print('   x   |   y   |   dy/dx   ')
    print('---------------------------')
    for i in range(len(data)):
        if i == 0:
            value = one_sided_diff(data[i][1],data[i+1][1],data[i+2][1], h)
        elif i == len(data)-1:
            value = -one_sided_diff(data[i][1],data[i-1][1],data[i-2][1], h)
        else:
            value = central_diff(data[i-1][1], data[i+1][1], h)
        print('{0:^7}|{1:^7}|{2:^11}'.format(data[i][0],data[i][1],value))
        print('---------------------------')

def central_diff(yp,yn,h):
    return (yn-yp)/(2*h)

def one_sided_diff(y1,y2,y3,h):
    return -(y3-4*y2+3*y1)/(2*h)

if __name__ == '__main__':
    main()
