class Tiket:
    def __init__(self, umur):
        self.umur = umur

    def harga(self):
        if self.umur <= 2:
            harga = 0
        elif self.umur >= 3 and self.umur <= 12:
            harga = 14
        elif self.umur >= 65:
            harga = 18
        else:
            harga = 23
        return harga

total = 0
while True:
    umur = int(input("Masukkan umur: "))
    tiket = Tiket(umur)
    harga = tiket.harga()
    total += harga
    if harga == 0:
        harga = "Gratis"
    print("Harga tiket: ", harga)
    lagi = input("Ingin menambahkan data lagi? (y/t) ")
    if lagi.lower() == "t":
        print("Total harga tiket: $", total)
        while True:
            bayar = int(input("Masukkan jumlah uang yang dibayarkan: $"))
            if bayar < total:
                print("Uang anda kurang")
            elif bayar > total:
                print("Uang anda lebih")
                print(f"Silahkan ambil kembalian: ${bayar - total}")
                break
            elif bayar == total:
                print("Uang anda pas")
                break
        break
