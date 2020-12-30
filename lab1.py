import func as f
import sys
import colorama
from colorama import Fore, Style
import time
sys.setrecursionlimit(20000)

def Lab1Main():
    colorama.init()
    print(Fore.GREEN + 'Lab 1: ' + Style.RESET_ALL)
    A = '170076B15F9575D21DE39D5C429799BBCDDB867016DE2248E3CFDE73A4D70C8636A9E41ABE671E7B9FB4739A5FF64DF9D0D3A64E0C9B20BFE58F1C62B28477EE9FD202010BAC440ADF3CA016A32DB844F23DEC2AB93AE869A6262FC23C5CE419807CDBA930A5433884E3B34B22477289BD3A7712CDD4B4110BD9887E7428FDF7'
    B = '09D1C2D6E1591932F73C2F499C4E0A2E252DE828CDA7842CE0972C4101FE772B56C45C475EDDEDAEC2DBD13E375E02D2C149B69AB51FF3F94533CA34A815484EC86DACE936BDC62B5F3F9EB6F5BE6BD253E256181D35D7D63EE24459824D462C53676E3DFF98700415ADA65FDA7CBD3B3F359C817F52BEDA70C9DD85F68473C6'   
    C = '20D2398840EE8F05151FCCA5DEE5A3E9F3096E98E485A675C4670AB4A6D583B18D6E40621D450C2A629044D8975450CC921D5CE8C1BB14B92AC2E6975A99C03D683FAEEA426A0A363E7C3ECD98EC241746204242D670C03FE508741BBEAA2A45D3E449E7303DB33C9A9159AAFCC42FC4FC7013944D2772EB7CA366046AAD71BD'
    
    print('A = ' + A) 
    print('B = ' + B)
    print('C = ' + C)
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    s = time.time()
    print('A + B = ' + f.rlshift(f.conv((f.LongAdd(f.conv(A), f.conv(B))), 16 , 32)) + Fore.BLUE + "\nTime: " + str(time.time() - s) + " seconds" + Style.RESET_ALL )
    print('A - B = ' + f.rlshift(f.conv((f.LongSub(f.conv(A), f.conv(B))), 16 , 32)) + Fore.BLUE + "\nTime: " + str(time.time() - s) + " seconds" + Style.RESET_ALL )
    print('A * B = ' + f.rlshift(f.conv((f.LongMul(f.conv(A), f.conv(B))), 16 , 32)) + Fore.BLUE + "\nTime: " + str(time.time() - s) + " seconds" + Style.RESET_ALL )
    print('A / B = ' + f.diV(A, B)[0] + ' ( R = ' + f.diV(A, B)[1] + ')' + Fore.BLUE + "\nTime: " + str(time.time() - s) + " seconds" + Style.RESET_ALL )
    f.poW(A, B)
    f.tests(A, B, C)
    B = '2'
    

if __name__ == "__main__":
   Lab1Main()