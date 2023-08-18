from pojisteny import Pojisteny

class EvidencePojistnychUdalosti:

    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteneho(self, pojisteny):
        self.pojisteni.append(pojisteny)

    def zobraz_seznam(self):
        for pojisteny in self.pojisteni:
            print(pojisteny)

    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None
