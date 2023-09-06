"""Raise
Raise: Anda dapat menggunakan pernyataan raise untuk menghasilkan kesalahan atau pengecualian secara manual. 
Ini memungkinkan Anda untuk mengendalikan aliran program dan mengirim pesan kesalahan yang disesuaikan. 
"""


def bagi(a, b):
    if b == 0:
        raise ZeroDivisionError("Pembagian oleh nol tidak di izinkan")
    return a/b


print(bagi(10, 0))
