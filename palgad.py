from module_palgad1 import *


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]


while True:
    print("Andmed: ")
    print(inimesed)
    print(palgad)
    print("Vajua:\n1-Andmete lisamiseks\n2-Andmete kustutamiseks nime järgi\n3-Maksimaalse palka saaja näitamiseks}\n4-Väiksema palga näitamiseks\n5-Sorteerida listid kahanevas ja kasvavas järjekorras\n6-\n7-Palgaotsing nime järgi\n8-Inimesed kes saavad palga suurem või väiksem kui valitud palg")
    v=int(input())
    if v==1:
         k=int(input("Palju inimesi soovite lisada? "))
         if k>0:
            for l in range(0,k):
               add_peson(palgad,inimesed)
    if v==2:
        k=int(input("Palju inimesi soovite kustutada ?"))
        if k>0:
            for l in range(k):
                del_person(palgad,inimesed)
    if v==3:
        max_wage(palgad,inimesed)
    if v==4:
        min_wage(palgad,inimesed)
    if v==5:
        sort_wage(palgad,inimesed)
    if v==6:
        print(2)
    if v==7:
        find_wage(palgad,inimesed)
    if v==8:
        more_wage(palgad,inimesed)

