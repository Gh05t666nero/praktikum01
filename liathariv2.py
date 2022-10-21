class Bulan:
    def __init__(self, bulan, tahun):
        self.bulan = bulan
        self.tahun = tahun

    def __str__(self):
        return f'{self.bulan} {self.tahun}'

    def jumlah_hari(self):
        if self.bulan == 1 or self.bulan == 3 or self.bulan == 5 or self.bulan == 7 or self.bulan == 8 or self.bulan == 10 or self.bulan == 12:
            return 31
        elif self.bulan == 4 or self.bulan == 6 or self.bulan == 9 or self.bulan == 11:
            return 30
        elif self.bulan == 2:
            if self.tahun % 4 == 0:
                return 29
            else:
                return 28

def main():
    try:
        bulan = int(input('Masukkan bulan: '))
        if bulan > 12 or bulan < 1:
            print('Bulan tidak valid')
        else:
            tahun = int(input('Masukkan tahun: '))
            hasil = Bulan(bulan, tahun)
            print(f'Jumlah hari pada bulan {bulan} tahun {tahun} adalah {hasil.jumlah_hari()} hari.')
    except ValueError:
        print('Inputan tidak valid')

if __name__ == '__main__':
    main()
