'''
Program menghitung dua jarak antara dua titik koordinat
Dikodekan oleh M. Fauzan Wijaya
25 September 2022
'''

import math

print('Program menghitung dua jarak antara dua titik koordinat')
print('Dikodekan oleh M. Fauzan Wijaya')
x1 = float(input("Masukkan latitude titik A: "))
y1 = float(input("Masukkan longitude titik A: "))
x2 = float(input("Masukkan latitude titik B: "))
y2 = float(input("Masukkan longitude titik B: "))

def calculate(x1, y1, x2, y2):
    # Mengonversi latitude dan longitude ke radians
    x1 = math.radians(x1)
    y1 = math.radians(y1)
    x2 = math.radians(x2)
    y2 = math.radians(y2)
    # Menghitung jarak
    distance = 6371.01 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
    return distance

print(calculate(x1, y1, x2, y2))