class Kendaraan:
    def __init__(self, jenisKendaraan):
        self.jenisKendaraan = str(jenisKendaraan)

class RodaDua(Kendaraan):
    def __init__(self, jenisKendaraan):
        super().__init__(jenisKendaraan)

class RodaEmpat(Kendaraan):
    def __init__(self, jenisKendaraan):
        super().__init__(jenisKendaraan)

kendaraanRodaDua = RodaDua('Honda')
print(kendaraanRodaDua.jenisKendaraan)

kendaraanRodaEmpat = RodaEmpat('Toyota')
print(kendaraanRodaEmpat.jenisKendaraan)