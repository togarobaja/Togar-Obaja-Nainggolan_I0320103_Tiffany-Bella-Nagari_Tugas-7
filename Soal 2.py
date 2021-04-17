import math
a = -9.08
b = 14.65
c = -23.67
d = float(input("masukkan angka yang diinginkan :"))
# Perhitungan
x = a * d + b * d + c
print('x kuadrat = ',math.sqrt(x))
y = b * d + c + d
print('y kuadrat = ',math.sqrt(y))
z = a+b+c+d
print("jumlsh mutlak semua nilai",abs(z))
komponen = [math.ceil(x), math.ceil(y), math.ceil(z)]
# menampilkan semua hasil perhitungan
print("data perhitungan (pembulatan atas)", komponen)