list_kata = ['alfamart', {'a': [3, 8], 'b': 2023}, ('training', 'pada', {
                                                    'c': 'kelompok', 'd': 'pelatihan'}, 'membuat'), 'soal', 'peserta', ('tanggal', 'lain', 'menjadi'), {'e': 'dibagi'}]


def funcFromKel2(paramList):
    list_ = []

    for item in paramList:
        if (type(item) == dict):
            for d in item.values():
                if (type(d) == list):
                    for i in d:
                        list_.append(i)
                else:
                    list_.append(d)
        elif (type(item) == tuple):
            for i in item:
                if (type(i) == dict):
                    for d in i.values():
                        list_.append(d)
                else:
                    list_.append(i)
        else:
            list_.append(item)
    return list_


listUtama = funcFromKel2(list_kata)
print(list_kata, "\n")
print(listUtama, "\n")

# Soal a : Pada hari ke 3 pelatihan peserta dibagi menjadi 8 kelompok.
stringA = f"{listUtama[5].capitalize()} hari ke {listUtama[1]} {listUtama[7]} {listUtama[10]} {listUtama[14]} {listUtama[13]} {listUtama[2] } {listUtama[6]}."
print("=====Output Soal A=====")
print(stringA)

# Soal b : Kelompok 3 membuat soal ini untuk peserta lain di training Alfamart pada tanggal 8 September 2023.
stringB = f"{listUtama[6].capitalize()} {listUtama[1]} {listUtama[8]} {listUtama[9]} ini untuk {listUtama[10]} {listUtama[12]} di {listUtama[4]} {listUtama[0].capitalize()} {listUtama[5]} {listUtama[11]} {listUtama[2]} september {listUtama[3]}."
print("\n=====Output Soal B=====")
print(stringB)
