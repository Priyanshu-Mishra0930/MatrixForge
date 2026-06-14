from matrixcalc.subtraction import m_sub

assert m_sub([[1]], [[2]]) == [[-1]]

assert m_sub(
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
) == [
    [-4, -4],
    [-4, -4]
]

assert m_sub([[1, 2]], [[1]]) is None