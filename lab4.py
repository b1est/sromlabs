from func import lcmp, sdth, ins, conv, BinConv, power2
from lab3 import bts, stb, Num# add, addBig

def multMatrix(a, M = []): 
    for i in range(0, len(a)):
        M.append([])
        for j in range(0, len(a)):
            if (-(2 ** i) - (2 ** j)) % (2 * len(a) + 1) == 1 or (-(2 ** i) + (2 ** j)) % (2 * len(a) + 1) == 1 or ((2 ** i) - (2 ** j)) % (2 * len(a) + 1) == 1 or ((2 ** i) + (2 ** j)) % (2 * len(a) + 1) == 1:
                M[i].append(1) 
            else:
                M[i].append(0)
    return M

def sqrONB(a):
    a = stb(a)
    a.insert(0, a[-1])
    del a[- 1]
    return a

def mulONB(a, b, m): 
    d = []
    
    for k in range(0, len(a)):
        c = []
        for j in range(0, len(a)):
            tmp = 0
            for i in range(0, len(a)):
                tmp = a[i] * m[i][j] + tmp 
            c.append(tmp % 2)
        add = 0
        for i in range(len(c)):
            add = add + c[i] * b[i]
        d.append(add % 2)
        del add
        a.append(a[0])
        del a[0]
        b.append(b[0])
        del b[0]
    return d

def power(a):
    tmp = []
    tmp.append(a[-1])
    for j in range(len(a) - 1):
        tmp.append(a[j])
    a = tmp
    tmp.clear()
    return a
def powerN(n):
    
    powers = []
    left = []
    
    while n != 0:
        
        i = hpowerN(n)[0]
        left = hpowerN(n)[1]
        n -= 2**i
        
        powers.append(i)
        if n == 2:
            powers.append(2)
            return powers
    if powers[-1] == 0:
        del powers[-1]
    return powers 
 
def hpowerN(n, left = []):
    i = 1
    while 2**i < n and 2**i != n:
        i += 1 
    if 2**i > n:
        i -= 1
        if 2**i < n:
            n -= 2**i
            left.append(n)
            return i, left
        return i, left
    elif 2**i == n:
        return i, left
    else:
        print("smth wrong")

def f(n):
    tmp = []
    for i in range(1, len(n)):
        if i == 1:
            t = []
            t.append(n[0])
            t.append(n[1])
            tmp.append(t)
            del t
            
        else:
            tmp.append(n[i])
    return tmp
def hf(n):
    while len(n) != 1:
        n = f(n)
    return n
def power20(a, n, m = 173):
    if 2**m - 1 < len(n):
        print('power: ERROR')
        return -1
    n = int(conv(n, 10, 2))
    powers = powerN(n)
    for i in powers:
        for j in range(i):
            tmp = power(stb(a))
        i = tmp
    powers = hf(powers)
    

    
def invONB(a): 
    a = stb(a)
    tmp = a
    n = BinConv(conv(str(len(a) - 1), 16, 10))
    k = 1
    for i in range(1, len(n)):
        num = stb(sqrONB(tmp))
        num = power(tmp, 2**k)
        matr = multMatrix(num)
        tmp = mulONB(num, tmp, matr)
        k = 2*k
        if n[i] == 1:
            tmp = stb(sqrONB(tmp))
            TMPmtr = multMatrix(tmp)
            tmp = mulONB(tmp, a, TMPmtr)
            k = k + 1
    tmp = stb(sqrONB((tmp)))
    return tmp


def tr(a = [], trc= [0]):
    tmp = Num()
    for i in range(len(a)):
        trc = tmp.addBig(trc, a)
        a = stb(sqrONB(a))
    return trc

def Add():
    tmp = Num()
    a = "100000000000000000100000000000000000000000000000000000000000000000000000000010000000000000000001000000000000000000000000000000000001000000000000000000000000000000000000000001"
    b = "100000000000000000100000000000000000000000100000000000000100000000000000000010000000000000000001000000001000000000000000000100000001000000000000000000010000000000000000000001"
    if tmp.addPol(stb(a), stb(b)) == '' or tmp.addPol(stb(a), stb(b)) is None:
        print(0)
    print(tmp.addPol(stb(a), stb(b)))

def Sqr():
    a = "10000000000000000010000000000000000000000000000000000000000000000000000000001000000000000000000100000000000000000000000000000000001000000000000000000000000000000000000000001"
    print(bts(sqrONB(a)))

def Mul():
    a = "10000000000000000010000000000000000000000000000000000000000000000000000000001000000000000000000100000000000000000000000000000000001000000000000000000000000000000000000000001"
    b = "10000000000000000010000000000000000000000010000000000000010000000000000000001000000000000000000100000000100000000000000000010000000100000000000000000010000000000000000000001"
    
    res = mulONB(stb(a), stb(b), multMatrix(a))
    print(bts(res))

def Trace():
    a = "10000000000000000010000000000000000000000000000000000000000000000000000000001000000000000000000100000000000000000000000000000000001000000000000000000000000000000000000000001"
    print(bts(tr(stb(a))))

def Power():
    a = "10000000000000000010000000000000000000000000000000000000000000000000000000001000000000000000000100000000000000000000000000000000001000000000000000000000000000000000000000001"
    power20(a, '01010')
    #print(bts(power(stb(a), 2)))

def ArithmeticONB(): 
    #Add()
    #Sqr()
    #Mul()
    #Trace()
    Power()

def t1():
    a = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    b = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    c = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    tmp = Num()
    summ = tmp.addBig(stb(a), stb(b))
    matrSumm= multMatrix(summ)
    res1 = mulONB(summ, stb(c), matrSumm)
    matrA = multMatrix(a)
    m1 = mulONB(stb(a), stb(c), matrA)
    matrB = multMatrix(b)
    m2 = mulONB(stb(b), stb(c), matrB)
    res2 = tmp.addBig(m1, m2)

    if res1 == res2:
        print("Nice")
    else:
        print("Nice try")

def t2(m = 173):
    a = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"

    n = 2 ** m -1
    print(n) 

    d = bts(power(stb(a), 2**m))
    d = div()
    print(d)
    if bts(d) == '1':
        print("nice")
    else:
        print("nice try")
    
def main():
    ArithmeticONB()
    #t1()
    #t2()
if __name__ == "__main__":
    main()