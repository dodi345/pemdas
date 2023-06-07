from collections import deque

antri = deque([1,2,3,4,5])
print(f"Data Sekarang : {antri}")

antri.append(6)
print(f"data masuk : {6}")
print(f"Data Sekarang : {antri}")

antri.append(7)
print(f"data masuk : {7}")
print(f"Data Sekarang : {antri}")

# decrease antrian
out = antri.popleft()
print(f"data keluar : {out}")
print(f"data sekarang : {antri}")

out = antri.popleft()
print(f"data keluar : {out}")
print(f"data sekarang : {antri}")

out = antri.popleft()
print(f"data keluar : {out}")
print(f"data sekarang : {antri}")

antri.append(8)
print(f"data masuk : {8}")
print(f"data sekarang {antri}")