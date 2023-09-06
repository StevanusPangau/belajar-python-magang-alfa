"""
Anda dapat membuat pengecualian kustom (custom exception) dalam Python dengan cara yang relatif mudah. Anda perlu membuat sebuah kelas yang merupakan subkelas dari Exception atau salah satu pengecualian yang ada, dan Anda bisa menambahkan perilaku atau pesan kustom sesuai kebutuhan Anda
"""


class MyCustomException(Exception):
    def __init__(self, message="Ini adalah pengecualian kustom"):
        self.message = message
        super().__init__(self.message)

# Contoh penggunaan pengecualian kustom


def fungsi_berisiko(nilai):
    if nilai < 0:
        raise MyCustomException("Nilai tidak boleh negatif")


try:
    fungsi_berisiko(-5)
except MyCustomException as e:
    print(f"Terjadi pengecualian kustom: {e}")
