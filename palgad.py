from module_palgad1 import *


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]


while True:
    print("Andmed: ")
    print(inimesed)
    print(palgad)
    print("Vajua:\n1-Andmete lisamiseks\n2-Andmete kustutamiseks nime järgi\n3-Maksimaalse palka saaja näitamiseks}\n4-Väiksema palga näitamiseks\n5-Sorteerida listid kahanevas ja kasvavas järjekorras\n6-Vaadata kui palju võrdsa palga saajaid on\n7-Palgaotsing nime järgi\n8-Vaadata kui palju inimene saab tulumaksuga\n9-Koostada top rikkamad ja vaesemad\n10-Sorteerida kas A-Z või Z-A\n0-Quit")
    v=int(input())
    if v==1:
         k=int(input("Palju inimesi soovite lisada? "))
         if k>0:
            for l in range(0,k):
               add_peson(palgad,inimesed)
    elif v==2:
        k=int(input("Palju inimesi soovite kustutada ?"))
        if k>0:
            for l in range(k):
                del_person(palgad,inimesed)
    elif v==3:
        max_wage(palgad,inimesed)
    elif v==4:
        min_wage(palgad,inimesed)
    elif v==5:
        sort_wage(palgad,inimesed)
    elif v==6:
        equal_wage(palgad,inimesed)
    elif v==7:
        find_wage(palgad,inimesed)
    elif v==8:
       tax_wage(palgad,inimesed)
    elif v==9:
        top(palgad,inimesed)
    elif v==10:
        name_sort(palgad,inimesed)
    elif v==0:
        break
    else:
        print("Numbrid 0-10")
