import string
import random
import os

os.system("clear")

kasus_indonesia = [
    {
        'kode' : ' 1A',
        'jenis' : 'KK',
        'nama' : 'Korupsi',
        'kerugian' : '120000000',
        'pelaku' : 'Juliari Batubara'
    },
    {
        'kode' : '2A',
        'jenis' : 'PL',
        'nama' : 'Jual Pulau',
        'kerugian' : '50000000',
        'pelaku' : 'Megamendung'
    },
    {
        'kode' : '1B',
        'jenis' : 'FF',
        'nama' : 'Sanksi FIFA',
        'kerugian' : '80000000',
        'pelaku' : 'Bupati'
    },
    {
        'kode' : '2B',
        'jenis' : 'PM',
        'nama' : 'SAMBO CS',
        'kerugian' : '95000000',
        'pelaku' : 'Jackie'
    }
]

history = {}

input_kasus_indo = {
    'kode' : 'kode',
    'jenis' : '0',
    'nama' : '0',
    'kerugian' : 0,
    'pelaku' : 0
}


print(f"{'KEY':<10}| {'Kode':<5} | {'Jenis':<15} | {'Nama':<10} | {'Kerugian':<10} | {'Pelaku':<10}")
print("-" * 32)
for data in kasus_indonesia:
    print(f"{data['kode']:<5} | {data['jenis']:<15} | {data['nama']:<10} | {data['kerugian']:<10} | {data['pelaku']:<10}")

print("-" * 32)



while True:
    print(f"{'WELCOME TO OUR COUNTRY ': ^100}")

    kasus = dict.fromkeys(input_kasus_indo.keys())
    print(kasus)

    banyak_kasus = input("Silahkan masukkan kode kasus (Contoh: 1BFF018) : ")
    kode = banyak_kasus[0:2]
    jenis = banyak_kasus[2:4]
    jumlah = int(banyak_kasus[4:])

    if jenis == "KK":
        kerugian = 120000000
        kasus = jumlah * kerugian
    elif jenis == "PL":
        kerugian = 50000000
        kasus = jumlah * kerugian
    elif jenis == "FF":
        kerugian = 80000000
        kasus = jumlah * kerugian
    elif jenis == "PM":
        kerugian = 95000000
        kasus = jumlah * kerugian
    else:
        print("Jenis kasus tidak ditemukan. Silahkan coba lagi!")



    KEY = ' '.join((random.choice(string.ascii_uppercase) for i in range(6)))

    history.update({KEY :input_kasus_indo})


    print(f"\n{'KEY':<10} {'kode':<15} {'jenis':<15} {'nama':<15} {'kerugian':<15} {'pelaku':<15}")
    print('~'*100)

    for kasus in history:
        KEY = kasus
        KODE = history[KEY] ['kode']
        JENIS = history[KEY] ['jenis']
        NAMA = history[KEY] ['nama']
        KERUGIAN = history[KEY] ['kerugian']
        PELAKU= history[KEY] ['pelaku']

        print(f"{KEY:<10} {KODE:<15} {JENIS:<15} {NAMA:<15} {KERUGIAN:<15} {PELAKU:<15}")

    print("\n")
    tambah = input("Mau tambah kagak (y/n) ??? ")
    if tambah == "n": #jika tidak menambah data akan berhenti
        break


print(f"Kode: {kode}, Jenis: {jenis}, Jumlah: {jumlah}, Kerugian: {jk}")
print("\nAkhir dari program, thanks a lot ") 
      

