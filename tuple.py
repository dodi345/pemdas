# operasi da metode tuple

data_tuple = (12, 14, 16, 18)
print(data_tuple)
print(data_tuple[1])
print(data_tuple[-1])
print(len(data_tuple))
print(max(data_tuple))
print(min(data_tuple))
print(sum(data_tuple))
print(data_tuple+(2,3,4))
print(data_tuple*2)

# mengekstrak isi tuple
mahasiswa = ('JHONNY SINS', 'SUBANG', 80)

# ekstrak data atau sequence unpacking
nama, alamat, usia =  mahasiswa

# setiap variable diatas akan memiliki niladi dari tiap isi tuple secara berurutan
print('Nama : ',nama)
print('Alamat : ', alamat)
print('Usia : ',usia)