import numpy as np

def find_max_index(arr):
    max_value = abs(arr[0])
    max_index = 0

    for i in range(1, len(arr)):
        if abs(arr[i]) > max_value:
            max_value = abs(arr[i])
            max_index = i

    return max_index


def gauss_elimination_with_partial_pivoting():
    matrix34= np.array([
        [0,2,-1,5,29],
        [-3,-6,+2,-1,-71.5],
        [1,1,5,3,-27.5],
        [-4,2,-2,-1,55]
    ],dtype=float)

    np.set_printoptions(suppress=True)
    print("Original Matrix:\n", matrix34)

    # forward elimination ---------------------

    k = 0  # counter that helps to start from a lower row when switching columns

    # Iterate the matrix in diagonal
    # i = column, j = row
    for i in range(matrix34.shape[1] - 1):
        for j in range(matrix34.shape[0] - 1):
            j = j + k

            if j >= matrix34.shape[0] - 1:
                continue

            if matrix34[i, j] == 0:
                max_index = find_max_index(matrix34[:, i])

                row_to_swap = matrix34[i, :].copy()
                row_max_value = matrix34[max_index, :].copy()

                matrix34[i, :] = row_max_value
                matrix34[max_index, :] = row_to_swap
                print("Pivot:\n", matrix34)

            b = matrix34[j + 1, i].copy()
            a = matrix34[i, i].copy()
            factor = b / a
            row = matrix34[i,].copy()
            array = factor * row
            temp = matrix34[j + 1,].copy() - array

            matrix34[j + 1, :] = temp
            print("step {},{} :\n{}".format(i, j, matrix34))

        # to start the next iteration 1 row down
        k = k + 1

    # back substitution
    x = backward_substitution(matrix34)

    print("Roots:", x)


def backward_substitution(matrix):
    n = matrix.shape[0]
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += matrix[i, j] * x[j]

        x[i] = (matrix[i, -1] - sum_ax) / matrix[i, i]

    return x

if __name__ == "__main__":
    try:
        gauss_elimination_with_partial_pivoting()
    except Exception as e:
        print("An unexpected error occurred:", e)

# print(arr1.dtype)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)
#
# print("\narray 2")
# arr2 = arr1.flatten()
# print(arr2

# a = matrix34.shape
# print(type(a))
# print(a[0])
# print(a[1])
