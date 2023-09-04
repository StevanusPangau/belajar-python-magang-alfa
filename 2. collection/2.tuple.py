# Deklarasi tuple
a = ()
b = (3, 7, 9)
c = ('Ford', 'Bmw', 'Honda')
d = (3, (5, 'London'), 12)

# Print Tuple
print("----print tuple")
print(a)
print(b)
print(c)
print(d)

for i in c:
    print(i)

# Panjang tuple
print("\n----len tuple")
print(len(a))
print(len(b))
print(len(c))
print(len(d))

# Get item
print("\n----ambil data value berdasarkan index")
print(b[2])
print(c[1])
print(d[1][1])

# Get index
print("\n----ambil data index berdasarkan value")
print(b.index(7))
print(c.index('Honda'))

# Mengabungkan tuple
print("\n----mengabungkan tuple")
tuple1 = (1, 2, 3)
tuple2 = (4, 5)

new_tuple = tuple1 + tuple2  # Membuat tuple baru dengan elemen tambahan
print(new_tuple)  # Output: (1, 2, 3, 4, 5)
