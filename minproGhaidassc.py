print("SELAMAT DATANG")

print("=====Pilihan Menu====")
print("1. tambah produk")
print("2. edit jumlah item")
print("3. hapus produk")

pilih = input("menu apa yang akan kamu pilih?: ")
nama_produk = ["baju", "jilbab", "sepatu", "tas", "buku", "pulpen"]
jumlah_item = ["1", "2", "3", "4", "5","6", "7"]


if pilih == "1":
    while True:
        tambah_produk = input("produk apa yang akan ditambahkan?: ").lower()

        if tambah_produk in nama_produk:
            print(f"produk '{tambah_produk}' berhasil ditambahkan ke keranjang")
            break
        else:
            print("produk yang anda pilih tidak tersedia. Silahkan pilih produk lain.")
            ulang = input("ingin memilih produk lain? (ya/tidak): ").lower()
            if ulang != "ya":
                print("proses selesai")
                break

elif pilih == "2":
        while True:
            edit_jumlah_item = input("masukkan jumlah item yang ingin diperbarui: ").lower()

            if edit_jumlah_item in jumlah_item:
                print(f"jumlah item produk diperbarui")
                break  
            else:
                print("jumlah item yang anda pilih tidak tersedia. Silahkan masukkan jumlah item lain")
                ulang = input("ingin memasukkan jumlah item lain?: ").lower()
                if ulang != "ya":
                    print("proses selesai")
                    break

elif pilih == "3":
    while True:
        produk_dihapus = input("produk apa yang ingin dihapus?: ").lower()

        if produk_dihapus in nama_produk:
            nama_produk.remove(produk_dihapus)
            print(f" '{produk_dihapus}' telah dihapus dari keranjang")
            break
        else:
            print("produk tidak ditemukan di keranjang, Silahkan memilih produk lain.")
            ulang = input("ingin menghapus produk lain?: ").lower()
            if ulang != "ya":
                print("proses selesai")
                break

else:
    print("info yang anda masukkan tidak valid, silahkan memilih ulang")


print("TERIMAKASIH TELAH MENGGUNAKAN LAYANAN KAMI")
print("SILAHKAN DATANG KEMBALI:))")