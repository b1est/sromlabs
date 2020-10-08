import func as f

#c = f.LongAdd(f.conv(input()), f.conv(input()))
#c = f.LongSub(f.conv(input()), f.conv(input()))   
#c = f.LongMul(f.conv(input()), f.conv(input()))
#c = f.LongDivMod(f.conv(input()), f.conv(input()))


c = f.LongPower(f.conv(input(), 2), f.conv(input(), 2))
#c = f.conv(c, 16, 32)
print(c)