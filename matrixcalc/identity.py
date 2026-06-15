def identity(x):
    identity_matrix=[]
    for i in range (0,x):
        identity_col=[]
        for j in range (0,x):
            if(i==j):
                identity_col.append(1)
            else:
                identity_col.append(0)
        identity_matrix.append(identity_col)
    return identity_matrix