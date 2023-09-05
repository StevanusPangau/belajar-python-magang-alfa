import sys
###########################################
# Opening File
print("Operning file")

f1 = open('mydoc1', 'r')
f2 = open('mydoc2', 'r')
fb1 = open('mydoc3', 'rb')
fb2 = open('mydoc4', 'rb')

###########################################
# Reading File


def reading_data(f):
    while True:
        data = f.readline()
        if (data == '') or (data == None):
            break

        # Periksa apakah berkas adalah berkas teks atau biner
        if isinstance(data, str):
            sys.stdout.write(data)  # Jika berkas teks, tulis sebagai string
        elif isinstance(data, bytes):
            try:
                # Jika berkas biner, coba dekode dan tulis sebagai string
                sys.stdout.write(data.decode())
            except UnicodeDecodeError:
                # Jika dekode gagal, tulis sebagai byte
                sys.stdout.buffer.write(data)


print("from mydoc1>>>>>")
reading_data(f1)
print(">>>>>>>>>>>>>>>>")

print("\nfrom mydoc2>>>>>")
reading_data(f2)
print(">>>>>>>>>>>>>>>>")

print("\nfrom mydoc3>>>>>")
reading_data(fb1)
print(">>>>>>>>>>>>>>>>")

print("\nfrom mydoc4>>>>>")
reading_data(fb2)
print(">>>>>>>>>>>>>>>>")

###########################################
# Close all

print("close file...")
f1.close()
f2.close()
fb1.close()
fb2.close()
