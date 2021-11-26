def f1(a):
    ilosc = 0
    for i in a:
        if i > 8 and i%2==0:
            ilosc += 1
    print(ilosc)

f1([1,2,4,6,2,22,33,44,56])

def f2(a1,a2):
    ilosc1=0
    ilosc2=0
    for i in a1:
        if len(str(i))==2:
            ilosc1 += 1
    for p in a2:
        if len(str(p))==2:
            ilosc2 += 1
    if ilosc1 == ilosc2:
        print(True)
    else:
        print(False)
                
f2([23,4,53],[44,32,42,534])                