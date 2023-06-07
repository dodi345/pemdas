harga_barang = 1500
total_harga = 0

while True:
    qty = int(input("Masukan jumlah barang yang akan dibeli: "))
    total_harga += harga_barang * qty
    print("Harga beli sekarang Rp. ", total_harga)

    ulang = input("Apakah ingin melanjutkan transaksi? (Ya/Tidak) ")
    if ulang == "Tidak" or ulang == "tidak":
        break

print("Total harga adalah Rp. ", total_harga)
