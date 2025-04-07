


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

# def more_wage(p:list,i:list):
#     """Shows people that are getting more/less than inputed wage
#      :p, list:  wage list:
#     :i, list:  people list:
#     """
#     losti=[]
#     lostp=[]
   
#     try:
#         märk=input("Kirjuta kas suurem (>) või väiksem (<): ")
#         if märk=="<":
#             palk=float(input("Kirjuta palga: "))
#             if palk >0:
#                 for o in range(p):
#                     if palk>int(p[o]):
#                         s=int(p[o])
#                         losti.append(i[o])
#                         lostp.append(s)
#         elif märk==">":
#             palk=float(input("Kirjuta palga: "))
#             if palk >0:
#                 for o in range(p):
#                     if palk<int(p[o]):
                        
#                         losti.append(i[o])
#                         lostp.append(int(p[o]))


#     except Exception as e:
#          print ("Viga:",e)
#     print(losti)
#     print(lostp)

   




    





