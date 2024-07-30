def seg_max3(v):
    n=len(v)
    smax=e=d=0
    for i in range(n):
        for j in range(i,n):
            s=0
            for k in range(i,j+1):
                s+=v[k]
                if s > smax:
                    e,d,smax=i,j+1,s
    return e,d,smax
