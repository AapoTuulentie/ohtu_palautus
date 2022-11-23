from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tuotteet = []

    def tavaroita_korissa(self):
        if len(self.tuotteet) == 0:
            return 0
        maara = 0
        for ostos in self.tuotteet:
            maara += ostos.lukumaara()
        return maara

    def hinta(self):
        if len(self.tuotteet) == 0:
            return 0
        summa = 0
        for ostos in self.tuotteet:
            summa += ostos.hinta()
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.tuotteet:
            if Ostos(lisattava).tuotteen_nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(Ostos(lisattava).lukumaara())
                return
        
        self.tuotteet.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.tuotteet:
            if Ostos(poistettava).tuotteen_nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(-Ostos(poistettava).lukumaara())

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        ostokset = []
        for ostos in self.tuotteet:
            ostokset.append([ostos.tuotteen_nimi(), ostos.lukumaara()])

        return ostokset
