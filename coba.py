kode = input("Masukkan kode pembelian: ")

# mengambil informasi jumlah beli dari kode pembelian
jumlah_beli = int(kode[:2])

# mengambil informasi tujuan wisata dari kode pembelian
tujuan = tujuan_wisata[kode[2:5]]["nama"]

# mengambil informasi harga per tiket dari kode pembelian
harga_tiket = tujuan_wisata[kode[2:5]]["harga"]