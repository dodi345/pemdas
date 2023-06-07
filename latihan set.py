A = {'Budi','Krisna','Fajar','Ucup','Faqih','Gesta','Debby','Izzis','Riza','Aufa','Dodi'}
B = {'Ahmad','Budi','Fajar','Ucup','Hilal','Faqih','Zahran','Debby','Nurul','Aca','Aufa','Dodi','Dzikry'}
C = {'Ahmad','Krisna','Fajar','Hilal','Faqih','Gesta','Zahran','Izzis','Nurul','Riza','Aca','Aufa','Luthfi'}

#UNION
print("UNION")
print("A∪B : " ,A.union(B) )
print("A∪C : ", A.union(C))
print("B∪C : ",B.union(C))
mahasiswa_1B = A.union(B).union(C)
print("A∪B∪C : ",mahasiswa_1B)


#INTERSECTION
print("INTERSECTION")
print("A∩B : ",A.intersection(B))
print("A∩C : ",A.intersection(C))
print("B∩C : ",B.intersection(C))
irisan = A.intersection(B).intersection(C)
print("A∩B∩C : ",irisan)

# DIFFFERENCE
print("DIFFERENCE")
print("A-B : ",A.difference(B))
print("B-A : ",B.difference(A))
print("A-C : ",A.difference(C))
print("C-A : ",C.difference(A))
print("B-C : ",B.difference(C))
print("C-B : ",C.difference(B))
print("A-B-C : ",A.difference(B).difference(C))
print("B-C-A : ",B.difference(C).difference(A))
print("C-A-B : ",C.difference(A).difference(B))

# SYMMETRIC DIFFERENCE
print("SYMMETRIC DIFFERENCE")
print("A⊕B : ",A.symmetric_difference(B))
print("A⊕C : ",A.symmetric_difference(C))
print("B⊕C : ",B.symmetric_difference(C))
beda_setangkup = A.symmetric_difference(B).symmetric_difference(C)
print("A⊕B⊕C : ",beda_setangkup)
