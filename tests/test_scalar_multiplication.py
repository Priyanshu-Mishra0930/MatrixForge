from matrixcalc.scalar_multiplication import m_s_mul

assert m_s_mul([[1]], 5) == [[5]]

assert m_s_mul(
    [[1, 2],
     [3, 4]],
    2
) == [
    [2, 4],
    [6, 8]
]

assert m_s_mul(
    [[1, 2, 3],
     [4, 5, 6]],
    3
) == [
    [3, 6, 9],
    [12, 15, 18]
]

assert m_s_mul(
    [[1, -2],
     [-3, 4]],
    -2
) == [
    [-2, 4],
    [6, -8]
]

assert m_s_mul([], 5) == []