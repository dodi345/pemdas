
saldo = 100000

def pilihan_jasa(jenis_jasa, jarak):
    harga_per_km = 0
    if jenis_jasa == "Perjalanan":
        harga_per_km = 2000
    elif jenis_jasa == "Antar makanan":
        harga_per_km = 3000
    elif jenis_jasa == "Antar barang":
        harga_per_km = 2500
    else:
        return "Jenis jasa tidak dikenal"

    harga = jarak * harga_per_km
    return harga

def pembayaran(jenis_pembayaran, harga):
    diskon = 0
    if jenis_pembayaran == "saldo":
        diskon = harga * 0.15
    elif jenis_pembayaran == "cash":
        diskon = 0
    else:
        return "Jenis pembayaran tidak dikenal"

    harga_akhir = harga - diskon
    return harga_akhir

jenis_jasa = input("Masukkan jenis jasa (Perjalanan, Antar makanan, Antar barang): ")
jarak = int(input("Masukkan jarak (dalam km): "))
harga = pilihan_jasa(jenis_jasa, jarak)

if type(harga) == str:
    print(harga)
else:
    print("Harga:", harga)

    jenis_pembayaran = input("Masukkan jenis pembayaran (saldo, cash): ")
    harga_akhir = pembayaran(jenis_pembayaran, harga)

    if type(harga_akhir) == str:
        print(harga_akhir)
    else:
        print("Harga setelah diskon:", harga_akhir)
        print("Saldo akhir:", saldo - harga_akhir)