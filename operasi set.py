# UNION
print("UNION")
set_kelas_A = {'Ray', 'Sheva','Yisviana','Tsabit','Mika'}
set_kelas_B = {'Ahmad','Jhonny','Sins','Jordi','Dodi'}

# cara 1
print( set_kelas_A | set_kelas_B)

# cara 2
print(set_kelas_A.union(set_kelas_B))

set_Mhs_Prodi = set_kelas_A | set_kelas_B
print(set_Mhs_Prodi)

# INTERSECTION
print("INTERSECTION")
set_kelas_A = {'Ray', 'Sheva','Yusviana','Tsabit','Mika'}
set_pengurus= {'Ahmad','Sheva','Yusviana','Jordi','Dodi'}

# cara 1
print(set_kelas_A & set_pengurus)
# cara 2
print(set_kelas_A.intersection(set_pengurus))

set_kelasA_pengurus = set_kelas_A & set_pengurus
print(set_kelasA_pengurus)


# DIFFERENCE
print("DIFFERENCE")
set_kelas_A = {'Ray', 'Sheva','Yusviana','Tsabit','Mika'}
set_pengurus= {'Tsabit','Budi','Yusviana','Jordi','Dodi'}


# cara 1
# anggota kelas a yang bukan pengurus
print(set_kelas_A - set_pengurus)
print(set_kelas_A.difference(set_kelasA_pengurus))

# cara 2
print(set_pengurus - set_kelas_A)
print(set_pengurus.difference(set_kelas_A))

set_kelasA_nonpengurus = (set_kelas_A - set_pengurus)
print(set_kelasA_nonpengurus)

#SYMMETRIC DIFFERENCE

print("SYMETRIC DIFFERENCE")
set_kelas_A = {'Ray', 'Sheva','Yusviana','Tsabit','Mika'}
set_pengurus= {'Tsabit','Budi','Yusviana','Jordi','Dodi'}

print(set_kelas_A.symmetric_difference(set_pengurus))