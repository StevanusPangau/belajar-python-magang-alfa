def suatufungsiA():
    angka1 = 1
    angka2 = 2
    hasilA = angka1 + angka2
    return hasilA


def suatufungsiB(angka1=0):
    angka2 = 2
    hasilB = angka1 + angka2
    return hasilB


def suatufungsiC(angka1, angka2):
    hasilC = angka1 + angka2
    return hasilC


def suatufungsiD(*args):
    hasilD = 0
    for i in args:
        print("hasilD temporary : ", hasilD)
        hasilD = hasilD + i
        print("hasilD temporary setelah ditambah angka berikutnya : ", hasilD)
    return hasilD


def suatufungsiE(**kwargs):
    print(kwargs["angka1"])
    print(kwargs["angka2"])
    print(kwargs["angka3"])

    for key, val in kwargs.items():
        print(key, " = ", val)


hasilA = suatufungsiA()
print("Tugas A : ", hasilA)

hasilB = suatufungsiB(1)
print("Tugas B : ", hasilB)

hasilC = suatufungsiC(5, 5)
print("Tugas C : ", hasilC)
