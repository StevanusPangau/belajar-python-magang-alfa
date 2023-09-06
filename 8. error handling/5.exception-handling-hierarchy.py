"""
Exception Handling Hierarchy (Hirarki Penanganan Pengecualian) adalah konsep di mana Anda dapat menangani berbagai jenis pengecualian dengan cara yang terstruktur dan sesuai dengan tingkat kerumitan penanganan kesalahan. Ini memungkinkan Anda untuk menangani kesalahan berdasarkan tipe pengecualian yang lebih spesifik terlebih dahulu, dan jika tidak ada yang cocok, Anda dapat menangani pengecualian yang lebih umum.

Berikut adalah penjelasan lebih rinci tentang Exception Handling Hierarchy:

Base Exception:

Ini adalah kelas dasar untuk semua pengecualian dalam Python.
Semua pengecualian dalam Python adalah subkelas dari BaseException.
Ini adalah pengecualian yang paling umum dan akan menangani semua jenis pengecualian jika tidak ada penanganan yang lebih spesifik.
Exception:

Exception adalah kelas yang lebih umum daripada BaseException.
Semua pengecualian bawaan Python yang umum, seperti ZeroDivisionError, ValueError, TypeError, dan banyak lainnya, adalah subkelas dari Exception.
Biasanya, Anda akan menangani pengecualian dalam blok except Exception: jika Anda ingin menangani semua jenis pengecualian yang terkait dengan kode Anda.
Specific Exceptions:

Di bawah kelas Exception, Anda akan menemukan berbagai pengecualian yang lebih spesifik.
Contoh pengecualian yang lebih spesifik meliputi ZeroDivisionError, ValueError, TypeError, FileNotFoundError, dan banyak lainnya.
Anda dapat menangani pengecualian ini secara terpisah berdasarkan jenisnya untuk menangani kesalahan dengan cara yang sesuai.
Custom Exceptions:

Selain pengecualian bawaan, Anda juga dapat membuat pengecualian kustom (custom exceptions) dengan membuat kelas pengecualian sendiri yang merupakan subkelas dari Exception.
Ini memungkinkan Anda untuk membuat pengecualian yang sesuai dengan kebutuhan aplikasi Anda.
"""

try:
    # Kode yang mungkin menghasilkan kesalahan
    angka = int("abc")
except ZeroDivisionError:
    # Penanganan khusus untuk ZeroDivisionError
    print("Tidak dapat membagi oleh nol")
except ValueError:
    # Penanganan khusus untuk ValueError
    print("Terjadi kesalahan nilai")
except Exception as e:
    # Penanganan kesalahan umum
    print(f"Terjadi kesalahan: {e}")
