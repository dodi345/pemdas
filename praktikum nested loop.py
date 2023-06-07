# praktikum 1
print("PRAKTIKUM 1")
print('FOR LOOP ')
daftar_nilai = ['sepatu', 'baru',60, 80, 55, 40]
for nilai in daftar_nilai:
      print('Nilai : ',nilai)

print("PRAKTIKUM 1")
print('FOR LOOP ')
daftar_nilai = ['sepatu', 'baru',60, 80, 55, 40]
for nilai in daftar_nilai:
    print('Nilai : ',nilai)
    print(type(daftar_nilai))
    data_baru = str(daftar_nilai)
    print(data_baru)
    print(type(data_baru))


# praktikum  2
print("PRAKTIKUM 2")
print('for loop dan range')
daftar_nilai = [60,80,55,40]
panjang = len(daftar_nilai)
for i in range(panjang):
    print('Nilai : ',daftar_nilai)

# print("PRAKTIKUM 2")
print('for loop dan range')
daftar_nilai = [60,80,55,40]
panjang = len(daftar_nilai)
for i in range(2):
    print('Nilai : ',daftar_nilai)


# praktikum 3
print("PRAKTIKUM 3")
print('WHILE')
daftar_nilai = [60,80,55,40]
panjang = len(daftar_nilai)
i = 0
while i < panjang:
    print('Nilai : ',daftar_nilai[i])
    i += 1
    

# print("PRAKTIKUM 3")
print('WHILE')
daftar_nilai = [60,80,55,40]
panjang = len(daftar_nilai)
i = 2
while i < panjang:
    print('Nilai : ',daftar_nilai[i])
    i += 1

# praktikum 4
print("PRAKTIKUM 4")
print('LIST COMPREHENSION')
daftar_nilai = [60,80,55,40]
[print('Nilai : ',i) for i in daftar_nilai]

# praktikum 5
print("PRAKTIKUM 5")
print('ENUMERATE')
daftar_nilai = [60,80,55,40]
for index , nilai in  enumerate(daftar_nilai):
    print('Index : ',index, 'Nilai : ',nilai)

# praktikum 6
print("PRAKTIKUM 6")
nama = input('Masukan Nama \t: ')
nim = input('Masukan NIM \t: ')
data_mahasiswa = [nama, nim]
print(data_mahasiswa)

# praktikum 7
daftar_mahasiswa = []
while True:
    nama = str(input('Masukan Nama \t: '))
    nim = int(input('Masukan NIM \t: '))
    data_mahasiswa = [nama, nim]
    daftar_mahasiswa.append(data_mahasiswa)
    print(daftar_mahasiswa)

    for index , mhs in enumerate(daftar_mahasiswa):
        print("|", index+1, "|",mhs[0], "\t\t|",mhs[1],"|")
    tambah = input("\nApakah ingin tambah data ? (Y/N) ") 

    if tambah == 'N' :
        break  

# prakrikum 7
daftar_mahasiswa = []
while True:
    nama = str(input('Masukan Nama \t: '))
    nim = int(input('Masukan NIM \t: '))
    alamat = str(input('Masukan Alamat \t: '))
    hobi = str(input('Hobi Kamu Apa \t: '))
    cita_cita = str(input('Kenapa kamu bilang begitu, siapa yang nyuruh \t: '))
    data_mahasiswa = [nama, nim, alamat, hobi, cita_cita]
    daftar_mahasiswa.append(data_mahasiswa)
    print(daftar_mahasiswa)

    for index , mhs in enumerate(daftar_mahasiswa):
        print("|", index+1, "|",mhs[0], "\t\t|",mhs[1], "|",mhs[2], "|",mhs[3], "|",mhs[4])
    tambah = input("\nApakah ingin tambah data ? (Y/N) ") 

    if tambah == 'N' :
        break  