import os

def header():
    os.system("clear")
    print(f"{'MENGHITUNG LUAS PERSEGI SEDERHANA':^40}")
    print(f"{'PROGRAM INI DIBUAT UNTUK DIBUAT':^40}")
    print(f"{'='*40:^40}")

def input_user():
    lebar = int(input("Masukan nilai anda : "))
    panjang = int(input("Masukan Nilai disini : "))

    return lebar,panjang

def hitung_luas(lebar, panjang):
    return lebar*panjang

def hitung_keliling(lebar, panjang):
    return 2*(lebar+panjang)


while True:
    header()
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    print(f"Hasil dari ini adalah : {LUAS}")
    print(f"Hasil ini juga adalah : {KELILING}")
    
    isContinue = input("Apakah mau lanjut (y/n) ? ")
    if isContinue == "n":
        break 

print("Program sederhana telah selesai!!!!")