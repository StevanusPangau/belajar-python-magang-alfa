# Deklarasi
a = {}
b = {2: 'Sea', 5: 'River', 9: 'Mountain'}
c = {2: {4: 'abcd', 5: 'qwerty'}, 5: 'asdf'}
d = dict(name='elena', age=30, roles=('manager', 'consultant'))

# Print dict
print("----print dict")
print(a)
print(b)
print(c)
print(d)
print(b[2])
print(d['name'])

# keys value
print("\n----keys value")
print(b.keys())
print(b.values())
print(b.items())

# add items
print("\n----add item")
a.setdefault(1, 'Honda')
a.setdefault(2, 'Bmw')
a.setdefault(3, 'Supra')
a[4] = 'mobil baru'
newMobil = {5: 'hyundai', 6: 'alpart'}
a.update(newMobil)
print(a)

# del data
print("\n----del data")
del a[3]
hapusMobil = a.pop(1)
print(hapusMobil)
print(a)

# check key (cek jika ada key di dalam dict tersebut)
print("\n----check item")
print(3 in b)
print(5 in b)

# Print for dict
print("\n----print for dict")
# cara 1
for key, value in b.items():
    print(key, ":", value)

# cara 2
for key in b.keys():
    print(key, ":", b[key])
