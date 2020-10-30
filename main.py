import func as f

#c = f.LongAdd(f.conv(input()), f.conv(input()))  # +
#c = f.LongSub(f.conv(input()), f.conv(input()))   # +
A = '4D3C91C579C2C6216567A5241614B561ADDF76C4BB659E6FE7F65FF76A918C843F0458B3EF457BCD9022D78798A29462EC99C74E6674690267D3E9844251B39D'
B = 'DAF1ABDA4AD4D9FE3E36A529210C2AE99B905922FC0519798A26E351FE23AF375AD6BA288EE030B70DF0CE1CDF1E8B75BA56494DC6ED36B181814CD5783E6C81'
c = f.LongMul(f.conv(A), f.conv(B))             # +
d = f.LongDivMod(f.conv(c), f.conv(A))          # - + еще степень и проверки


#c = f.LongPower(f.conv(input(), 2, 16), f.conv(input(), 2, 16))
d = f.conv(c, 16, 32)
print(d)