import func
from func import *
import sys
import colorama
from colorama import Fore, Style
sys.setrecursionlimit(2000000)

def testGcdAndLcm():
    a = '0EC5BC6D07A5FE071949CD1B6FBA6E6A946EA60D31A8'
    b = '1D88627536B979CE29578D4BDA512642B3E03DDF0A51'
    s = time.time()
    print(gcd(a, b), "\nTime: " + str(time.time() - s) + " seconds")
    s = time.time()
    print(lcm(a, b), "\nTime: " + str(time.time() - s) + " seconds")

def Lab2Main():
    
    colorama.init()
    print(Fore.GREEN + 'Lab 2: ' + Style.RESET_ALL)
    #testGcdAndLcm()
    
    #ArithmeticMod()
    #test11()
    #test22()
    
if __name__ == "__main__":
    Lab2Main()
    
    
















    