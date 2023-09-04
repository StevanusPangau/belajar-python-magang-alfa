# Deklrarasi List
numbers = []
a = [5, 4, 2, 8, 3]
cities = ['Manado', 'Jakarta', 'Tangerang', 'Solo']
b = [2, 3, 'Semarang', 6, 'Jakarta']
c = range(1, 10, 2)

# Print Lists
print('----print(lists)')
print(a)
for city in cities:
    print(city)
print(b)
print(c)

# Melihat panjang list
print("\n----get lenght of list")
print(len(a))
print(len(cities))

# Tambah item di list
print("\n----add item")
numbers.append(9)
numbers.append(5)
cities.append("Lombok")

for i in numbers:
    print(i)

for city in cities:
    print(city)

# Cari item spesifik di list
print("\n----get item")
print(numbers[1])
print(cities[3])
print(a[0])

# Urutkan list
print("\n----sort list")
a.sort()
print(a)

# Edit item list
print("\n----edit item")
cities[3] = "new city"
for city in cities:
    print(city)

# Hapus item
print("\n----remove item")
a.remove(5)  # Hapus berdasarkna value
print(a)
del cities[3]  # Hapus berdasarkan index
for city in cities:
    print(city)
