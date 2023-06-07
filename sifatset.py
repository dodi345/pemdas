# set tidak bisa menggunakan index
my_set = {'a', 'b', 'c'}
print(my_set[0])

# sset berdifat tidak berurutan
my_set = {'a', 'b', 'c'}
print(my_set)

# set tidak bisa menerima nilai duplikat
set_kalimat = {'python', 'semangat', 'belajar', 'pemrograman', 'python'}
print(set_kalimat)

# set tidak mengenal indeks
print(set_kalimat[2])
print(set_kalimat[-1])

# set tidak bisa dirubah
set_kalimat[2] = 'bermain'
print(set_kalimat)