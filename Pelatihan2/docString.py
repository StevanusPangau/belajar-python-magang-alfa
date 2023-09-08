"""contoh modul
contoh modul adalah class untuk menyelesaikan suatu perhitungan
"""


class Aritmatika:
    """
    class aritmatika adalah class perhitungan
    """

    def tambah(angka1, angka2):
        """
        Fungsi tambah adalah fungsi untuk menjumlahkan 2 angka
        param angka1: angka pertama yang akan dijumlahkan
        type angka1: int
        param angka2: angka kedua yang akan dijumlahkan
        type angka2: int
        return: hasil penjumlahan angka1 dan angka2
        return type: int
        """

        hasil = angka1 + angka2
        return hasil

    def kurang(angka1, angka2):
        """
        Fungsi kurang adalah fungsi untuk mengurangi 2 angka
        param angka1: angka pertama yang akan dikurangi
        type angka1: int
        param angka2: angka kedua yang akan dikurangi
        type angka2: int
        return: hasil pengurangan angka1 dan angka2
        return type: int
        """

        hasil = angka1 - angka2
        return hasil
