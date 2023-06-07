list1 = [123, 124, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 136, 137]
print("List awal : ",list1)

n = int(input("Masukan jumlah angka yang ingin anda tambahkan (skala 5-10 ya ges ya) :"))
for i in range(n):
    angka = int(input(f"Masukan angka ke-{i+1} (skala 1-50 ya ges ya) : "))
    list1.append(angka)

print("Semua isi list : ",list1)

elemen = int(input("Pilih satu elemen yang hendak dihitung : "))
jumlah = list1.count(elemen)
print("jumlah elemen : ",jumlah)

list1.sort()
angka_terkecil = list1[:5]
print("5 angka terkecil adalah : ",angka_terkecil)

angka_terbesar  = list1[-5:]
print("5 Angka terbesar adalah : ",angka_terbesar)

print("Gabungan keduanya : ",angka_terkecil  + angka_terbesar)