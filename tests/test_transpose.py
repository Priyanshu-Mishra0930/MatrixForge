from matrixcalc.transpose import m_tran

assert m_tran([[1]]) == [[1]]

assert m_tran(
    [[1,2,3],
     [4,5,6]]
) == [
    [1,4],
    [2,5],
    [3,6]
]