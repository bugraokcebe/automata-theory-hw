#201213093 - Buğra Han Okcebe

def operatorMu(c):
    return ((c == '+') | (c == '-') | (c == '/') | (c == '*'))

def operator(c):
    if c =='+':
        return 0
    elif c=='-':
        return 1
    elif c=='*':
        return 2
    elif c=='/':
        return 3
    else:
        return -1

def fonk (c,birinciDeger,ikinciDeger):
    oprt = operator(c)
    if (oprt == 0) : 
        return birinciDeger + ikinciDeger
    elif (oprt == 1): 
        return birinciDeger - ikinciDeger
    elif (oprt == 2): 
        return birinciDeger * ikinciDeger
    elif (oprt == 3): 
        return birinciDeger / ikinciDeger
    else :
        print("operatör değil")
        return -1

#--------------------------------------------------------------------------------------

while True:
    yigin = []
    kuyruk = []
    List = []
    karakterList = []                                                                
    sonKarakter =''                                                                
    sonuc=-1

    print('-----------------------------------------------------------')
    notasyon = input("Polish Notation :")
    List = notasyon.split(" ")
    print('-----------------------------------------------------------')

    boolDeger = False
    sonKarakter=""

    for i in List :
        if(operatorMu(i)):
            boolDeger=True
            sonKarakter=i
            yigin.append(i)
        elif(operatorMu(i)==False):
            karakterList.append(int(i))
            if(len(karakterList)==2 ):
                if(boolDeger):
                    sonuc = fonk(yigin[len(yigin)-1],karakterList[0],karakterList[1])
                    del karakterList[0:]
                    del yigin[len(yigin)-1]
                    kuyruk.append(sonuc)
                    boolDeger=False
                else:
                    kuyruk.append(karakterList[0])
                    kuyruk.append(karakterList[1])
            else:
                if(i == List[-1]):
                    kuyruk.append(int(i))
                    print(i)


    lenght = len(yigin)
    for i in range(lenght):
        sonuc = fonk(yigin[len(yigin)-1],kuyruk[0],kuyruk[1])
        del kuyruk[0:2]
        kuyruk.insert(0,sonuc)
        del yigin[len(yigin)-1]
    print("Sonuç :",kuyruk[0])
    print('-----------------------------------------------------------')