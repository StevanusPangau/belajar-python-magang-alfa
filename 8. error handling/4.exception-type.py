"""Exception Type
Exception Types: Python memiliki banyak jenis pengecualian yang mewakili berbagai jenis kesalahan. 
Anda dapat menangani jenis pengecualian tertentu atau mengambil tindakan berbeda berdasarkan jenis kesalahan yang terjadi. 
Misalnya, ValueError, TypeError, FileNotFoundError, dll.

try:
    # Kode yang mungkin menghasilkan kesalahan
except ValueError:
    # Tangani kesalahan tipe ValueError
except TypeError:
    # Tangani kesalahan tipe TypeError
"""

try:
    hasil = 10 / 0  # Zero Division Error

    angka = int("abc")  # Value error

    hasil = "10" + 5  # Type error

    file = open("berkas_tidak_ada.txt", "r")  # File note founder error

    my_list = [1, 2, 3]
    item = my_list[5]  # Index error

    my_dict = {"nama": "John", "usia": 30}
    nilai = my_dict["alamat"]  # Key error
except ZeroDivisionError as e:
    # Ini terjadi ketika Anda mencoba membagi oleh nol.
    print(f"Terjadi kesalahan: {e}")
except ValueError as e:
    # Ini terjadi ketika Anda mencoba mengkonversi nilai yang tidak valid ke tipe data tertentu, seperti mengubah string yang tidak dapat diubah menjadi integer.
    print(f"Terjadi kesalahan: {e}")
except TypeError as e:
    # Ini terjadi ketika Anda melakukan operasi yang tidak sesuai dengan jenis data yang diharapkan, seperti mencoba menggabungkan tipe data yang tidak cocok.
    print(f"Terjadi kesalahan: {e}")
except FileNotFoundError as e:
    # Ini terjadi ketika Anda mencoba membuka berkas yang tidak ada.
    print(f"Terjadi kesalahan: {e}")
except IndexError as e:
    # Ini terjadi ketika Anda mencoba mengakses indeks di luar jangkauan dalam list atau tuple.
    print(f"Terjadi kesalahan: {e}")
except KeyError as e:
    # Ini terjadi ketika Anda mencoba mengakses kunci yang tidak ada dalam kamus (dictionary).
    print(f"Terjadi kesalahan: {e}")

"""
Ini hanyalah beberapa contoh pengecualian yang lebih spesifik yang sering digunakan dalam Python. 
Setiap pengecualian memiliki situasi di mana mereka akan terjadi, dan Anda dapat menangani masing-masing sesuai kebutuhan aplikasi Anda.
"""
