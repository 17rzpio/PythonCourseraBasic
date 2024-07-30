def is_prime(argument):
    count=0
    for n in range(1,argument+1):
        if argument%n==0:
            count+=1
        if count>2:
            return False
    return True




