data_set = {'Bogor', 'Bandung', 'Jakarta'}
print(len(data_set))

data_set2 = {1,2,3,4,5}
print(max(data_set2))
print(min(data_set2))
print(sum(data_set2))

# menambah 1 elemen
data_set.add('Subang')
print(data_set)

data_set.add((10, 20, 30)) #bisa ditambah dengan tuple
print(data_set)

# menambahkan banyak elemen
set_hewan = {'Ayam', 'Sapi', 'Kambing'}
set_hewan.update({100, 200, 300}) #bisa ditambah dengan himpunan
print(set_hewan)
set_hewan.update([1000, 2000, 3000]) #bisa ditambah dengan list
print(set_hewan)

# menghapus set
data_set = {'A', 'B','C','D','E','F','G'}
print(data_set)

# menghapus nilai jika nilai tidak ada yang error
data_set.remove('A')
print(data_set)

# menghapus nilai, jika tidak ada yg eerro
data_set.discard('B')
print(data_set)

# menghapus nilai dari kiri
data_set.pop()
print(data_set)

# menghapus semua anggota
data_set.clear()
print(data_set)