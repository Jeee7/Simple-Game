# 1 - 100
# Suruh user nebak, lalu kasihtau sama apa nggak
# Kasih tau dia bener atau salah tebakannya

from ast import If
import random as rn

mulai = True

angka = rn.randint(1, 10)
while mulai == True:

    tebak = int(input('Pilih Angka : '))

    if tebak == angka:
        print('Horray! Tebakan mu benar, angkanya adalah ' + str(angka))
        mulai = False
    elif tebak > int(angka):
        print('Terlalu tinggi. Coba lagi')
    elif tebak < int(angka):
        print('Terlalu rendah. Coba lagi')
    else:
        print('Yahhh salah kack, tebakanmu ' + str(tebak),
              '  Yang benar adalah = ' + str(angka))
