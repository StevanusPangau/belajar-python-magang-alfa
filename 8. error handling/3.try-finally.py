"""Try Finally Block
Try-Finally Blocks: Blok try-finally digunakan untuk memastikan bahwa kode dalam blok finally selalu dijalankan, 
bahkan jika ada kesalahan dalam blok try. 
Ini digunakan terutama untuk membersihkan sumber daya atau mengambil tindakan pembersihan.
"""

try:
    f = open('file.txt', 'r')
    print(f.read())
    # Lakukan operasi pada berkas
finally:
    f.close()  # Pastikan berkas ditutup, bahkan jika terjadi kesalahan
