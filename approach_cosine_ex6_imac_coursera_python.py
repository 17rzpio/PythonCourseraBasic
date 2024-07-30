n = int(input("\ntype n value of the first number of series: "))
x = float(input("\ntype x for calculate cosine of x: "))

sum1 = 1
signal = 1
for m in range(0,(n*2+2),2):
    if m==2:
        sum1=1
    fatorial=1
    for p in range(1,m+1):
        fatorial*=p
    sum1-=(((x**m)/fatorial)*(signal))
    signal*=(-1)
if sum1<0:
    sum1*=(-1)
print(sum1)
##soma=0
##for i in range(0,n):
##    fatorial=1
##    for p in range(1,i+1):
##       fatorial*=p
##    soma = soma+((-1)**i)*(x**(2*i))/fatorial
##print(soma)
