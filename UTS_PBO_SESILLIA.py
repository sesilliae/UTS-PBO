def menu() :
    print("SELAMAT DATANG DI PENYIMPANAN UANG DIGITAL")
    print("1.Informasi Saldo")
    print("2.Tambah saldo")
    print("3.Ambil Saldo")
    print("4.Keluar")
    print("================")

def tampilkansaldo() :
    saldoumum = "0"
    saldotabungan = "0"
    print("Saldo umum anda saat ini adalah adalah Rp.",(saldoumum) )
    print("Saldo umum anda saat ini adalah adalah Rp." ,(saldotabungan))

def tambahsaldo() :
    print("1.Umum")
    print("2.Tabungan")
    pilih = int(input("Pilih penyimpanan : "))
    if pilih == 1:
            print("Menambahkan saldo umum")
            tambahumum = input("Nominal Yang Akan Di Tambahkan: ")
            hasil1= saldoumum + tambahumum
            print("Saldo umum anda saat ini adalah adalah Rp.",hasil1)
    elif pilih == 2:
            print("Menambahkan saldo tabungan")
            tambahtabungan = input("Nominal Yang Akan Di Tambahkan: ")
            hasil2= saldotabungan + tambahtabungan
            print("Saldo umum anda saat ini adalah adalah Rp.",hasil2)

def ambilsaldo() :
    print("1.Umum")
    print("2.Tabungan")
    pilih = int(input("Pilih penyimpanan : "))
    if pilih == 1:
            print("Menambahkan saldo umum")
            ambilumum = input("Nominal Yang Akan Di Ambil: ")
            hasil3= saldoumum + ambilumum
            print("Saldo umum anda saat ini adalah adalah Rp.",hasil3)
    elif pilih == 2:
            print("Menambahkan saldo tabungan")
            tambahtabungan = input("Nominal Yang Akan Di Tambahkan: ")
            hasil4= saldotabungan + ambiltabungan
            print("Saldo umum anda saat ini adalah adalah Rp.",hasil4)

def keluar() :
    print("TERIMA KASIH")

#PROGRAM UTAMA
    print("SELAMAT DATANG PADA PROGRAM")
    menu()
    a = int(input("Silahkan pilih menu : "))
    if a == 1:
            tampilkansaldo()
            menu()
    elif a == 2:
            tambahsaldo()
    elif a == 3:
            ambilsaldo()
    elif a == 4:
            keluar()
    else:
            print("pilihan tidak tersedia")