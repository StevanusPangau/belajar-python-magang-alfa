def contoh_fungsi():
    nilai1 = 10
    nilai2 = 20
    nilai3 = 30
    return nilai1, nilai2, nilai3


# Memanggil fungsi
hasil = contoh_fungsi()

# Mencetak hasil yang dikembalikan
print(hasil)  # Output: (10, 20, 30)

# Memecah tupel hasil menjadi variabel-variabel terpisah
nilai_a, nilai_b, nilai_c = hasil
print(nilai_a)  # Output: 10
print(nilai_b)  # Output: 20
print(nilai_c)  # Output: 30


def perform(num):
    d = num * 5
    return d, d + 5, d - 2


print(perform(5))
