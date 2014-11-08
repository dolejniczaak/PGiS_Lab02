import string
from collections import Counter
from operator import index

f = open('harry.txt','r')
lancuch = ""
while 1:
    line = f.readline()
    if not line:break
    lancuch += line
f.close()

wyjscie=lancuch.lower()

for c in string.punctuation:
    wyjscie= wyjscie.replace(c,"")
    
wyjscie=wyjscie.split()

def liczenie(wyjscie):
    c=Counter(wyjscie)
    w=c.values()
    k=c.keys()
    indeks=w.index(max(w))
    wartosc=w[indeks]
    slowo=k[indeks]
    statystyki =open('statystyki.txt', 'w')
    statystyki.write("Najczesciej wystepujace w tekscie slowo to: "+slowo+". Wystepuje ono "+ str(wartosc)+" razy.")
    statystyki.close()  
    
liczenie(wyjscie)  

