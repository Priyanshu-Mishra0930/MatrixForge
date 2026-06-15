from matrixcalc.identity import identity

assert identity(1) == [
    [1]
]

assert identity(2) == [
    [1, 0],
    [0, 1]
]

assert identity(3) == [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]