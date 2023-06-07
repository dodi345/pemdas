# mendefinisikan dictionary untuk menyimpan data barang
data_barang = {
    "B001": {"nama": "Pensil", "harga": 500, "stok": 50},
    "B002": {"nama": "Buku", "harga": 10000, "stok": 20},
    "B003": {"nama": "Penghapus", "harga": 1000, "stok": 30},
    "B004": {"nama": "Penggaris", "harga": 2000, "stok": 40},
    "B005": {"nama": "Bolpoin", "harga": 2000, "stok": 35}
}

# mendefinisikan fungsi untuk mencetak data barang
def cetak_data_barang():
    print("Data Barang:")
    print("Kode\tNama\t\tHarga\tStok")
    for kode, data in data_barang.items():
        print(kode, "\t", data["nama"], "\t\t", data["harga"], "\t", data["stok"])

# mendefinisikan fungsi untuk membeli barang
def beli_barang():
    kode = input("Masukkan kode barang: ")
    if kode in data_barang:
        jumlah = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        if jumlah > data_barang[kode]["stok"]:
            print("Stok barang tidak cukup!")
        else:
            total_harga = jumlah * data_barang[kode]["harga"]
            data_barang[kode]["stok"] -= jumlah
            print("Barang", data_barang[kode]["nama"], "sebanyak", jumlah, "buah telah dibeli.")
            print("Total harga yang harus dibayar adalah Rp", total_harga)
    else:
        print("Barang dengan kode", kode, "tidak ditemukan!")

# mendefinisikan fungsi untuk menjual barang
def jual_barang():
    kode = input("Masukkan kode barang: ")
    if kode in data_barang:
        jumlah = int(input("Masukkan jumlah barang yang ingin dijual: "))
        data_barang[kode]["stok"] += jumlah
        print("Barang", data_barang[kode]["nama"], "sebanyak", jumlah, "buah telah dijual.")
    else:
        print("Barang dengan kode", kode, "tidak ditemukan!")

# mendefinisikan program utama
while True:
    print("\n=== Aplikasi Toko ===")
    print("1. Cetak Data Barang")
    print("2. Beli Barang")
    print("3. Jual Barang")
    print("4. Keluar")
    pilihan = input("Masukkan pilihan: ")
    if pilihan == "1":
        cetak_data_barang()
    elif pilihan == "2":
        beli_barang()
    elif pilihan == "3":
        jual_barang()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan aplikasi toko!")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
