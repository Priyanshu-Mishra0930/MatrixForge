# from matrixcalc.addition import m_add

# assert m_add([[1]], [[2]]) == [[3]]

# assert m_add(
#     [[1, 2],
#      [3, 4]],

#     [[5, 6],
#      [7, 8]]
# ) == [
#     [6, 8],
#     [10, 12]
# ]

# assert m_add([[1, 2]], [[1]]) is None
from matrixcalc import m_add

print(m_add([[1]], [[2]]))