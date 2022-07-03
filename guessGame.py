# 1 - 100
# Suruh user nebak, lalu kasihtau sama apa nggak
# Kasih tau dia bener atau salah tebakannya

# 1 - 100
# Let user guess , then let user know is it correct or no
# Tell user right or wrong 

from ast import If
import random as rn

# Set Variable for looping
mulai = True
# Set variable to determine how much the try limit , let say 5
i = 5

# Generate random number from 1 - 100
angka = rn.randint(1, 100)

# The game started
while mulai == True:

    # Get user input for guessing
    tebak = int(input('Pilih Angka : '))

    # Some Validation
    if tebak == angka:
        print('Horray! Tebakan mu benar, angkanya adalah ' + str(angka)) # Will print out if the guess is Correct
        mulai = False # Change the start variable for looping to False to make it wont loop again
    elif tebak > int(angka):
        print('Terlalu tinggi. Coba lagi') # When the guess is too high from the correct number
        i -= 1 # To decrease 'lifes' or try to guess
    elif tebak < int(angka):
        print('Terlalu rendah. Coba lagi') # When the guess is too low from the correct number
        i -= 1 # To decrease 'lifes' or try to guess
        
    if i == 0: #If the limit is run out, this will printout
        print('Kesempatan mencoba sudah habis') # Tell no more try to guess
        print('Jawaban Yang benar adalah = ' + str(angka)) # Tell the correct answer
