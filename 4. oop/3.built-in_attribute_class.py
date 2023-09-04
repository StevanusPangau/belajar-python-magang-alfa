class Person:
    # Konstruktor
    def __init__(self, nama):
        self.nama = nama  # Menyimpan nama saat objek dibuat
        print(f"Selamat datang, {self.nama}!")

    # Destruktor
    def __del__(self):
        print(f"{self.nama} telah pergi.")


# Membuat objek Person
seseorang = Person("Evan")
