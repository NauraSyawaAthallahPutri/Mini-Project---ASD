"""
Nama: Naura Syawal Athallah Putri
Kelas: Sistem Informasi - A - 23
NIM: 2309116032
---------------------------------------------------------------------------------------------------
    KETENTUAN!
1. Lanjutkan program kalian yang sudah buat pada mini project pertemuan 1.
2. Ubahlah penyimpanan data kalian dari menggunakan Struktur Data Bawaan menjadi Linked List (Single, Multiple, Circular) pilih salah satu.
3. Ubah fitur CRUD menggunakan Linked List
4. Fitur Create (Bisa menambahkan node di awal, akhir, dan diantara node).
5. Fitur Delete (Bisa menghapus node di awal, akhir, dan diantara node).
----------------------------------------------------------------------------------------------------
"""


# Class produk
class NodeProdukPanasonic:
    # Inisialisasi objek dengan atribut  yang akan di-inputkan
    def __init__(self, nama_item, kode_item, harga_item, stok_item, keterangan_item):
        self.nama_item = nama_item
        self.kode_item = kode_item
        self.harga_item = harga_item
        self.stok_item = stok_item
        self.keterangan_item = keterangan_item
        self.selanjutnya = None



# Class Double linked List
class SingleLinkedList:
    # Constructor untuk Single Linked List kosong
    def __init__(self):
        self.head = None
    
    # Method tambah node di awal
    def tambah_node_awal (self, data_produk):
        if self.head == None:
            self.head = data_produk
            print("""
                +==================================+
                |   Barang berhasil ditambahkan.   |
                +==================================+
                """)
            return
        else:
            node_baru = data_produk
            node_baru.selanjutnya = self.head
            self.head = node_baru
            print("""
                +==================================+
                |   Barang berhasil ditambahkan.   |
                +==================================+
                """)
            return
    
    # Metod tambah node di tengah
    """ 
    Node akan ditambahkan setelah node kode_item yang diinputkan.
    """
    def tambah_node_tengah(self, data_produk):
        kode_barang_sebelumnya = input(f"Masukkan kode barang sebelumnya: ")
        if self.head == None:
            print("""
                +=========================================================+
                |   List barang kosong. Tidak dapat menyisipkan barang.   
                +=========================================================+
                """)
            return
        # Mencari node dengan kode barang yang diinginkan
        head_node = self.head
        while head_node:
            if head_node.kode_item == kode_barang_sebelumnya:
                node_baru = data_produk
                node_baru.selanjutnya = head_node.selanjutnya
                head_node.selanjutnya = node_baru
                print("""
                +==================================+
                |   Barang berhasil disisipkan.    |
                +==================================+
                """)
                return
            head_node = head_node.selanjutnya
        
        print(f"""
            +===========================================================+
            |   Kode barang {kode_barang_sebelumnya} tidak ditemukan.   |
            +===========================================================+
            """)
    
    # Method tambah node di akhir
    def tambah_node_akhir(self, data_produk):
        if self.head == None:
            self.head = data_produk
            print("""
                +==================================+
                |   Barang berhasil ditambahkan.   |
                +==================================+
                """)
            return
        else:
            head_node = self.head
            while head_node.selanjutnya:
                head_node = head_node.selanjutnya
            head_node.selanjutnya = data_produk
            print("""
                +==================================+
                |   Barang berhasil ditambahkan.   |
                +==================================+
                """)
            return
            
    # Method menampilkan produk
    def menampilkan_produk (self):
        if self.head == None:
            print("""
                +====================+
                |   Barang kosong.   |
                +====================+
                """)
        else:
            head_node = self.head
            while head_node:
                print(f"Nama: {head_node.nama_item},\n Kode: {head_node.kode_item},\n Harga: {head_node.harga_item},\n Stok: {head_node.stok_item},\n Keterangan: {head_node.keterangan_item}")
                print(20*"-")
                head_node =head_node.selanjutnya
            print()
    
    # Method create produk   
    def tambah_produk(self):
        try:
            nama_item = str(input("Masukkan nama barang: "))
            kode_item = str(input("Masukkan kode barang: "))
            harga_item = int(input("Masukkan harga barang: "))
            stok_item = int(input("Masukkan stok barang: "))
            keterangan = str(input("Masukkan keterangan singkat: "))
            
            # Mengecek kesamaan kode
            head_node = self.head
            while head_node:
                if head_node.kode_item == kode_item:
                    print("Kode produk tidak boleh sama.")
                    kode_item = str(input("Masukkan kode barang: "))
                    continue
                head_node = head_node.selanjutnya
            
            # Mengecek kevalidan input
            while len(kode_item) > 12:
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
            
            # Inisialisasi barang yang di-inputkan ke node
            data_produk = NodeProdukPanasonic(nama_item, kode_item, harga_item, stok_item, keterangan)
            
            # Untuk memilih letak node
            """
            Apabila pengguna memasukan selain 1 dan 2, maka program otomatis 
            akan menambahkan barang setelah node terakhir.
            """
            pilih_letak = input(f"Mohon pilih letak barang yang ingin dimasukkan:\n 1. FIRST\n 2. MIDDLE\n 3. LAST\n >")
            # Menambahkan node di awal
            if pilih_letak == "1":
                self.tambah_node_awal(data_produk)
            # Menambahkan node di tengah
            elif pilih_letak == "2":
                self.tambah_node_tengah(data_produk)
            # Menambahkan node di akhir
            else:
                self.tambah_node_akhir(data_produk)

        except ValueError:
            print("Masukkan data sesuai yang diminta.")
    
    # Method hapus produk
    def hapus_produk(self):
        try:
            hapus = str(input("Silahkan masukkan kode barang yang ingin anda hapus: "))
            memastikan = input(f"Apakah anda yakin ingin menghapus barang tersebut?(Y/N) \n >").upper()
            
            if memastikan == "Y":
                # Inisialisasi head node
                head_node = self.head
                if head_node == None:
                    return
                # Jika barang yang dimau adalah head node (FIRST node)
                if head_node.kode_item == hapus:
                    self.head = head_node.selanjutnya
                    print("""
                        +==================================+
                        |     Barang berhasil dihapus.     |
                        +==================================+
                        """)
                    return
                # Mencari kode barang yang sesuai
                while (head_node.selanjutnya and head_node.selanjutnya.kode_item) != hapus:
                    head_node = head_node.selanjutnya
                if head_node.selanjutnya == True:
                    head_node.selanjutnya = head_node.selanjutnya.selanjutnya
                    print("""
                        +==================================+
                        |     Barang berhasil dihapus.     |
                        +==================================+
                        """)
                else:
                    print("""
                        +==================================+
                        |   Kode barang tidak ditemukan.   |
                        +==================================+
                        """)

            else:
                print("""
                    +==================================+
                    |     Barang gagal ditambahkan.    |
                    +==================================+
                    """)
        except ValueError:
            print("""
                    !=============================================!
                    |     Mohon masukkan sesuiai yang diminta.    |
                    +=============================================+
                    """)     
    
    # Method update stok
    def manajemen_stok(self):
        try:
            while True:
                pilih_produk = str(input("Silahkan masukkan kode barang yang ingin anda update: "))
                head_node = self.head
                while head_node:
                    if head_node.kode_item == pilih_produk:
                        stok_baru = int(input("Masukkan stok terbaru: "))
                        
                        # Mengecek kevalidan input
                        while stok_baru < 1:
                            print("Angka tidak boleh negatif.")
                            stok_baru = int(input("Masukkan stok barang: "))
                            continue
                                
                        # Menampilkan tampilan sementara untuk barang yang akan di-update
                        print("Detail produk: ")
                        print("Nama Item:", head_node.nama_item)
                        print("Harga Item:", head_node.harga_item)
                        print("Stok Item:", stok_baru)
                        print("Keterangan:", head_node.keterangan_item)
                        
                        memastikan = input("\nApakah anda yakin bahwa data berikut sudah benar? (Y/N)\n >").upper()
                        if memastikan == "Y":
                            head_node.stok_item = stok_baru
                            print("""
                            +==============================+
                            |   Stok berhasil di-update.   |
                            +==============================+
                            """)
                            return
                        elif memastikan == "N":
                            print("""
                            +===========================+
                            |   Stok batal di-update.   |
                            +===========================+
                            """)
                            break
                        else:
                            print("""
                            +==========================+
                            |   Pilihan tidak valid.   |
                            +==========================+
                            """)
                            break
                    head_node = head_node.selanjutnya

                else:
                    print("""
                        +=============================+
                        |   Produk tidak ditemukan.   |
                        +=============================+
                        """)
                    break         
        except ValueError:
            print("""
            !=============================================!
            |     Mohon masukkan sesuiai yang diminta.    |
            +=============================================+
            """) 

                
                
# Function Main Program
def main_program():
    try:
        linked_list = SingleLinkedList()
        while True:
            print("""
                    +================================================+

                            P   A   N   A   S   O   N   I   C
                            
                                Product  Management  System
                    
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
                linked_list.menampilkan_produk()
            elif pilih_menu == "2":
                linked_list.tambah_produk()
            elif pilih_menu == "3":
                linked_list.hapus_produk()
            elif pilih_menu == "4":
                linked_list.manajemen_stok()
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
        print("""
            !=============================================!
            |     Mohon masukkan sesuiai yang diminta.    |
            +=============================================+
            """)     


# Memanggil function main_program() untuk menjalankan program        
main_program()



