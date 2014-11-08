f = open('menu.txt','r')
lancuch = ""
while 1:
    line = f.readline()
    if not line:break
    lancuch += line
f.close()
wyjscie=lancuch.lower()
wyjscie=wyjscie.split()
menu= dict(zip(*[iter(wyjscie)]*2))
menu = dict((k, float(v)) for k, v in menu.iteritems())
def zamowienie(zamowienie):
    cena = 0
    for i in zamowienie:
        if i in menu:
            cena += menu[i]
    return cena
print zamowienie(['frytki','lody'])