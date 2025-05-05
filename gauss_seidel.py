import numpy as np

def gauss_seidel():
    matrix_a = np.array([
        [3,-0.1,-0.2],
        [0.1,7,-0.3],
        [0.3,-0.2,10],
    ],dtype=float)

    np.set_printoptions(suppress=True)

    matrix_b= np.array([7.85,-19.3,71.4],dtype=float)

    re = 0.0001

    x1prev = (matrix_b[0] - (matrix_a[0, 1] * 0) - (matrix_a[0, 2] * 0)) / matrix_a[0, 0]
    x2prev = (matrix_b[1] - (matrix_a[1, 0] * x1prev) - (matrix_a[1, 2]) * 0) / matrix_a[1, 1]
    x3prev = (matrix_b[2] - (matrix_a[2, 0] * x1prev) - (matrix_a[2, 1] * x2prev)) / matrix_a[2, 2]

    re1 = 100
    re2 = 100
    re3 = 100
    flag = True;
    i=0
    print("n:0, x1: {}, x2: {}, x3: {}".format(x1prev,x2prev,x3prev))

    while flag:
        if re1 < re and re2 < re and re3 < re:
            flag = False

        x1 = (matrix_b[0] - (matrix_a[0, 1] * x2prev) - (matrix_a[0, 2] * x3prev)) / matrix_a[0, 0]
        re1 = abs((x1 - x1prev) / x1)
        x1prev = x1

        x2 = (matrix_b[1] - (matrix_a[1, 0] * x1prev) - (matrix_a[1, 2]) * x3prev) / matrix_a[1, 1]
        re2 = abs((x2 - x2prev) / x2)
        x2prev = x2

        x3 = (matrix_b[2] - (matrix_a[2, 0] * x1prev) - (matrix_a[2, 1] * x2prev)) / matrix_a[2, 2]
        re3 = abs((x3 - x3prev) / x3)
        x3prev = x3

        i = i + 1

        print("n:{}, x1: {}, x2: {}, x3: {}, re1:{}, re2:{}, re3:{} \n".format(i,x1,x2,x3,re1,re2,re3))

    print("X1: {}\nX2: {}\nX3: {}\n".format(x1,x2,x3))

if __name__ == '__main__':
    gauss_seidel()