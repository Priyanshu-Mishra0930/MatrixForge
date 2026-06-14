def m_mul(x,y):
    if len(x[0]) != len(y):
        return None

    mul_matrix_AxB = []

    for i in range(len(x)):
        mul_col_AxB = []
        for j in range(len(y[0])):
            s = 0
            for k in range(len(y)):
                s += x[i][k] * y[k][j]
            mul_col_AxB.append(s)
        mul_matrix_AxB.append(mul_col_AxB)
    return mul_matrix_AxB