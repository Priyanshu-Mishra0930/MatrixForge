from matrixcalc.determinant import determinant

assert determinant([[5]]) == 5

assert determinant(
    [[1, 2],
     [3, 4]]
) == -2

assert determinant(
    [[2, 0],
     [0, 3]]
) == 6

assert determinant(
    [[1, 2, 3],
     [0, 4, 5],
     [1, 0, 6]]
) == 22

assert determinant(
    [[6, 1, 1],
     [4, -2, 5],
     [2, 8, 7]]
) == -306

assert determinant(
    [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
) == 1

assert determinant(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
) == 0

assert determinant(
    [[2, 5],
     [1, 3]]
) == 1

assert determinant(
    [[-1, 2],
     [3, -4]]
) == -2
assert determinant(
    [[1, 0, 2, -1],
     [3, 0, 0, 5],
     [2, 1, 4, -3],
     [1, 0, 5, 0]]
) == 30
assert determinant([]) == 0