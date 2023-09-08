class Handphone:
    # Constructor
    def __init__(self):
        self.panjang = 0
        self.lebar = 100
        self.berat = 0

    def getPanjang(self):
        return "HP : " + str(self.panjang)

    # Destructor
    # def __del__(self):
    #     print("Destructor")

class Xioami(Handphone):
    def __init__(self):
        super().__init__()
        # Overriding
        self.lebar = 50
        self.varA = "Isi"

    # Override Function
    def getPanjang(self):
        # ambil value get panjang dari parend class
        return super().getPanjang()
        # return "Xioami : " + str(self.panjang)

# hp = Handphone()
# print(hp.getPanjang())

xioami = Xioami()
print(xioami.getPanjang())