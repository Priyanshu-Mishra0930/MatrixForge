from matrixcalc.multiplication import m_mul

assert m_mul([[1]], [[2]]) == [[2]]

assert m_mul(
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
) == [
    [19, 22],
    [43, 50]
]

assert m_mul([[1, 2]], [[1]]) is None