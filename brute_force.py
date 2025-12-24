import itertools
import string

password_asli = "abc"

chars = string.ascii_lowercase

for panjang in range (1, 4):
    for percobaan in itertools.product(chars, repeat=panjang):
        tebakan = "".join(percobaan)
        print("Mencoba:", tebakan)
        if tebakan == password_asli:
            print("Password ditemukan:", tebakan)
            exit()