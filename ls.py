hobi = []
stop = False
i = 0

#mengisi hobi
while(not stop):
    hobi_baru = input("Masukan Hobi Baru anda ke-{} : ".format(i))
    hobi.append(hobi_baru)
    #increment i
    i += 1

    tanya = input("Mau isi hobi lagi ? (Y/N) : ")
    if (tanya == "N"):
        stop= True
#Cetak semua hobi
print("=" * 10)
print(f"Kamu memiliki hobi ".format(len(hobi)))
for hb in hobi:
    print("- {}".format(hb))
