saldo = 100000
jenis_jasa = input("Masukan jenis jasa  : ")
jarak = int(input("Masukan jarak (dalam km): "))
jenis_pembayaran = str(input("jenis Pembayaran : "))
diskon = 0.15

if (jenis_jasa == "Perjalanan"):
    harga_per_km = 2000
elif (jenis_jasa == "Antar makanan"):
    harga_per_km = 3000
elif j(jenis_jasa == "Antar barang"):
    harga_per_km = 2500
else:
    print("Jasa tidak tersedia")
harga = int(harga_per_km * jarak)
print("Harga", harga)


if (jenis_pembayaran == "saldo"):
    diskon = harga * 0.15
elif (jenis_pembayaran == "cash"):
    diskon = 0
else: 
    print("jenis pembayaran tidak tersedia")

harga_akhir = int(harga - diskon)
print("Harga: ",harga_akhir)


print("Total Bayar : ",harga_akhir)
print("Total Diskon ",diskon)
print("Sisa Saldo : ",saldo - harga_akhir)




