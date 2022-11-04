def cek(bilangan):
    if bilangan > 1:
        for i in range(2, bilangan):
            if (bilangan % i) == 0:
                return f"{bilangan} bukan bilangan prima karena habis dibagi oleh {i}"
                break
        else:
            return f"{bilangan} adalah bilangan prima"
    else:
        return f"{bilangan} bukan bilangan prima"

if __name__ == "__main__":
    try:
        print(cek(int(input("Masukkan angka: "))))
    except:
        print("Input harus bilangan bulat")
