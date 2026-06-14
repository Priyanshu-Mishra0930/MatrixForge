def m_sub(x,y):
    if len(x)!=len(y):
        return None
    for i in range(len(x)):
        if len(x[i])!=len(y[i]):
            return None
    sub_matrix_AB=[]
    for i in range(len(x)):
        sub_colAB=[]
        for j in range(len(x[i])):
            sub_colAB.append(x[i][j]-y[i][j])
        sub_matrix_AB.append(sub_colAB)
    return sub_matrix_AB