# Soal 1
# test_list = ['D', 'C', {'a': 'A', 'i': 'I'}, ('B', 'E', ['G', 'F']), 'H']
# new_list = []

# for data in test_list:
#     if isinstance(data, (tuple)):
#         new_list.append(list(data))
#     elif isinstance(data, (dict)):
#         new_list.append(list(data.values()))
#     else:
#         new_list.append(data)

# print(new_list)


# def ubahList(lst):
#     result = []
#     for item in lst:
#         if isinstance(item, list):
#             result.extend(ubahList(item))
#         else:
#             result.append(item)
#     return result


# result = ubahList(new_list)
# result.sort()

# print(result)


# >>>> Soal 2
alfamart = "ALFAMART PT. SUMBER ALFARIA TRIJAYA"
listPerson = ['adi', 'ali', 'abi']
dictKelas = {'a': 'tangerang', 'b': 'alam sutera'}
# Dari kumpulan data di atas, susunlah menjadi string berikut:
# a. Ali sedang magang di PT Sumber Alfaria Trijaya
# b. Head office Alfamart terletak di Alam Sutera

# Soal 3
testString = "This is a test. This test is a good test."
# Hitunglah banyaknya kata yang keluar, lalu ubah menjadi bentuk dictionary seperti berikut:
# {
#     "this": 2,
#     "is": 2,
#     "a": 2,
#     "test": 3,
#     "good": 1
# }


# Soal 4
# Dari list di atas, buatlah list - list baru dengan ketentuan sebagai berikut
# a. List 'pangkat_dua' yang berisi hasil perpangkatan 2
# b. List dengan nilai lebih dari sama dengan 10
# c. List bilangan genap

# numbers = [3, 8, 12, 6, 15, 20, 17, 5, 10]
# new_list1 = []
# new_list2 = []
# new_list3 = []

# for i in numbers:
#     new_list1.append(i ** 2)
#     if i >= 10:
#         new_list2.append(i)
#     if i % 2 == 0:
#         new_list3.append(i)

# print(new_list1)
# print(new_list2)
# print(new_list3)


# Soal 6
names = ["Bob", "David", "Charlie", "Eve", "Alice", "Alfamart"]
# a. Urutkan berdasarkan abjad (a-z)
# b. Urutkan dari kata yang paling hingga paling pendek

names.sort()
print(names)

names.sort(key=len, reverse=True)
print(names)

# Soal 10
# a. Hitung rata-rata nilai dari setiap murid, contoh output:
#    Alice's average grade: 87
#    ...
# b. Buat list murid yang naik kelas (rata-rata > 70)

student_data = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 78, 95]},
    {"name": "Bob", "age": 21, "grades": [70, 65, 80, 72]},
    {"name": "Charlie", "age": 19, "grades": [45, 55, 60, 50]},
    {"name": "David", "age": 22, "grades": [80, 82, 85, 78]},
    {"name": "Eve", "age": 20, "grades": [92, 88, 78, 95]},
]

naik_kelas = []
for data in student_data:
    if 'grades' in data:
        total_nilai = sum(data['grades'])
    name = data['name']
    avg_grade = total_nilai/len(data['grades'])
    print(f"{name} average grade : {avg_grade}")

    if avg_grade > 70:
        naik_kelas.append(name)

print("\nSiswa yang naik kelas : ")
for siswa in naik_kelas:
    print(siswa)
