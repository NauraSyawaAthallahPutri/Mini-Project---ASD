"""
Nama: Naura Syawal Athallah Putri
Kelas: Sistem Informasi - A - 23
NIM: 2309116032
---------------------------------------------------------------------------------------------------
    KETENTUAN !
1. Buatlah program dengan menggunakan bahasa pemrograman Python dengan ketentuan berikut:
2. Membuat program CRUD menggunakan salah satu struktur data bawaan (List, Dictionary, Tuple, Set).
3. Memiliki paling sedikit 5 variabel / field.
4. Terapkan dalam bentuk Object Oriented Programming.
----------------------------------------------------------------------------------------------------
"""

# Import Library
from prettytable import PrettyTable

# Dictionary untuk menyimpan produk
"""
Key: Kode Produk -> str < 12
Value: Nama, Kode, Harga, Stok, Keterangan
"""
produk = {}


# Class produk
class ProdukPanasonic:
    # Inisialisasi objek dengan atribut  yang akan di-inputkan
    def __init__(self, nama_item, kode_item, harga_item, stok_item, keterangan_item):
        self.nama_item = nama_item
        self.kode_item = kode_item
        self.harga_item = harga_item
        self.stok_item = stok_item
        self.keterangan_item = keterangan_item



# Class manajemen Produk
class ManajemenProduk:
    
    # Method menampilkan produk
    def tampilkan_produk():
        # Menampilkan produk dengan menggunakan PrettyTable
        table = PrettyTable()
        table.field_names = ["Kode Item", "Nama Item", "Harga Item", "Stok Item", "Keterangan"]
        
        for k, v in produk.items():
            table.add_row([k, v.nama_item, v.harga_item, v.stok_item, v.keterangan_item])
        
        print(table)
    
    # Method create produk   
    def tambah_produk():
        try:
            
            nama_item = str(input("Masukkan nama barang: "))
            kode_item = str(input("Masukkan kode barang: "))
            harga_item = int(input("Masukkan harga barang: "))
            stok_item = int(input("Masukkan stok barang: "))
            keterangan = str(input("Masukkan keterangan singkat: "))
            
            # Mengecek kevalidan input
            while len(kode_item) > 12 :
                print("Kode produk harus kurang dari sama dengan 12 karakter.")
                kode_item = str(input("Masukkan kode barang: "))
                continue
            while stok_item < 1:
                print("Angka tidak boleh negatif.")
                stok_item = int(input("Masukkan stok barang: "))
                continue
            while harga_item < 1000:
                print("Harga tidak valid")
                harga_item = int(input("Masukkan harga barang: "))
                continue
                
                
            memastikan = input(f"Apakah anda yakin bahwa data tersebut sudah benar?(Y/N) \n >").upper()
            
            if memastikan == "Y":
                produk_baru = ProdukPanasonic(nama_item, kode_item, harga_item, stok_item, keterangan)
                produk[kode_item] = produk_baru
                print("Barang berhasil ditambahkan.")
                return produk_baru
            elif memastikan == "N":
                print("Barang batal ditambahkan.")
            else:
                print("Barang gagal ditambahkan.")
                
        except ValueError:
            print("Masukkan data sesuai yang diminta.")
    
    # Method untuk menghapus produk
    def hapus_produk():
        try:
            
            hapus = str(input("Silahkan masukkan kode barang yang ingin anda hapus: "))
            memastikan = input(f"Apakah anda yakin ingin menghapus barang tersebut?(Y/N) \n >").upper()
            
            if memastikan == "Y":
                del produk[hapus]
                print("Barang berhasil dihapus.")
                return
            elif memastikan == "N":
                print ("Barang batal untuk dihapus.")
            else:
                print("Barang gagal untuk dihapus.")
                
        except ValueError:
            print("Mohon masukkan data yang diminta.")       
    
    # Method update stok
    def manajemen_stok():
        try:
            
            while True:
                pilih_produk = str(input("Silahkan masukkan kode barang yang ingin anda update: "))
                
                if pilih_produk in produk:
                    produk_terpilih = produk[pilih_produk]
                    stok_baru = int(input("Masukkan stok terbaru: "))
                    
                    # Mengecek kevalidan input
                    while stok_baru < 1:
                        print("Angka tidak boleh negatif.")
                        stok_baru = int(input("Masukkan stok barang: "))
                        continue
                            
                    # Menampilkan tampilan sementara untuk barang yang akan di-update
                    print("Detail produk: ")
                    print("Nama Item:", produk_terpilih.nama_item)
                    print("Harga Item:", produk_terpilih.harga_item)
                    print("Stok Item:", produk_terpilih.stok_item)
                    print("Keterangan:", produk_terpilih.keterangan_item)
                    
                    memastikan = input("\nApakah anda yakin bahwa data berikut sudah benar? (Y/N)\n >").upper()
                
                    if memastikan == "Y":
                        produk_terpilih.stok_item = stok_baru
                        print("Stok berhasil di-update.")
                        return
                    elif memastikan == "N":
                        print("Stok batal di-update.")
                        break
                    else:
                        print("Pilihan tidak valid.")
                        break
                    
                else:
                    print("Produk tidak ditemukan.")
                    break
                    
        except ValueError:
            print("Mohon masukkan sesuai data yang diminta.")

                
                
# Function Main Program
def main_program():
    try:
        
        while True:
            print("""
                    +================================================+

                            P   A   N   A   S   O   N   I   C
                            
                                Product  management  system
                    
                    +================================================+
                """)
            print(f"""
                    Welcome!     
                    Ada yang perlu kami bantu?
                    --------------------------------------------------
                    1. Lihat Produk
                    2. Tambah Produk
                    3. Hapus Produk
                    4. Manajemen Stok
                    5. Keluar
                """)

            pilih_menu = input(">")

            if pilih_menu == "1":
                ManajemenProduk.tampilkan_produk()
            elif pilih_menu == "2":
                ManajemenProduk.tambah_produk()
            elif pilih_menu == "3":
                ManajemenProduk.hapus_produk()
            elif pilih_menu == "4":
                ManajemenProduk.manajemen_stok()
            elif pilih_menu == "5":
                print("""
                    Thank you for your participation!
                    
                    +==============================================+
                    
                            P   A   N   A   S   O   N   I   C
                            💡A better Life, A Better World💡 
                    
                    +==============================================+
                
                    """)
                break
            else:
                print("Pilihan tidak ada di daftar menu.")
                
    except ValueError:
        print("Silahkan masukkan sesuai data yang diminta.")


# Memanggil function main_program() untuk menjalankan program        
main_program()



