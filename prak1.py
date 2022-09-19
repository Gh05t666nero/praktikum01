NAMA = input('Masukkan Nama: ')
ALAMAT = input('Masukkan Alamat: ')
UMUR = input('Masukkan Umur: ')
ANGKATAN = input('Masukkan Angkatan: ')
IS_MALE = True

if IS_MALE:
    GENDER = 'Laki-laki'
elif IS_MALE == False:
    GENDER = 'Perempuan'
else:
    GENDER = 'Netral :v'

print(f'Nama saya {NAMA}, tinggal di {ALAMAT}, umur saya {UMUR} tahun, angkatan {ANGKATAN}, dan jenis kelamin saya adalah {GENDER}')