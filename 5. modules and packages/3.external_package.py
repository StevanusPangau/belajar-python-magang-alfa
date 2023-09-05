"""External Package

external package kita gunakan saat membutuhkan package dari luar python yang dibuat oleh orang lain
untuk menginstal package dari luar kita perlu menggunakan perinah pip
contoh : pip3 install 'nama package'
"""

import colorama
from colorama import Fore, Back, Style

colorama.init
message = "Hello world from python"
print(message)
print(Fore.RED + message)
print(Fore.GREEN + message)
print(Fore.BLUE + message)
print(Fore.RED + Back.YELLOW + message + Style.RESET_ALL)
