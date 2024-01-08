class Nauczyciel:
    def __init__(self , _imie, _nazwisko, _włosy, _wzrost) -> None:
        self.imie = _imie
        self.nazwisko = _nazwisko
        self.włosy = _włosy
        self.wzrost =_wzrost


    def inf(self):
        print("=======================")
        print("informacje o nauczucielu ")
        print("=======================")
        print(f"nazwisko: {self.nazwisko}")
        print(f"włosy: {self.włosy}")
        print(f"imie: {self.imie}")
        print(f"wzrost: {self.wzrost}")

u1 = Nauczyciel("Monika", "Czerwonka", "długie", "niski")
u1.inf() 



class Polityk:
    def __init__(self , _imie, _nazwisko, _włosy, _wzrost) -> None:
        self.imie = _imie
        self.nazwisko = _nazwisko
        self.włosy = _włosy
        self.wzrost =_wzrost


    def inf(self):
        print("=======================")
        print("informacje o polityku")
        print("=======================")
        print(f"nazwisko: {self.nazwisko}")
        print(f"włosy: {self.włosy}")
        print(f"imie: {self.imie}")
        print(f"wzrost: {self.wzrost}")

u3 = Polityk("Szymon", "Hołownia", "krótkie", "przecietny")
u3.inf() 



class Zwierze:
    def __init__(self , _gatunek, _rasa, _siersc, _wzrost) -> None:
        self.gatunek = _gatunek
        self.rasa = _rasa
        self.siersc = _siersc
        self.wzrost =_wzrost


    def inf(self):
        print("=======================")
        print("informacje do adopcji")
        print("=======================")
        print(f"rasa: {self.rasa}")
        print(f"siersc: {self.siersc}")
        print(f"gatunek: {self.gatunek}")
        print(f"wzrost: {self.wzrost}")

u4 = Zwierze("pies", "chihuahua", "krótka", "do kostki")
u4.inf() 



class Influencer:
    def __init__(self , _imie, _nazwisko, _włosy, _wzrost) -> None:
        self.imie = _imie
        self.nazwisko = _nazwisko
        self.włosy = _włosy
        self.wzrost =_wzrost


    def inf(self):
        print("=======================")
        print("informacje o jupitezrze")
        print("=======================")
        print(f"nazwisko: {self.nazwisko}")
        print(f"włosy: {self.włosy}")
        print(f"imie: {self.imie}")
        print(f"wzrost: {self.wzrost}")

u2 = Influencer("Karol", "Wiśniewski", "łysy", "niski")
u2.inf() 
