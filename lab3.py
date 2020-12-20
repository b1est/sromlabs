from func import lcmp, sdth, ins, BinConv, rBinConv, conv, stb, bts
import time


class Num:
    def __init__(self):
        self.polynom = "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000111"
        self.m = 173
   
    def modb(self, bigNum, a, b = 2):
        bigNum.reverse()
        carry = 0
        res = []
        for i in range(len(bigNum)):
            temp = carry + a * bigNum[i]  
            res.append(temp % b)
            carry = temp // b
        if carry != 0:
            res.append(carry)
        res.reverse()
        bigNum.reverse()
        return res

    def mulL(self, a, b, e = 2): 
        if len(a) > len(b):
            x = a
            a = b
            b = x    
        res = []
        b.reverse()
        for i in range(len(b)):
            tmp = Num()
            temp = tmp.modb(a, b[i], e)
            temp = sdth(stb(temp), i)
            
            res = tmp.addBig(temp, res)
        return res
        
    def divL(self, a, b):
        k = len(b)
        r = a
        q = []
        if type(b) == str:
            b = stb(b)
        while lcmp(r, b) == 1 or lcmp(r, b) == 0:
            t = len(r)
            
            c = sdth(b, t-k)
            tmp = Num()
            r = tmp.addBig(r, c)
            q = ins(q, t-k)
            while(len(r) != 0):
                if r[0] == 0:
                    del r[0]
                else:
                    break
        return q, r

    def addPol(self, a, b):
        if len(a) < len(b):
            x = a
            a = b
            b = x
        a.reverse()
        r = []
        b.reverse()
        for i in range(len(a)):
            temp = 0
            if len(b) > i:
                temp = b[i]
            r.append((a[i] + temp) % 2)
        r.reverse()
        res = bts(r)
        return res

    def addBig(self, a, b):
        if len(a) < len(b):
            x = a
            a = b
            b = x
        res = []
        a.reverse()
        b.reverse()
        for i in range(len(a)):
            tmp = 0
            if len(b) > i:
                tmp = b[i]
            res.append((a[i] + tmp) % 2)
        res.reverse()
        return res

    def sqr(self, a):
        p = stb(self.polynom)
        nA = len(a) - 1
        for i in range(nA):
            a.insert(i*2 + 1, 0)
        r = Num()
        res = r.divL(a.copy(), p)[1]
        return res

    
    def mulPoly(self, a, b):
        tmp = Num()
        aBin = stb(a)
        bBin = stb(b)
        pol = stb(self.polynom)

        mul = tmp.mulL(aBin, bBin, 2)
        div = tmp.divL(mul, pol)[1]
        while(len(div) > self.m):
            del div[0]
        num = bts(div)
        return num

    def Tr(self, a):
        tmp = Num()
        a = stb(a)
        pol = stb(self.polynom)
        tr = [0]
        for i in range(0, self.m):
            tr = tmp.addBig(tr.copy(), a.copy())
            a = tmp.sqr(a.copy())
        res = bts(tr)
        del tmp
        return res
    def poW(self, a, n):
        tmp = Num()
    
        b = [1]
        a = stb(a)
        e = stb(n)
        e.reverse()
        
        for i in range(len(e)):
            if e[i] == 1:
                b = tmp.mulL(b.copy(), a.copy())
                b = tmp.divL(b.copy(), self.polynom)[1]
            a = tmp.sqr(a.copy())
            a = tmp.divL(a.copy(), self.polynom)[1]
        res = b
        return res

    def inv(self, a):
        tmp = Num()
        a = stb(a)
        n = str(bin((2 ** self.m) - 2))
        n = n[2::]
        tmp = tmp.poW(a, n)
        return tmp

    @staticmethod
    def Arithmetic(a, b = None, n = None):
        Add(a, b)
        Mul(a, b)
        Trace(a)
        Sqr(a)
        Power(a, n)
        Inv(a)
    @staticmethod
    def tests():
        a = "10000000000000000000000000000000000000000010000000000000000000010000000000000000000000000000000000000000010000000000100000000000000000100000000000000000000011001001"
        b = "10000000000000001000000000000000000000000000000010000000000010000000000000000000000000000000000000000000010000000000100000000001000000000000000000000000000011001001"
        c = "10000000010000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000010000000000100000000000000000000000000000000100000011001001"
        t1(a, b, c)
        t2('10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001')

def Add(a, b):
    num = Num()
    s = time.time() 
    res = bts(num.addBig(stb(a), stb(b)))
    
    print(res + "\nTime: " + str(time.time() - s) + " seconds")

def Mul(a, b):
    num = Num()
    s = time.time()
    res = num.mulPoly(a, b)
    print(res + "\nTime: " + str(time.time() - s) + " seconds")

def Trace(a):
    num = Num()
    s = time.time()
    res = num.Tr(a)
    print(res + "\nTime: " + str(time.time() - s) + " seconds")

def Sqr(a):
    num = Num()
    s = time.time()
    a = stb(a)
    p = stb(num.polynom)
    res = num.sqr(a)
    print(bts(res) + "\nTime: " + str(time.time() - s) + " seconds")

def Power(a, n):
    num = Num()
    s = time.time()
    r = num.poW(a, n)
    print(bts(r) + "\nTime: " + str(time.time() - s) + " seconds")

def Inv(a):
    num = Num()
    s = time.time()
    r = num.inv(a)
    print(bts(r) + "\nTime: " + str(time.time() - s) + " seconds")

def t1(a, b, c): 
    
    n = Num()
    a = stb(a)
    b = stb(b)
    c = stb(c)
    res1 = n.mulPoly(bts(n.addBig(a.copy(), b.copy())), c)
    res2 = n.addPol(stb(n.mulPoly(bts(a), bts(c))), stb(n.mulPoly(bts(b), bts(c))))
    if res1 == res2:
        print("ok.")
    else:
        print("no")

def t2(a):
    
    num = Num()
    n = 2 ** num.m - 1
    n = str(bin(n))
    n = bts(n[2:])
    d = num.poW(a, n)
    if bts(d) == '1':
        print("ok.")
    else:
        print("no.")

def main():
    num = Num()
    a = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    b = "10000000000000000000010000100000000100000000001000000000100000000010001000000000100000000000000000000000000000000000000000000000000000000000000000000000000011001001"
    n = "111111111111111111011111111111111111111111101111111111111111111111111111111111111111111111111110"
    num.Arithmetic(a, b, n)
    num.tests()



    
if __name__ == "__main__":
    main()