from pojisteny import Pojisteny
from evidence import EvidencePojistnychUdalosti

def main():
    evidence = EvidencePojistnychUdalosti()


    while True:
        print("\n1 - Vytvořit pojištěného")
        print("2 - Zobrazit seznam pojištěných")
        print("3 - Vyhledat pojištěného")
        print("4 - Ukončit")

        volba = input("Zvolte akci: ")

        if volba == "1":
            jmeno = input("Jméno: ")
            prijmeni = input("Příjmení: ")
            vek = int(input("Věk: "))
            telefon = input("Telefonní číslo: ")
            pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
            evidence.pridej_pojisteneho(pojisteny)
            print("Pojištěný byl vytvořen.")

        elif volba == "2":
            print("\nSeznam pojištěných:")
            evidence.zobraz_seznam()

        elif volba == "3":
            jmeno = input("Jméno: ").strip()
            prijmeni = input("Příjmení: ").strip()
            nalezeny_pojisteny = evidence.vyhledej_pojisteneho(jmeno, prijmeni)
            if nalezeny_pojisteny:
                print("\nNalezený pojištěný:")
                print(nalezeny_pojisteny)
            else:
                print("Pojištěný nebyl nalezen.")

        elif volba == "4":
            break

        else:
            print("Neplatná volba.")

if __name__ == "__main__":
    main()
