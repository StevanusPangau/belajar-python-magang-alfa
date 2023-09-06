"""Try Except Block
Try-Except Blocks: Ini adalah cara paling umum untuk menangani kesalahan di Python. 
Anda dapat mencoba menjalankan potongan kode yang mungkin menyebabkan kesalahan dalam blok try, 
dan jika ada kesalahan, Anda dapat menangkapnya dan menjalankan kode alternatif dalam blok except.
"""


try:
    hasil = 10/0
except ZeroDivisionError as e:
    print(f"Terjadi kesalahan {e}")
