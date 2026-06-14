from matrixcalc import m_add, m_sub, m_mul, m_trans

assert m_add([[1]], [[2]]) == [[3]]
assert m_sub([[5]], [[2]]) == [[3]]
assert m_mul([[2]], [[3]]) == [[6]]
assert m_trans([[1,2]]) == [[1],[2]]