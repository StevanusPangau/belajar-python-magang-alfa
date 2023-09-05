class Kendaraan:
    def info(self):
        return "Ini adalah kendaraan umum."


class Mobil(Kendaraan):
    def info(self):
        return "Ini adalah mobil."


class Sepeda(Kendaraan):
    pass


mobil = Mobil()
sepeda = Sepeda()

print(mobil.info())  # Output: Ini adalah mobil.
print(sepeda.info())  # Output: Ini adalah kendaraan umum.

"""Overriding

bisa dikatakan untuk overriding adalah subclass yang bisa mengubah perilaku dari methode yang diwariskan oleh superclass atau parent
seperti contoh di atas yang dimana var mobil melakukan overriding sedangkan class sepeda tidak
"""
