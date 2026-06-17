def determinant(x):
    n = len(x)
    if n == 1:
        return x[0][0]
    if n == 2:
        return (
            x[0][0] * x[1][1]
            - x[0][1] * x[1][0]
        )
    det = 0
    for i in range(n):
        minor = []
        for j in range(1, n):
            new_row = (x[j][:i] + x[j][i+1:])
            minor.append(new_row)
        det += ((-1) ** i) * x[0][i] * determinant(minor)
    return det
