hi,mi,hf,mf = (input().split(" "))
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)
h = int(0)
m = int(0)

if hi < hf:
    h = hf - hi
    if mi < mf:
        m = mf - mi
    elif mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    elif mi == mf:
        m = 0

elif hi > hf:
    h = (24 - hi) + hf
    if mi < mf:
        m = mf - mi
    elif mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    elif mi == mf:
        m = 0

elif hi == hf:
    if mi < mf:
        m = mf - mi
        h = 0
    elif mi > mf:
        m = (60 - mi) + mf
        h = 23
    elif mi == mf:
        h = 24
        m = 0

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h,m))
