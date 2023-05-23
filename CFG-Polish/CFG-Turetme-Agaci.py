#201213093 - Buğra Han Okcebe

while True:
    de = 0
    dp = 0
    dallanmavar = 1


    def DallanmaVarmi():

        boy = len(tumagac)
        for i in range(boy):
            deger = tumagac[i]
            pozisyon = len(deger)
            for j in range(pozisyon):
                d = deger[j]
                if d in sozluk.keys():
                    de = i
                    dp = j
                    dallanmavar = 1

                    break
            else:
                continue

            break
        else:
            dallanmavar, de, dp = 0, 0, 0

        return (dallanmavar, de, dp)

    cfg = input("Cfg gir : ")
    # cfg = "S-->aa|bX|aXX,X-->ab|b"
    # cfg = "S-->aa|bX|aXX|aZ,X-->ab|b,Z-->a|bb"
    # cfg = "S-->aa|bX|aXX|aZ,X-->ab|b|Zb,Z-->a|bb"

    k = cfg.split(',')
    print('SATIRLAR:', k)

    ilk = True
    giris = ''
    sozluk = {}
    for i in k:
        degisken, degerler = i.split('-->')
        print('Degisken:', degisken, 'Degerleri:', degerler)
        sozluk[degisken] = degerler.split('|')

        if ilk == True:
            giris = degisken
            ilk = False

    print('-'*len('Sözlük: '+repr(sozluk)))
    print('Sözlük:', sozluk)
    print('-'*len('Sözlük: '+repr(sozluk)))

    tumagac = sozluk[giris]

    maxdongu = 100
    for dongusay in range(maxdongu):

        print('TÜM AĞAÇ:', tumagac)

        dallanmavar, de, dp = DallanmaVarmi()

        if dallanmavar == 1:
            eleman = tumagac[de]
            elemansol, elemansag = eleman[:dp], eleman[dp+1:]

            altdallar = []
            altdal = tumagac[de][dp]
            print(tumagac[de][dp])
            for dal in sozluk[altdal]:
                print(elemansol + dal + elemansag)
                altdallar.append(elemansol + dal + elemansag)

            tumagac[de:de+1] = altdallar
        else:
            break
    else:
        print()
        print('*** HATA VAR *** ')
        print('{} dallanma yapılamadı!!!!!!'.format(maxdongu))

    print('-'*len('TÜM AĞAÇ: '+repr(tumagac)))

    uretilenkelimeler = list(set(tumagac))
    uretilenkelimeler.sort()
    print('ÜRETİLEN KELİMELER:', uretilenkelimeler)


    tekrarlanankelimeler = tumagac.copy()

    for i in uretilenkelimeler:
        tekrarlanankelimeler.remove(i)

    tekrarlanankelimeler = list(set(tekrarlanankelimeler))
    tekrarlanankelimeler.sort()
    print('TEKRARLANAN KELİMELER:', tekrarlanankelimeler)
