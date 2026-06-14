def m_trans(x):
    m=len(x)
    n=len(x[0])
    at=[]
    for i in range (0,n):
        tran_col=[]
        for j in range(0,m):
            tran_col.append(x[j][i])
        at.append(tran_col)
    return at