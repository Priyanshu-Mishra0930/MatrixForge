from matrixcalc import m_add, m_sub, m_mul, m_trans, m_s_mul, identity ,determinant

assert m_add([[1]], [[2]]) == [[3]]
assert m_sub([[5]], [[2]]) == [[3]]
assert m_mul([[2]], [[3]]) == [[6]]
assert m_trans([[1,2]]) == [[1],[2]]
assert m_s_mul([[1,2],[3,4]],5) == [[5,10],[15,20]]
assert identity(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert determinant([[-1, 2],[3, -4]]) == -2