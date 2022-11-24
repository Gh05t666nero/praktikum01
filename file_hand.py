def buatFile():
    namaFile = input("Masukkan nama file : ")
    file = open(namaFile, "w")
    file.close()
    print("File berhasil dibuat")


def tambahData():
    namaFile = input("Masukkan nama file : ")
    file = open(namaFile, "a")
    data = input("Masukkan data : ")
    file.write(data)
    file.write("\n")
    file.close()
    print("Data berhasil ditambahkan")


def bacaFile():
    namaFile = input("Masukkan nama file : ")
    file = open(namaFile, "r")
    print(file.read())
    file.close()


def hapusFile():
    namaFile = input("Masukkan nama file : ")
    os.remove(namaFile)
    print("File berhasil dihapus")


def menu():
    print("Menu")
    print("1. Buat File")
    print("2. Tambah Data")
    print("3. Baca File")
    print("4. Hapus File")
    print("5. Keluar")
    pilih = input("Pilih menu : ")
    if pilih == "1":
        buatFile()
    elif pilih == "2":
        tambahData()
    elif pilih == "3":
        bacaFile()
    elif pilih == "4":
        hapusFile()
    elif pilih == "5":
        exit()
    else:
        print("Menu tidak tersedia")
        menu()


menu()
