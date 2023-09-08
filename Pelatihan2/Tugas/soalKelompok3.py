list_kata = ['alfamart', {'a': [3, 8], 'b': 2023}, ('training', 'pada', {
                                                    'c': 'kelompok', 'd': 'pelatihan'}, 'membuat'), 'soal', 'peserta', ('tanggal', 'lain', 'menjadi'), {'e': 'dibagi'}]
# Soal a
# Pada hari ke 3 pelatihan peserta dibagi menjadi 8 kelompok.
# Soal b
# Kelompok 3 membuat soal ini untuk peserta lain di training Alfamart pada tanggal 8 September 2023.


def funcKel3(listKel3):
    varList = []
    result = []

    for data in listKel3:
        if isinstance(data, (tuple)):
            for i in data:
                if (type(i) == dict):
                    varList.append(list(i.values()))
                else:
                    varList.append(i)
        elif isinstance(data, (dict)):
            varList.append(list(data.values()))
        else:
            varList.append(data)

    for item in varList:
        if isinstance(item, list):
            result.extend(ubahList(item))
        else:
            result.append(item)

    return result

# Soal a
# Pada hari ke 3 pelatihan peserta dibagi menjadi 8 kelompok.
# Soal b
# Kelompok 3 membuat soal ini untuk peserta lain di training Alfamart pada tanggal 8 September 2023.


listUtama = funcKel3(list_kata)

print(listUtama)

# stringA = f"{listUtama[5].capitalize()} hari ke {listUtama[1]} {listUtama[7]} {listUtama[10]} {listUtama[14]} {listUtama[13]} {listUtama[2] } {listUtama[6]}."
# print("=====Output Soal A=====")
# print(stringA)

# print()

# # Soal b
# # Kelompok 3 membuat soal ini untuk peserta lain di training Alfamart pada tanggal 8 September 2023.
# stringB = f"{listUtama[6].capitalize()} {listUtama[1]} {listUtama[8]} {listUtama[9]} ini untuk {listUtama[10]} {listUtama[12]} di {listUtama[4]} {listUtama[0].capitalize()} {listUtama[5]} {listUtama[11]} {listUtama[2]} september {listUtama[3]}."
# print("=====Output Soal B=====")
# print(stringB)
