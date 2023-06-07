nama = input("Masukan Nama : ")
nim = int(input("Masukan nim : "))
nilai = input("Masukan nilai ujian :")
nilai = int(nilai)

if nilai > 70:
    hasil_ujian = "LULUS"
else :
    hasil_ujian = "TIDAK LULUS"

print ("Nama : ",nama)
print("NIM : ",nim)
print("==========================")
print("Hasil Ujian : ",hasil_ujian)
