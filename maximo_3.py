def maximo(a,b,c):
    if int(a)>int(b):
        if int(a)>int(c):
            return a
        if int(b)>int(c):
            return b
        if(c>b):
            return c
    if(b>c):
        return b
    elif(c>b):
        return c
    elif(a==b==c):
        return a

def soma():
    return 1+2

