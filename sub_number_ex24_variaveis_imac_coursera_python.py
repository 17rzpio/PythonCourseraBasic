p = int(input("\ntype first positive number for verify is sub number: "))

while p < 1:
    p = int(input("\ntype first positive number for verify is sub number: "))

q = int(input("\ntype second positive number for verify if first number is sub number of him and bigger than first: "))

while q < 1 and q >= p:
    q = int(input("\ntype second positive number for verify if first number is sub number of him and bigger than first: "))

flag_sub_number = False

place = 0
place_flag= False

if (int(q/1000000000))>0:
    place = 10
    place_flag = True
    
elif (int(q/100000000))>0:
    place = 9
    place_flag = True

elif (int(q/10000000))>0:
    place = 8
    place_flag = True

elif (int(q/1000000))>0:
    place = 7
    place_flag = True

elif (int(q/100000))>0:
    place = 6
    place_flag = True

elif (int(q/10000))>0:
    place = 5
    place_flag = True

elif (int(q/1000))>0:
    place = 4
    place_flag = True

elif (int(q/100))>0:
    place = 3
    place_flag = True

elif (int(q/10))>0:
    place = 2
    place_flag = True

if place==2:
    r = int(q/10)
    s = q - (r*10)
    if p ==r or s ==p:
        flag_sub_number = True

if place==3:
    t = int(q/100)
    r = int((q - (t*100))/10)
    s = q - (r*10) - (t*100)
    if p < 10:
        if p == r or p ==s or p== t:
            flag_sub_number = True        
    else:
        u = int(p/10)
        v = p - (u*10)
        if (v==s and u==r) or (v==r and u==t):
            flag_sub_number = True

if place==4:
    w = int(q/1000)
    t = int((q-(w*1000))/100)
    r = int((q-(w*1000)-(t*100))/10)
    s = q - (r*10) - (t*100) - (w*1000)
    if p < 10:
        if (p == r or p ==s or p== t or p==w):
            flag_sub_number = True   
    elif p < 100:
        u = int(p/10)
        v = p - (u*10)
        if (u==r and v==s) or (v==r and u==t) or (u==t and v==w):
            flag_sub_number = True
    else:
        x = int(p/100)
        u = int((p-(x*100))/10)
        v = p - (x*100) - (u*10)
        if (u==r and v==s and x==t) or (v==r and u==t and x==w):
            flag_sub_number = True

if place==5:
    y = int(q/10000)
    w = int((q-(y*10000))/1000)
    t = int((q-(y*10000)-(w*1000))/100)
    r = int((q-(y*10000)-(w*1000)-(t*100))/10)
    s = q - (y*10000)-(w*1000)-(t*100)-(r*10)
    if p <10:
        if(p == r or p ==s or p== t or p==w or p==y):
            flag_sub_number = True  
    elif p < 100:
        u = int(p/10)
        v = p-(u*10)
        if (u==r and v==s) or (v==r and u==t) or (v==t and u==w) or (v==w and u==y):
            flag_sub_number = True
    elif p < 1000:
        x = int(p/100)
        u = int((p-(x*100))/10)
        v = p - (x*100) - (u*10)
        if (u==r and v==s and x==t) or (v==r and u==t and x==w) or (v==t and u==w and x==y):
            flag_sub_number = True
    else:
        z = int(p/1000)
        x= int((p-(z*1000))/100)
        u = int((p-(z*1000)-(x*100))/10)
        v = p - (z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w) or (v==r and u==t and x==w and z==y):
            flag_sub_number = True
if place==6:
    a = int(q/100000)
    y= int((q-(a*100000))/10000)
    w = int((q-(a*100000)-(y*10000))/1000)
    t = int((q-(a*100000)-(y*10000)-(w*1000))/100)
    r = int((q-(a*100000)-(y*10000)-(w*1000)-(t*100))/10)
    s = q - (a*100000)-(y*10000)-(w*1000)-(t*100)-(r*10)
    if p <10:
        if(p == r or p ==s or p== t or p==w or p==y or p==a):
            flag_sub_number = True
    elif p < 100:
        u = int(p/10)
        v = p-(u*10)
        if (u==r and v==s) or (v==r and u==t) or (v==t and u==w) or (v==w and u==y)or(v==y and u==a):
            flag_sub_number = True
    elif p < 1000:
        x = int(p/100)
        u = int((p-(x*100))/10)
        v = p - (x*100) - (u*10)
        if (u==r and v==s and x==t) or (v==r and u==t and x==w) or (v==t and u==w and x==y) or (v==w and u==y and x==a):
            flag_sub_number = True
    elif p < 10000:
        z = int(p/1000)
        x= int((p-(z*1000))/100)
        u = int((p-(z*1000)-(x*100))/10)
        v = p - (z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w) or (v==r and u==t and x==w and z==y) or (v==t and u==w and x==y and z==a):
            flag_sub_number = True
    else:
        b = int(p/10000)
        z= int((p-(b*10000))/1000)
        x = int((p-(b*10000)-(z*1000))/100)
        u = int((p-(b*10000)-(z*1000)-(x*100))/10)
        v = p - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w and b==y)or(v==r and u==t and x== w and z==y and b==a):
            flag_sub_number = True
if place==7:            
    c = int(q/1000000)
    a = int((q- (c*1000000))/100000)
    y = int((q- (c*1000000)-(a*100000))/10000)
    w = int((q-(c*1000000)-(a*100000)-(y*10000))/1000)
    t = int((q-(c*1000000)-(a*100000)-(y*10000)-(w*1000))/100)
    r = int((q-(c*1000000)-(a*100000)-(y*10000)-(w*1000)-(t*100))/10)
    s = q - (c*1000000) - (a*100000) - (y*10000) - (w*1000) - (t*100) -(r*10)
    if p <10:
        if(p == r or p ==s or p== t or p==w or p==y or p==a or p==c):
            flag_sub_number = True
    elif p < 100:
        u = int(p/10)
        v = p-(u*10)
        if (u==r and v==s) or (v==r and u==t) or (v==t and u==w) or (v==w and u==y)or(v==y and u==a)or(v==a and u==c):
            flag_sub_number = True
    elif p < 1000:
        x = int(p/100)
        u = int((p-(x*100))/10)
        v = p - (x*100) - (u*10)
        if (u==r and v==s and x==t) or (v==r and u==t and x==w) or (v==t and u==w and x==y) or (v==w and u==y and x==a)or(v==y and u==a and x==c):
            flag_sub_number = True
    elif p < 10000:
        z = int(p/1000)
        x= int((p-(z*1000))/100)
        u = int((p-(z*1000)-(x*100))/10)
        v = p - (z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w) or (v==r and u==t and x==w and z==y) or (v==t and u==w and x==y and z==a)or(v==w and u==y and x==a and z==c):
            flag_sub_number = True
    elif p < 100000:
        b = int(p/10000)
        z= int((p-(b*10000))/1000)
        x = int((p-(b*10000)-(z*1000))/100)
        u = int((p-(b*10000)-(z*1000)-(x*100))/10)
        v = p - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w and b==y)or(v==r and u==t and x==w and z==y and b==a)or(v==t and u==y and x==y and z==a and b==c):
            flag_sub_number = True
    else:
        d = int(p/100000)
        b = int((p-(d*100000))/10000)
        z = int((p-(d*100000)-(b*10000))/1000)
        x = int((p-(d*100000)-(b*10000)-(z*1000))/100)
        u = int((p-(d*100000)-(b*10000)-(z*1000)-(x*100))/10)
        v = p - (d*100000) - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w and b==y and d==a)or(v==r and u==t and x==w and z==y and b==a and d==c):
            flag_sub_number = True
if place==8:
    
    e = int(q/10000000)
    c = int((q - (e*10000000))/1000000)
    a = int((q-(e*10000000)-(c*1000000))/100000)
    y = int((q-(e*10000000)-(c*1000000)-(a*100000))/10000)
    w = int((q-(e*10000000)-(c*1000000)-(a*100000)-(y*10000))/1000)
    t = int((q-(e*10000000)-(c*1000000)-(a*100000)-(y*10000)-(w*1000))/100)
    r = int((q-(e*10000000)-(c*1000000)-(a*100000)-(y*10000)-(w*1000)-(t*100))/10)
    s = q - (e * 10000000)-(c*1000000)-(a*100000)-(y*10000)-(w*1000)-(t*100)-(r*10)
    if p <10:
        if(p == r or p ==s or p== t or p==w or p==y or p==a or p==c or p==e):
            flag_sub_number = True
    elif p < 100:
        u = int(p/10)
        v = p-(u*10)
        if (u==r and v==s) or (v==r and u==t) or (v==t and u==w) or (v==w and u==y)or(v==y and u==a)or(v==a and u==c)or(v==c and u==e):
            flag_sub_number = True
    elif p < 1000:
        x = int(p/100)
        u = int((p-(x*100))/10)
        v = p - (x*100) - (u*10)
        if (u==r and v==s and x==t) or (v==r and u==t and x==w) or (v==t and u==w and x==y) or (v==w and u==y and x==a)or(v==y and u==a and x==c)or(v==a and u==c and x==e):
            flag_sub_number = True
    elif p < 10000:
        z = int(p/1000)
        x= int((p-(z*1000))/100)
        u = int((p-(z*1000)-(x*100))/10)
        v = p - (z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w) or (v==r and u==t and x==w and z==y) or (v==t and u==w and x==y and z==a)or(v==w and u==y and x==a and z==c)or(v==y and u==a and x==c and z==e):
            flag_sub_number = True
    elif p < 100000:
        b = int(p/10000)
        z= int((p-(b*10000))/1000)
        x = int((p-(b*10000)-(z*1000))/100)
        u = int((p-(b*10000)-(z*1000)-(x*100))/10)
        v = p - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w and b==y)or(v==r and u==t and z==y and b==x)or(v==t and u==y and z==x and b==c)or(v==y and u==x and z==c and b==e):
            flag_sub_number = True
    elif p < 1000000:
        d = int(p/100000)
        b = int((p-(d*100000))/10000)
        z = int((p-(d*100000)-(b*10000))/1000)
        x = int((p-(d*100000)-(b*10000)-(z*1000))/100)
        u = int((p-(d*100000)-(b*10000)-(z*1000)-(x*100))/10)
        v = p - (d*100000) - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(v==s and u==r and x==t and z==w and b==y and d==a)or(v==r and u==t and x==w and z==y and b==a and d==c)or(v==t and u==w and x==y and z==a and b==c and d==e):
            flag_sub_number = True
    else:
        f = int(p/1000000)
        d = int((p-(f*1000000))/100000)
        b = int((p-(f*1000000)-(d*100000))/10000)
        z= int((p-(f*1000000)-(d*100000)-(b*10000))/1000)
        x = int((p-(f*1000000)-(d*100000)-(b*10000)- (z*1000))/100)
        u = int((p-(f*1000000)-(d*100000)-(b*10000)- (z*1000)-(x*100))/10)
        v = p - (f*1000000)-(d*100000) - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(v==s and u==r and x==t and z==w and b==y and d==a and f==c)or(v==r and u==t and x==w and z==y and b==a and d==c and f==e):
            flag_sub_number = True
if place == 9:
    g = int(q/100000000)
    e = int((q - (g*100000000))/10000000)
    c = int((q - (g*100000000) - (e*10000000))/1000000)
    a = int((q - (g*100000000) - (e*10000000)-(c*1000000))/100000)
    y = int((q - (g*100000000) - (e*10000000)-(c*1000000)-(a*100000))/10000)
    w = int((q - (g*100000000) - (e*10000000)-(c*1000000)-(a*100000)-(y*10000))/1000)
    t = int((q - (g*100000000) - (e*10000000)-(c*1000000)-(a*100000)-(y*10000)-(w*1000))/100)
    r = int((q - (g*100000000) - (e*10000000)-(c*1000000)-(a*100000)-(y*10000)-(w*1000)-(t*100))/10)
    s = q - (g*100000000) - (e*10000000)-(c*1000000)-(a*100000)-(y*10000)-(w*1000)-(t*100)-(r*10)
    if p <10:
        if(p == r or p ==s or p== t or p==w or p==y or p==a or p==c or p==e or p==g):
            flag_sub_number = True
    elif p < 100:
        u = int(p/10)
        v = p-(u*10)
        if (u==r and v==s) or (v==r and u==t) or (v==t and u==w) or (v==w and u==y)or(v==y and u==a)or(v==a and u==c)or(v==c and u==e)or(v==e and u==g):
            flag_sub_number = True
    elif p < 1000:
        x = int(p/100)
        u = int((p-(x*100))/10)
        v = p - (x*100) - (u*10)
        if (u==r and v==s and x==t) or (v==r and u==t and x==w) or (v==t and u==w and x==y) or (v==w and u==y and x==a)or(v==y and u==a and x==c)or(v==a and u==c and x==e)or(v==c and u==e and x==g):
            flag_sub_number = True
    elif p < 10000:
        z = int(p/1000)
        x= int((p-(z*1000))/100)
        u = int((p-(z*1000)-(x*100))/10)
        v = p - (z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w) or (v==r and u==t and x==w and z==y) or (v==t and u==w and x==y and z==a)or(v==w and u==y and x==a and z==c)or(v==y and u==a and x==c and z==e)or(v==a and u==c and x==e and z==g):
            flag_sub_number = True
    elif p < 100000:
        b = int(p/10000)
        z= int((p-(b*10000))/1000)
        x = int((p-(b*10000)-(z*1000))/100)
        u = int((p-(b*10000)-(z*1000)-(x*100))/10)
        v = p - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w and b==y)or(v==r and u==t and z==y and b==x)or(v==t and u==y and z==x and b==c)or(v==y and u==x and z==c and b==e)or(v==x and u==c and z==e and b==g):
            flag_sub_number = True
    elif p < 1000000:
        d = int(p/100000)
        b = int((p-(d*100000))/10000)
        z = int((p-(d*100000)-(b*10000))/1000)
        x = int((p-(d*100000)-(b*10000)-(z*1000))/100)
        u = int((p-(d*100000)-(b*10000)-(z*1000)-(x*100))/10)
        v = p - (d*100000) - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(v==s and u==r and x==t and z==w and b==y and d==a)or(v==r and u==t and x==w and z==y and b==a and d==c)or(v==t and u==w and x==y and z==a and b==c and d==e)or(v==w and u==y and x==a and z==c and b==e and d==g):
            flag_sub_number = True
    elif p<10000000:
        f = int(p/1000000)
        d = int((p-(f*100000))/100000)
        b = int((p-(f*100000)-(d*100000))/10000)
        z= int((p-(f*100000)-(d*100000)-(b*10000))/1000)
        x = int((p-(f*100000)-(d*100000)-(b*10000)- (z*1000))/100)
        u = int((p-(f*100000)-(d*100000)-(b*10000)- (z*1000)-(x*100))/10)
        v = p - (f*1000000)-(d*100000) - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(v==s and u==r and x==t and z==w and b==y and d==a and f==c)or(v==r and u==t and x==w and z==y and b==a and d==c and f==e)or(v==t and u==w and x==y and z==a and b==c and d==e and f==g):
            flag_sub_number = True
    else:
        h = int(p/10000000)
        f = int((p-(h*10000000))/1000000)
        d = int((p-(h*10000000)-(f*1000000))/100000)
        b = int((p-(h*10000000)-(f*1000000)-(d*100000))/10000)
        z = int((p-(h*10000000)-(f*1000000)-(d*100000)-(b*10000))/1000)
        x = int((p-(h*10000000)-(f*1000000)-(d*100000)-(b*10000)-(z*1000))/100)
        u = int((p-(h*10000000)-(f*1000000)-(d*100000)-(b*10000)-(z*1000)-(x*100))/10)
        v = p - (h * 10000000)-(f*1000000)-(d*100000)-(b*10000)-(z*1000)-(x*100)-(u*10)
        if(v==s and u==r and x==t and z==w and b==y and d==a and f==c and h==e)or(v==r and u==t and x==w and z==y and b==a and d==c and f==e and h==g):
            flag_sub_number = True
if place == 10:
    i = int(q/1000000000)
    g = int((q-(i*1000000000))/100000000)
    e = int((q-(i*1000000000)-(g*100000000))/10000000)
    c=int((q-(i*1000000000)-(g*100000000)-(e*10000000))/1000000)
    a=int((q-(i*1000000000)-(g*100000000)-(e*10000000)-(c*1000000))/100000)
    y=int((q-(i*1000000000)-(g*100000000)-(e*10000000)-(c*1000000)-(a*100000))/10000)
    w=int((q-(i*1000000000)-(g*100000000)-(e*10000000)-(c*1000000)-(a*100000)-(y*10000))/1000)
    t=int((q-(i*1000000000)-(g*100000000)-(e*10000000)-(c*1000000)-(a*100000)-(y*10000)-(w*1000))/100)
    r=int((q-(i*1000000000)-(g*100000000)-(e*10000000)-(c*1000000)-(a*100000)-(y*10000)-(w*1000)-(t*100))/10)
    s=q-(i*1000000000)- (g*100000000) - (e*10000000)-(c*1000000)-(a*100000)-(y*10000)-(w*1000)-(t*100)-(r*10)
    if p <10:
        if(p == r or p ==s or p== t or p==w or p==y or p==a or p==c or p==e or p==g or p==i):
            flag_sub_number = True
    elif p < 100:
        u = int(p/10)
        v = p-(u*10)
        if (u==r and v==s) or (v==r and u==t) or (v==t and u==w) or (v==w and u==y)or(v==y and u==a)or(v==a and u==c)or(v==c and u==e)or(v==e and u==g)or(v==g and u==i):
            flag_sub_number = True
    elif p < 1000:
        x = int(p/100)
        u = int((p-(x*100))/10)
        v = p - (x*100) - (u*10)
        if (u==r and v==s and x==t) or (v==r and u==t and x==w) or (v==t and u==w and x==y) or (v==w and u==y and x==a)or(v==y and u==a and x==c)or(v==a and u==c and x==e)or(v==c and u==e and x==g)or(v==e and u==g and x==i):
            flag_sub_number = True
    elif p < 10000:
        z = int(p/1000)
        x= int((p-(z*1000))/100)
        u = int((p-(z*1000)-(x*100))/10)
        v = p - (z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w) or (v==r and u==t and x==w and z==y) or (v==t and u==w and x==y and z==a)or(v==w and u==y and x==a and z==c)or(v==y and u==a and x==c and z==e)or(v==a and u==c and x==e and z==g)or(v==c and u==e and x==g and z==i):
            flag_sub_number = True
    elif p < 100000:
        b = int(p/10000)
        z= int((p-(b*10000))/1000)
        x = int((p-(b*10000)-(z*1000))/100)
        u = int((p-(b*10000)-(z*1000)-(x*100))/10)
        v = p - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(u==r and v==s and x==t and z==w and b==y)or(v==r and u==t and x==w and z==y and b==a)or(v==t and u==w and x==y and z==a and b==c)or(v==w and u==y and x==a and z==c and b==e)or(v==y and u==a and x==c and z==e and b==g)or(v==a and u==c and x==e and z==g and b==i):
            flag_sub_number = True
    elif p < 1000000:
        d = int(p/100000)
        b = int((p-(d*100000))/10000)
        z = int((p-(d*100000)-(b*10000))/1000)
        x = int((p-(d*100000)-(b*10000)-(z*1000))/100)
        u = int((p-(d*100000)-(b*10000)-(z*1000)-(x*100))/10)
        v = p - (d*100000) - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(v==s and u==r and x==t and z==w and b==y and d==a)or(v==r and u==t and x==w and z==y and b==a and d==c)or(v==t and u==w and x==y and z==a and b==c and d==e)or(v==w and u==y and x==a and z==c and b==e and d==g)or(v==y and u==a and x==c and z==e and b==g and d==i):
            flag_sub_number = True
    elif p<10000000:
        f = int(p/1000000)
        d = int((p-(f*100000))/100000)
        b = int((p-(f*100000)-(d*100000))/10000)
        z= int((p-(f*100000)-(d*100000)-(b*10000))/1000)
        x = int((p-(f*100000)-(d*100000)-(b*10000)- (z*1000))/100)
        u = int((p-(f*100000)-(d*100000)-(b*10000)- (z*1000)-(x*100))/10)
        v = p - (f*1000000)-(d*100000) - (b*10000)-(z*1000)-(x*100)-(u*10)
        if(v==s and u==r and x==t and z==w and b==y and d==a and f==c)or(v==r and u==t and x==w and z==y and b==a and d==c and f==e)or(v==t and u==w and x==y and z==a and b==c and d==e and f==g)or(v==w and u==y and x==a and z==c and b==e and d==g and f==i):
            flag_sub_number = True
    elif p<100000000:
        h = int(p/10000000)
        f = int((p-(h*10000000))/1000000)
        d = int((p-(h*10000000)-(f*1000000))/100000)
        b = int((p-(h*10000000)-(f*1000000)-(d*100000))/10000)
        z = int((p-(h*10000000)-(f*1000000)-(d*100000)-(b*10000))/1000)
        x = int((p-(h*10000000)-(f*1000000)-(d*100000)-(b*10000)-(z*1000))/100)
        u = int((p-(h*10000000)-(f*1000000)-(d*100000)-(b*10000)-(z*1000)-(x*100))/10)
        v = p - (h * 10000000)-(f*1000000)-(d*100000)-(b*10000)-(z*1000)-(x*100)-(u*10)
        if(v==s and u==r and x==t and z==w and b==y and d==a and f==c and h==e)or(v==r and u==t and x==w and z==y and b==a and d==c and f==e and h==g)or(v==t and u==w and x==y and z==a and b==c and d==e and f==g and h==i):
            flag_sub_number = True
    else:
        j = int(p/100000000)
        h = int((p-(j*100000000))/10000000)
        f = int((p-(j*100000000)-(h*10000000))/1000000)
        d = int((p-(j*100000000)-(h*10000000)-(f*1000000))/100000)
        b = int((p-(j*100000000)-(h*10000000)-(f*1000000)-(d*100000))/10000)
        z = int((p-(j*100000000)-(h*10000000)-(f*1000000)-(d*100000)-(b*10000))/1000)
        x = int((p-(j*100000000)-(h*10000000)-(f*1000000)-(d*100000)-(b*10000)-(z*1000))/100)
        u = int((p-(j*100000000)-(h*10000000)-(f*1000000)-(d*100000)-(b*10000)-(z*1000)-(x*100))/10)
        v = p -(j*100000000)- (h * 10000000)-(f*1000000)-(d*100000)-(b*10000)-(z*1000)-(x*100)-(u*10)
        if(v==s and u==r and x==t and z==w and b==y and d==a and f==c and h==e and j==g)or(v==r and u==t and x==w and z==y and b==a and d==c and f==e and h==g and j==i):
            flag_sub_number = True        
    
print(" is subnumber: ",flag_sub_number)




















































  
