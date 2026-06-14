def m_add(x,y):
    if len(x)!=len(y):
        return None
    for i in range(len(x)):
        if len(x[i])!=len(y[i]):
            return None
    add_matrix=[]
    for i in range(len(x)):
        add_col=[]
        for j in range(len(x[i])):
            add_col.append(x[i][j]+y[i][j])
        add_matrix.append(add_col)
    return add_matrix