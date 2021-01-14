from func import lcmp, sdth, ins, conv, BinConv, power2
from lab3 import bts, stb, Num
import colorama
from colorama import Fore, Style
import time

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
    tmp = []
    tmp.append(a[-1])
    for j in range(len(a) - 1):
        tmp.append(a[j])
    
    return tmp

def rsqrONB(a): 
    tmp = []
    for i in range(1, len(a)):
        tmp.append(a[i])
    tmp.append(a[0])
    return tmp

def mulONB(a, b, m): 
    d = []
    
    for k in range(len(a)):
        c = []
        for j in range(len(a)):
            tmp = 0
            for i in range(len(a)):
                tmp = tmp + a[i] * m[i][j]  
            c.append(tmp % 2)
        add = 0
        for n in range(len(c)):
            add = add + c[n] * b[n]
        d.append(add % 2)
        a = rsqrONB(a)
        b = rsqrONB(b)
        
    return d

    


def power(a, n):
    tmp = []
    n.reverse()
    for i in range(0, len(a)):
        tmp.append(1)
    
    for i in range(0, len(n)):
        if n[i] == 1:
            matr = multMatrix(tmp)
            tmp = mulONB(tmp, a, matr)
        a = stb(sqrONB(bts(a)))
    return tmp
    

    
def invONB(a): 
    print('a = ', a)
    a = stb(a)
    n = stb(conv(str(len(a) - 1), 2, 10))
    k = 1
    print('k = ', k)
    b = a
    for i in range(1, len(n)):
        print(Fore.RED + 'i = ' + str(i) + Style.RESET_ALL)
        d = power(b, stb(conv(str(2**k), 2, 10)))
        print('b^2 = ' + bts(d))
        b = mulONB(d, b, multMatrix(d))
        print('b = b^2 * b = ' + bts(b))
        k = 2*k
        print('k = ', k)
        if n[i] == 1:
            b = stb(sqrONB(bts(b)))
            print('b^2 = ' + bts(b))
            b = mulONB(b, a, multMatrix(b))
            print('b = b^2 * a = ' + bts(b))
            k = k + 1
            print('k = ', k)
    return bts(stb(sqrONB(bts(b))))


def tr(a = []):
    tmp = Num()
    for i in a:
        trc = tmp.addBig([i], [i+1])
    return trc

def Add(a, b):
    tmp = Num()
    s = time.time() 
    res = tmp.addPol(stb(a), stb(b))
    print(res + Fore.BLUE + "\nTime: " + str(time.time() - s) + " seconds" + Style.RESET_ALL )

def Sqr(a):
    s = time.time() 
    res = bts(sqrONB(a))
    print(res + Fore.BLUE + "\nTime: " + str(time.time() - s) + " seconds" + Style.RESET_ALL )

def Mul(a, b):
    s = time.time()
    res = bts(mulONB(stb(a), stb(b), multMatrix(a)))
    print(res + Fore.BLUE + "\nTime: " + str(time.time() - s) + " seconds" + Style.RESET_ALL )

def Trace(a):
    s = time.time()
    res = bts(tr(stb(a)))
    print(res + Fore.BLUE + "\nTime: " + str(time.time() - s) + " seconds" + Style.RESET_ALL )

def Power(a, n):
    s = time.time()
    res = bts(power(stb(a), stb(n)))
    print(res + Fore.BLUE + "\nTime: " + str(time.time() - s) + " seconds" + Style.RESET_ALL )
       
def Inv(a):
    s = time.time()
    res = invONB(a)
    print( "a^(-1) = " + res + Fore.BLUE + "\nTime: " + str(time.time() - s) + " seconds" + Style.RESET_ALL )

def ArithmeticONB(a, b, n): 
    #Add(a, b)
    #Mul(a, b)
    Trace(a)
    #Sqr(a)
    #Inv(a)
    #Power(a, n)

def t1():
    a = "11111001111011000001001110100010011100000111011111110000110001101011110100100011011100110100011000010011011100111100101110011101110011110001001110101101110000100000011111010"
    b = "11111001111011001101001110100010011100000111011111110000110001101011110100100011011100110100011000010011011100111100101110011101110011110001001110101101110000100000011111010"
    c = "11111001111011000101001110100010011100000111011111110000110001101011110100100011011100110100011000010011011100111100101110011101110011110001001110101101110000100000011111010"
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
    a = "11111001111011000001001110100010011100000111011111110000110001101011110100100011011100110100011000010011011100111100101110011101110011110001001110101101110000100000011111010"

    n =  stb(conv(str(2 ** m -1), 2, 10))
    a = stb(a)
    d = bts(power(a, n))
    
    if d == '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111':
        print("Nice")
    else:
        print("Хорошая попытка")
    
def Lab4Main():
    colorama.init()
    print(Fore.GREEN + 'Lab 4: ' + Style.RESET_ALL)
    a = '11100110010110001000101111110110100111010110101101111100111100101001100111000111010100000000111100000000111001000111000011101011000010000100111011101010101001110111011001101'
    b = '00111110010101100101000111010000100011001110101101000010101010100101101110111110011001011110110111101001110001001011010111011001101011110101000110111110101101111110110010011'
    n = '11100000001000001111000100111011101001110001000111110101111100100111011101001101101100000001110101011110010000111010110001101001000010110010100000100100000010001011101000110'
    ArithmeticONB(a, b, n)
    #t1()
    #t2()
    
if __name__ == "__main__":
    Lab4Main()