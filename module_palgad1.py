





p=[]
i=[]
def add_peson(p:list,i:list):
    """Function adds person and his wage to the list.
    :p, list:  wage list:
    :i, list:  people list:

    """
    while True:
        try:
                    try:
                        nimi=input("Nimi: ")
                        if nimi.isalpha():
                            try:
                                palk=float(input("Palk: "))
                            except:
                                print("Palk on arv!")
                                
                           
                            print("Andmed on lisatud")
                            break
                    except:
                        print("Kirjuta ainult tähtede kasutades")

        except:
            print("Sisesta palun arv suurem kui null")
    p.append(palk)
    i.append(nimi)

def del_person(p:list,i:list):
    """Function deletes person and his wage from lists
    :p, list:  wage list:
    :i, list:  people list:
    """
    name=input("Sisesta nimi, mida tahate kustutada: ")
    try:
        if name.isalpha():
            k=i.count(name)
            if k>0:
                for j in range(k):

                    ind=i.index(name)
                    p.pop(ind)
                    i.remove(name)
                else:
                    print("Andmed puuduvad ")
    except:
        print("Kirjuta ainult tätede kasutades")

def max_wage(p:list,i:list):
    """Function gives max wage reciever
    :p, list:  wage list:
    :i, list:  people list:
    """
    maxx=p.copy()
    maxx.sort(reverse=True)
    ind=p.index(maxx[0])
    print(f"Maksimaalne palk: {maxx[0]}\nPalga saaja: {i[ind]}")


def min_wage(p:list,i:list):
    """Function gives max wage reciever
    :p, list:  wage list:
    :i, list:  people list:
    """
    mini=min(p)
    print(f"Väiksem palk on {mini}")
    k=p.count(mini)
    ind=p.index(mini)
    for j in range(k):

                    ind=p.index(mini)
                    print(f"Saab kätte {i[ind]}")
                    ind=ind+1

def sort_wage(p:list,i:list):
    """Function sorts lists both ways
    :p, list:  wage list:
    :i, list:  people list:
    """
    a=0 
    pal=p.copy()
    pal.sort()
    nam=[]
    for l in p:
       
        ind=p.index(pal[a])

        nam.append(i[ind])
        a+=1
    print("Kasvav järjekord")
    print(pal)
    print(nam)
    a=0 
    pal=p.copy()
    pal.sort(reverse=True)
    nam=[]
    for l in p:
       
        ind=p.index(pal[a])

        nam.append(i[ind])
        a+=1
    print("Kahanev järjekord")
    print(pal)
    print(nam)

def equal_wage(p:list,i:list):
    """Näitab palju võrdsa palga omanikke on
    :p, list:  wage list:
    :i, list:  people list:
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1

def find_wage(p:list,i:list):
    """Teeb palgaotsingu isiku nime järgi
    :p, list:  wage list:
    :i, list:  people list:
    """
    name=input("Sisesta nimi, mida tahate otsida: ")
    try:
        if name.isalpha():
            k=i.count(name)
            if k>0:
                for j in range(k):

                    ind=i.index(name)
                    print(f"{name} saab kätte {p[ind]}")
                    ind=ind+1
                else:
                    print("Andmed puuduvad ")
    except:
        print("Kirjuta ainult tätede kasutades")

def tax_wage(p:list,i:list):
    """Shows wage after taxes
     :p, list:  wage list:
        :i, list:  people list:
        """
    name=input("Sisesta nimi, kelle palga maksuga tahate vaadata: ")
    try:
        if name.isalpha():
            k=i.count(name)
            if k>0:
                for j in range(k):

                    ind=i.index(name)
                    notax=float(p[ind])
                    tax=notax-(notax*0.2)
                    print(i[ind])
                    print(f"Maksuga saab:{tax}")
                    

                    
                else:
                    print("Andmed puuduvad ")
    except:
        print("Kirjuta ainult tätede kasutades")





def top(p:list,i:list):
 """Function shows top n "rich" people and n "poor" people
    :p, list:  wage list:
    :i, list:  people list:
    """
 try:
     T=int(input("Kirjutate palju rikkamad ja vaesemad inmesi tahate näha: "))
     if T>0:

         a=0 
         pal=p.copy()
         pal.sort()
         nam=[]
         for l in p:
       
                ind=p.index(pal[a])

                nam.append(i[ind])
                a+=1
         print("Vaesemad ")
         for s in range(T):
             print(nam[s])
         a=0 
         pal=p.copy()
         pal.sort(reverse=True)
         nam=[]
         for l in p:
       
                ind=p.index(pal[a])

                nam.append(i[ind])
                a+=1
 
         print("Rikkamad")
         for x in range(T):

            print(nam[x])
     else:
        print("Kirjuta numbri")
 except:
     print("Viga!")

def name_sort(p:list,i:list):
        """Sorts names list A-Z or Z-A
        :p, list:  wage list:
        :i, list:  people list:
        """
        soov=int(input("Kui tahate sorteerida A-Z - sisestate 1\nKui soovite sorteerida Z-A - sisestage 2\n"))
        if soov==1 or soov==2:
            if soov==1:
                a=0 
                ini=i.copy()
                ini.sort()
                wag=[]
                for l in p:
       
                    ind=i.index(ini[a])

                    wag.append(p[ind])
                    a+=1
            elif soov==2:
                a=0 
                ini=i.copy()
                ini.sort(reverse=True)
                wag=[]
                for l in p:
       
                    ind=i.index(ini[a])

                    wag.append(p[ind])
                    a+=1
        print("Nimed A-Z")
        print(ini)
        print(wag)




    





