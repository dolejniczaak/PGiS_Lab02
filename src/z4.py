class Pies:
    def __init__(self, imie, wiek):
        self.imie=imie
        self.wiek=wiek
    def get_imie(self):
        return self.__imie
    def set_imie(self, imie):
        self.__imie=imie
    def get_wiek(self):
        return self.__wiek
    def set_wiek(self,wiek):
        self.__wiek=wiek
    def szczekaj(self):
        print "Hau hau!"
    def opisz(self):
        print "Wabie sie : "+self.imie+ " i mam "+str(self.wiek)+" lat."
class PiesObronny(Pies):
    def __init__(self,imie,wiek,zlosc):
        Pies.__init__(self, imie, wiek)
        self.zlosc=zlosc
    def get_zlosc(self):
        return self.__zlosc
    def set_zlosc(self, zlosc):
        self.__zlosc=zlosc
    def warcz(self):
        if (self.zlosc==False):
            print "Nie bede warczal, bo nie jestem zly"
        else:
            print "Wrauuu! Pies taki agresywny!"
    def atakuj(self):
        print "Atakuje!"
class PiesDomowy(Pies):
    def __init__(self, imie, wiek,iloscZnanychSztuczek):
        Pies.__init__(self, imie, wiek)
        self.iloscZnanychSztuczek=iloscZnanychSztuczek
    def get_iloscZnanychSztuczek(self):
        return self.__iloscZnanychSztuczek
    def set_iloscZnanychSztuczek(self, iloscZnanychSztuczek):
        self.__iloscZnanychSztuczek=iloscZnanychSztuczek
    def zabawiajCzlowieka(self):
        print "Hej czlowiek! Znam az "+str(self.iloscZnanychSztuczek)+" zabawnych sztuczek!"
class PiesBroniacyDomu(PiesObronny,PiesDomowy):
    def __init__(self,imie, wiek,zlosc,iloscZnanychSztuczek,adresPobytu):
        PiesDomowy.__init__(self, imie, wiek, iloscZnanychSztuczek)
        PiesObronny.__init__(self, imie, wiek, zlosc)
        self.adresPobytu=adresPobytu
    def get_adresPobytu(self):
        return self.__adresPobytu
    def set_adresPobytu(self, adresPobytu):
        self.__adresPobytu=adresPobytu
    def mieszka(self):
        print "Mieszkam pod adresem: "+self.adresPobytu

Burek=PiesBroniacyDomu("Burek",5,True,5,"Drzewce 24")
print Burek.szczekaj(), Burek.opisz(),Burek.mieszka(), Burek.atakuj(), Burek.zabawiajCzlowieka(), Burek.warcz()