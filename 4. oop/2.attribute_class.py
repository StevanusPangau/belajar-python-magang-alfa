class City:
    # class data
    def tambah(self, angka1, angka2):
        return angka1 + angka2

    def kurang(self, angka1, angka2):
        return angka1 - angka2


result = City()

print(result.tambah(10, 10))
print(result.kurang(12, 5))
