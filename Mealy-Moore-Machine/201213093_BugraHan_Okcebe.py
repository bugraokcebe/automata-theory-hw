#201213093-BuğraHan-Okcebe

def mooreMac():


    dosyaAdresi = "C:/Users/asus/OneDrive/Masaüstü/201213093_BugraHan_Okcebe/moore-txt/"

    fGecisTmoore = 'Gecistablosu.txt'
    fOutputTmoore = 'Output.txt'

    GecisTmoore = {}
    OutputTmoore = {}

    ilkgiris = ''

    with open(dosyaAdresi+fGecisTmoore) as f:
        dizi1 = f.readlines()
        print(dizi1)
        baslik = dizi1[0]
        girdi = baslik.strip().split(sep='\t')[1:]
        print(girdi)
        GirdiAdedi = len(girdi)
        print(GirdiAdedi)

        say = 0
        print('------565')
        for line in dizi1[1:]:
            satir = line.strip().split(sep='\t')
            print(satir)
            d = {girdi[i]:satir[i+1] for i in range(GirdiAdedi)}
            print(d)
            GecisTmoore[satir[0]] = d
            print(GecisTmoore)
            if say == 0:
                ilkgiris = satir[0]
            say = say + 1

            

    with open(dosyaAdresi+fOutputTmoore) as f:
        dizi1 = f.readlines()

        for line in dizi1[1:]:
            satir = line.strip().split(sep='\t')
            print('######')
            print(satir)
            OutputTmoore[satir[0]] = satir[1]
            print(OutputTmoore)


    girisMoore = input('Lütfen giriş stringini giriniz:')
    ######################################### girisMoore="aaababbaabb" #######################################################

    print('\n'*2)
    print('Adım Adım Gösterim')
    print('-----------------------------------------------------------')
    stateler = []
    ciktilar = []
    stateler.append(ilkgiris)
    ciktilar.append(OutputTmoore[ilkgiris])
    print('2222--2-2')
    state =  ilkgiris

    for g in girisMoore:
        state = GecisTmoore[state][g]
        print(state)
        cikti = OutputTmoore[state]
        print('Girdi:',g, 'State:',state, 'Çıktı:',cikti)
        stateler.append(state)
        ciktilar.append(cikti)

    print('\n'*2)
    print('Toplu Gösterim:')
    print('-----------------------------------------------------------')
    print('Girdi:',girisMoore)
    print('Stateler:', stateler)
    print('Outputlar:',ciktilar)
    print('Çıktı:',''.join(ciktilar))

def mealyMac():

    dosyaAdresi = "C:/Users/asus/OneDrive/Masaüstü/201213093_BugraHan_Okcebe/mealy-txt/"

    fGecisTmealy = 'GecisDiyagrami.txt'

    GecisTmealy = {}


    first = ''


    with open(dosyaAdresi+fGecisTmealy) as f:
        dizi2 = f.readlines()

        say = 0
        for line in dizi2[1:]:
            satir = line.strip().split(sep='\t')
            key = satir[0] + ' - ' + satir[1]
            print(key)
            GecisTmealy[key] = {'output':satir[2],'yenidrm':satir[3]}

            if say == 0:
                first = satir[0]
            say = say + 1



    girisMealy = input('Lütfen giriş stringini giriniz:')
    ########################################### girisMealy="1100010110" #############################################################3

    print('\n'*2)
    print('Adım Adım Gösterim')
    print('-----------------------------------------------------------')
    stateler = []
    ciktilar = []
    stateler.append(first)

    state =  first

    for g in girisMealy:
        key = state + ' - ' + g
        state = GecisTmealy[key]['yenidrm']
        cikti = GecisTmealy[key]['output']
        print('Girdi:',g, 'State:',state, 'Çıktı:',cikti)
        stateler.append(state)
        ciktilar.append(cikti)

    print('\n'*2)
    print('Toplu Gösterim:')
    print('-----------------------------------------------------------')
    print('Girdi:',girisMealy)
    print('Stateler:', stateler)
    print('Outputlar:',ciktilar)
    print('Output:',''.join(ciktilar))

while True:
    print("Hangi makineden işlem yapmak istiyorsunuz")
    print("Txtlerinizi güncellediğinizden emin olun!")
    print("1-> Moore-Machine")
    print("2-> Mealy-Machine")
    secim=int(input())

    if secim==1:
        mooreMac()
    elif secim==2:
        mealyMac()
    input("MENUYE DONMEK ICIN 'E' YE BASINIZ...")