#User ID: 34114
#Team ID: CSWC1223
#Email: castusmail@gmail.com

def fac(n):
    if n == 1:
        return 1
    return fac(n-1)*n


for i in range(1,20):
    for j in range(i,20):
        t1 = fac(i)
        t2 = fac(j)
        f1 = t1*t2
        f2 = t1+t2
        d = f1-f2
        if d < 0:
            continue
        f = float(d**.5)
        k = int(f)
        if not k:
                    continue
        if f1 == f2+k*k:
            print i
            print j
            print k
            print "END"
            
