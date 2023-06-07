stok_barang = [1,2,3,4,5,6,7]
print(f"Data Sekarang {stok_barang}")

# insert new data
stok_barang.append(8)
print(f"Data entry : {8}")
print(f"Data Sekarang : {stok_barang}")
stok_barang.append(9)
print(f"Data entry : {9}")
print(f"Data Sekarang : {stok_barang}")

out = stok_barang.pop()
print(f"Data keluar {out }")
print(f"Data Sekarang : {stok_barang}")

kosong = stok_barang.clear()
print(f"Data Sekarang {kosong}")

