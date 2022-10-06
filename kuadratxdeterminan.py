print("Program untuk mencari akar persamaan kuadrat dan determinan")
print("Menggunakan rumus (ax^2 + bx + c = 0)")
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))
determinan = b**2 - 4*a*c
print(f"Determinan: {determinan}")
if determinan > 0:
    print("Persamaan kuadrat memiliki dua akar")
    print("x1 = ", (-b + determinan**0.5)/(2*a))
    print("x2 = ", (-b - determinan**0.5)/(2*a))
elif determinan == 0:
    print("Persamaan kuadrat memiliki satu akar")
    print("x = ", -b/(2*a))
else:
    print("Persamaan kuadrat tidak memiliki akar")
