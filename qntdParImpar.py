a = int(input("digite quantos numeros"))
b=int(0)
e=0
f=0
while(b<a):
    c = int(input("digite numero"))
    d = c % 2
    if (d==0):
        e+=1
    else:
        f+=1
    b+=1
print("par",e)
print("impar",f)
