panjang = int(input('Masukkan Panjang Ruangan: '))
lebar = int(input('Masukkan Lebar Ruangan: '))
satuan = input('Ketik Satuan Meter/Inci: ')

if satuan == 'Meter' or satuan == 'meter':
    satuan = 'm'
elif satuan == 'Inci' or satuan == 'inci':
    satuan = 'i'
else:
    satuan = 'Satuan tidak diketahui.'
    exit()

total = panjang*lebar

print(f'Diketahui panjang dari sebuah ruangan adalah {panjang}{satuan} dengan lebar {lebar}{satuan}, sehingga luas dari ruangan tersebut adalah {total}{satuan}')