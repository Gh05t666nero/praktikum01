def pangkat(angka, power):
    if power == 0:
        return 1
    else:
        return angka * pangkat(angka, power - 1)

def main():
    angka = int(input("Masukkan angka: "))
    power = int(input("Masukkan pangkat: "))
    print(f"{angka} pangkat {power} adalah {pangkat(angka, power)}")

if __name__ == "__main__":
    main()
