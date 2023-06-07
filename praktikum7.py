akhir = int(input("Tuliskan angka akhir :"))
jumlah = 0
x = 1

while x <= akhir :
    if x % 2 == 1:
        jumlah = jumlah + x
    x = x + 1

print("Jumlah deret : ",jumlah)