sum1=0
signal=1
for n in range(1,10001):
    sum1+=(1/n)*(signal)
    signal*=(-1)
print(sum1)


sum1=0
signal=-1
for n in range(10000,0,-1):
    sum1+=(1/n)*(signal)
    signal*=(-1)
print(sum1)

pos = 0
for n in range(1,5001,2):
    pos+=(1/n)
neg = 0
for n in range(2,5001,2):
    neg+=(1/n)
print(pos-neg)

pos=0
for n in range(5000,0,-2):
    neg+=(1/n)
neg=0
for n in range(4999,0,-2):
    pos+=(1/n)
print(pos-neg)
