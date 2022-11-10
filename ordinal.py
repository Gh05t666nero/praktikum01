def eksekusi(angka):
    if angka % 100 in (11, 12, 13):
        return (angka, "th")
    else:
        return (angka, {1 : "st", 2 : "nd", 3 : "rd"}.get(angka % 10, "th"))

while True:
    try:
        angka = int(input("Masukkan Angka: "))
        if angka < 0:
            print("Terjadi kesalahan, angka yang dimasukkan harus lebih besar atau sama dengan 0")
        elif angka == 0:
            print((angka, "th"))
            print("Terima kasih telah menggunakan program saya")
            break
        else:
            print(eksekusi(angka))
    except ValueError:
        print("Terjadi kesalahan, masukkan harus berupa angka!")
