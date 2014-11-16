from math import sqrt
class zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def get_r(self):
        return self.__r
    def set_r(self,r):
        self.__r=r
    def get_i(self):
        return self.__i
    def set_i(self,i):
        self.__i=i
    def suma(self, zespolona):
        print "suma tych dwoch liczb zespolonych wynosi: "+str(self.r+zespolona.r) +str(self.i+zespolona.i)+'*i'
    def odejmij(self, zespolona):
        print "roznica tych dwoch liczb zespolonych wynosi: "+str(self.r-zespolona.r) +str(self.i-zespolona.i)+'*i'
    def modul(self):
        wart=sqrt((self.i)**2+(self.r)**2)
        print "modul z danej liczby zespolonej to: "+ str(wart)
    def wyswietl(self):
        if self.i>0:
            znak="+"
        else:
            znak=""
        print "dana liczba zespolona ma postac: "+str(self.r)+ znak+str(self.i)+"*i"
x=zespolona(3.0, -4.5)
y=zespolona(4.0, -3.5)
zespolona.suma(x, y)
zespolona.odejmij(x, y)
zespolona.modul(x)
zespolona.wyswietl(x)