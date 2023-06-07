print(      "| Kode  |       Menu           | Harga Per Tiket|")
pilihan = ( "|1. D-F | Dunia Fantasi        | 220000         |", 
            "|2. J-L | Jungle Land          | 120000         |",
            "|3. T-S | Trans Studio         | 150000         |",
            "|4. D-P | Dago Dream Park      | 35000          |",
            "|5. S-W | Sea World            | 125000         |")
y = "Y"
total_tiket = 0
total_pembelian = 0

while y == "Y":
    for x in pilihan:
        print(x)

    kode = input("Masukan kode destinasi (Contoh : 01J-L): ")
    print("===============================================")

    #Parsing jumlah beli dan tujuan wisata
    jumlah_beli = int(kode[:2])
    tujuan_wisata = kode[2:5]


    if tujuan_wisata == "D-F":
        harga_tiket = 220000
    elif tujuan_wisata  == "J-L" :
        harga_tiket = 120000
    elif tujuan_wisata ==  "T-S":
        harga_tiket = 150000
    elif tujuan_wisata ==  "D-P":
        harga_tiket = 350000
    elif tujuan_wisata ==  "S-W":
        harga_tiket = 125000
    else :
        print("Tidak ada tiket tersebut ")

    total_pembelian = total_pembelian + (harga_tiket * jumlah_beli)
    total_tiket = total_tiket + jumlah_beli
    y = input("Apakah anda ingin membeli tiket lagi? (Y/N)")

print("==========================================")
print("Total Tiket yang dibeli : ",total_tiket)
print("==========================================")
print("Total Pembelian : Rp. ",total_pembelian)
print("==========================================")
