total_barang = 0
opsi = 'Ya'
total_harga = 0

while opsi == "Ya":
    total_barang = total_barang + 1
    opsi = input("Apakah akan melanjutkan ? (Ya/Tidak)")
    total_harga = total_harga + 1500

print("Total Barang : ", total_barang)
print("Jumlah harga Rp. ",total_harga)


