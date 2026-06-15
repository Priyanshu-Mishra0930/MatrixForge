def m_s_mul(x,y):
    s_mul_matrix=[]
    for i in range(0,len(x)):
        s_mul_col=[]
        for j in range(0,len(x[0])):
            s_mul_col.append(x[i][j]*y)
        s_mul_matrix.append(s_mul_col)
    return s_mul_matrix
