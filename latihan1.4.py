pilihan = ( "|1. D-F | Dunia Fantasi   | 220000  |", 
            "|2. J-L | Jungle Land     | 120000  |",
            "|3. T-S | Trans Studio    | 150000  |",
            "|4. D-P | Dago Dream Park | 35000   |",
            "|5. S-W | Sea World       | 125000  |")
y = "Y"
total_tiket = 0
total_pembelian = 0

while y == "Y":
    for x in pilihan:
        print(x)
    menu = int(input("Silahkan pilih menu diatas : "))
    tiket = int(input("Total tiket yang ingin dibeli? :  "))

    if menu == 1:
        kode = "D-F"
        harga_tiket = 220000
    elif menu == 2 :
        kode = "J-L"
        harga_tiket = 120000
    elif menu == 3 :
        kode = "J-L"
        harga_tiket = 150000
    elif menu == 4 :
        kode = "J-L"
        harga_tiket = 350000
    elif menu == 5 :
        kode = "J-L"
        harga_tiket = 125000
    else :
        print("Tidak ada tiket tersebut ")
#     harga_tiket = 220000 if menu == 1 else 120000 if menu == 2 else 150000 if menu == 3 else 35000 if menu == 4 else 125000
    total_pembelian = total_pembelian + (harga_tiket * tiket)
    total_tiket = total_tiket + tiket
    y = input("Apakah anda ingin membeli tiket lagi? (Y/N)")
print(f"Total Tiket yang dibeli : ",total_tiket)
print(f"Total Pembelian : Rp. ",total_pembelian)
