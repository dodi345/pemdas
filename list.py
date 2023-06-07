#contoh pemanggilan list

deret = [1,2,3,4,5,6,7]
print(sum(deret))
print(max(deret))
print(deret[-3])
print(deret[2:5])

#append insert prepend
list_buah = ['Mangga',  'Pisang', 'Manggis', 'Durian']
list_buah.append('Semangka')
list_buah.insert(2, 'Mangkudu')

list_buah[2] = 'Rungkad'
print(list_buah)


#menghapus dengan del,remove,pop()
list_angka = [1,2,3,4,5]
print(list_angka)

#hapus satu angka dibelakang
angka_yang_terhapus = list_angka.pop()

print("angka yang terhapus", angka_yang_terhapus)
print(list_angka)

#menghapus dengan remove
list_buah = ['anggur','mangga','pepaya','apel']
print(list_buah)

#hapus item pertama dengan nilai 'apel'
list_buah.remove('apel')
print(list_buah)

#menghapus dengan del
list_buah = ['mangga','jambu','jeruk','anggur']
print(list_buah)

del list_buah[1]
print(list_buah)

del list_buah[0:2]
print(list_buah)


#sort(), 
list_buah.sort()
print(list_buah)

sistem = ['Windows','Android', 'MacOS', 'Linux']
print("Orisnil : ", sistem)

#reverse()
sistem.sort(reverse=False)
print("Update List ", sistem)


#########
list3 = ['a', 'b', 'c', 'd']
list4 = [1, 2, 3, 4]
print(list3 + list4)
print(list4 * 3)
for i in list3:
    list4.append(i)
    print(list4)

