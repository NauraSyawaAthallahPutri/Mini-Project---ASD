"""
Nama: Naura Syawal Athallah Putri
Kelas: Sistem Informasi - A - 23
NIM: 2309116032
---------------------------------------------------------------------------------------------------
- Penambahan Stack sebagai fitur Undo.
Node barang yang dihapus -> Masuk ke dalam stack.
Undo barang -> Mengambil stack teratas -> Menambahkannya ke linked list sebagai barang baru di awal.
----------------------------------------------------------------------------------------------------
"""

# Import Library
from prettytable import PrettyTable
import math

# Class Node
class NodeProdukPanasonic:
    # Inisialisasi objek dengan atribut  yang akan di-inputkan
    def __init__(self, nama_item, kode_item, harga_item, stok_item, keterangan_item):
        self.nama_item = nama_item
        self.kode_item = kode_item
        self.harga_item = harga_item
        self.stok_item = stok_item
        self.keterangan_item = keterangan_item
        self.next = None



# Class Double linked List
class SingleLinkedList: 
    # Constructor untuk head node dan tail node
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Method tambah node di awal
    def tambah_node_awal (self, node_baru):
        if self.head is None:
            self.head = node_baru
            self.tail = node_baru
            tambah = True
        else:
            node_baru.next = self.head
            self.head = node_baru
            tambah = True
        return self.head
    
    # Metod tambah node di tengah
    """ 
    Node akan ditambahkan setelah node kode_item yang diinputkan.
    """
    def tambah_node_tengah(self, node_baru):
        kode_barang_sebelumnya = input("Masukkan kode barang sebelumnya: ")
        if self.head is None:
            print("""
                +=========================================================+
                |   List barang kosong. Tidak dapat menyisipkan barang.   |
                +=========================================================+
                """)
            return 

        # Mencari node dengan kode barang yang diinginkan
        current_node = self.head
        while current_node:
            if current_node.kode_item == kode_barang_sebelumnya:
                if current_node.next is None: # Kalau node selanjutnya kosong
                    self.tail = node_baru
                tambah = True
                node_baru.next = current_node.next
                current_node.next = node_baru
                print("""
                +==================================+
                |   Barang berhasil disisipkan.    |
                +==================================+
                """)
                return current_node.next
            current_node = current_node.next
        print(f"""
            +===========================================================+
            |   Kode barang {kode_barang_sebelumnya} tidak ditemukan.   |
            +===========================================================+
            """)
        return None
    
    # Method tambah node di akhir
    def tambah_node_akhir(self, node_baru):
        if self.head is None:
            self.head = node_baru
            self.tail = node_baru
            tambah = True
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node_baru
            self.tail = node_baru
            tambah = True
            return current_node.next
        return self.head
            
    # Method menampilkan produk
    def menampilkan_produk (self):
        if self.head is None:
            print("""
                +====================+
                |   Barang kosong.   |
                +====================+
                """)
        else:
            head_node = self.head
            # Membuat tabel menggunakan PrettyTable
            table = PrettyTable()
            table.field_names = ["Kode Item", "Nama Item", "Harga Item", "Stok Item", "Keterangan"]

            # Memasukkan data dari setiap node ke dalam tabel
            while head_node is not None:
                table.add_row([head_node.kode_item, head_node.nama_item, head_node.harga_item, head_node.stok_item, head_node.keterangan_item])
                head_node = head_node.next
            print(table)
            
    # Method create produk   
    def tambah_produk(self, node_baru, pilih_letak, tambah):
        tambah = False
        try:
            nama_item = str(input("Masukkan nama barang: "))
            kode_item = str(input("Masukkan kode barang: "))
            harga_item = int(input("Masukkan harga barang (Rp) : "))
            stok_item = int(input("Masukkan stok barang: "))
            keterangan = str(input("Masukkan keterangan singkat: "))
            
            # Mengecek kesamaan kode
            head_node = self.head
            while head_node:
                while head_node.kode_item == kode_item:
                    print("Kode produk tidak boleh sama.")
                    kode_item = str(input("Masukkan kode barang: "))
                    continue
                head_node = head_node.next
            
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
            node_baru = NodeProdukPanasonic(nama_item, kode_item, harga_item, stok_item, keterangan)
            
            # Untuk memilih letak node
            """
            Apabila pengguna memasukan selain 1 dan 2, maka program otomatis 
            akan menambahkan barang setelah node terakhir.
            """
            pilih_letak = input(f"Mohon pilih letak barang yang ingin dimasukkan:\n 1. FIRST\n 2. MIDDLE\n 3. LAST\n >")
            # Menambahkan node di awal
            if pilih_letak == "1":
                self.tambah_node_awal(node_baru)
            # Menambahkan node di tengah
            elif pilih_letak == "2":
                self.tambah_node_tengah(node_baru)
            # Menambahkan node di akhir
            else:
                self.tambah_node_akhir(node_baru)
            
            if tambah == True:
                print("""
                +==================================+
                |   Barang berhasil ditambahkan.   |
                +==================================+
                """) 

        except ValueError:
            print("Masukkan data sesuai yang diminta.")
    
    # Method hapus produk
    def hapus_produk(self):
        try:
            hapus = str(input("Silahkan masukkan kode barang yang ingin anda hapus: "))
            memastikan = input(f"Apakah anda yakin ingin menghapus barang tersebut?(Y/N) \n >").upper()
            
            if memastikan == "Y":
                # Inisialisasi head node
                current = self.head
                deleted_node = None
                
                if current is None:
                    print("""
                        +=========================+
                        |   List barang kosong.   |
                        +=========================+
                        """)
                    return None
                # Jika barang yang dimau adalah head node (FIRST node)
                elif current.kode_item == hapus:
                    deleted_node = current
                    self.head = current.next
                    if current.next is None: # Jika barang yang dihapus tail node.
                        self.tail = None 
                    print("""
                        +================================+
                        |     Barang berhasil dihapus.   |
                        +================================+
                        """)
                    return deleted_node
                
                # Mencari kode barang yang sesuai
                while current.next:
                    if current.next.kode_item == hapus:
                        deleted_node = current.next
                        current.next = current.next.next
                        # Jika node yang dihapus adalah tail
                        if current.next is None:
                            self.tail = current
                        print("""
                            +================================+
                            |     Barang berhasil dihapus.   |
                            +================================+
                            """)
                        return deleted_node
                    current = current.next
                # Barang tidak ditemukan
                print("""
                    +==================================+
                    |   Kode barang tidak ditemukan.   |
                    +==================================+
                    """)
                return None
            else:
                print("""
                    +==============================+
                    |     Barang gagal dihapus.    |
                    +==============================+
                    """)
                return None
        except ValueError:
            print("""
                    !=============================================!
                    |     Mohon masukkan sesuai yang diminta.    |
                    +=============================================+
                    """)
            return None
    
    # Method update stok
    def manajemen_stok(self):
        try:
            pilih_produk = str(input("Silahkan masukkan kode barang yang ingin anda update: "))
            current_node = self.head
            while current_node:
                if current_node.kode_item == pilih_produk:
                    stok_baru = int(input("Masukkan stok terbaru: "))
                    
                    # Mengecek kevalidan input
                    while stok_baru < 1:
                        print("Angka tidak boleh negatif.")
                        stok_baru = int(input("Masukkan stok barang: "))
                        continue
                            
                    # Menampilkan tampilan sementara untuk barang yang akan di-update
                    print("Detail produk: ")
                    print("Nama Item:", current_node.nama_item)
                    print("Harga Item:", current_node.harga_item)
                    print("Stok Item:", stok_baru)
                    print("Keterangan:", current_node.keterangan_item)
                    
                    memastikan = input("\nApakah anda yakin bahwa data berikut sudah benar? (Y/N)\n >").upper()
                    if memastikan == "Y":
                        current_node.stok_item = stok_baru
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
                current_node = current_node.next
            else:
                print("""
                    +=============================+
                    |   Produk tidak ditemukan.   |
                    +=============================+
                    """)   
        except ValueError:
            print("""
            !=============================================!
            |     Mohon masukkan sesuiai yang diminta.    |
            +=============================================+
            """) 
    
    # Method Quicksort Stok
    def quicksort_stok(self, head, order):
        if head is None or head.next is None:
            return head

        # Memilih pivot
        pivot = head
        current = head.next
        pivot.next = None  # Pisahkan pivot

        # Inisialisasi list lower dan higher
        left_head = None
        left_tail = None
        right_head = None
        right_tail = None

        while current:
            next_node = current.next
            current.next = None  # Pisahkan node saat ini

            if order == "1":  # Pengurutan secara ascending
                if current.stok_item <= pivot.stok_item:
                    if left_head is None:
                        left_head = current
                        left_tail = current
                    else:
                        left_tail.next = current
                        left_tail = current
                else:
                    if right_head is None:
                        right_head = current
                        right_tail = current
                    else:
                        right_tail.next = current
                        right_tail = current
            else:  # Pengurutan secara descending
                if current.stok_item >= pivot.stok_item:
                    if left_head is None:
                        left_head = current
                        left_tail = current
                    else:
                        left_tail.next = current
                        left_tail = current
                else:
                    if right_head is None:
                        right_head = current
                        right_tail = current
                    else:
                        right_tail.next = current
                        right_tail = current
            current = next_node

        # Untuk mengurutkan bagian secara berulang
        left_head = self.quicksort_stok(left_head, order)
        right_head = self.quicksort_stok(right_head, order)

        # Menggabungkan kedua bagian
        if left_head is None:
            pivot.next = right_head
            return pivot
        else:
            left_tail.next = pivot
            pivot.next = right_head
            return left_head

    def quicksort_harga(self, head, order):
        if head is None or head.next is None:
            return head

        # Memilih pivot
        pivot = head
        head = head.next
        pivot.next = None  # Pisahkan pivot

        # Inisialisasi list lower dan higher
        left_head = None
        left_tail = None
        right_head = None
        right_tail = None
        
        current = head
        while current:
            next_node = current.next
            current.next = None  # Pisahkan node saat ini

            if order == "1":  # Pengurutan secara ascending
                if current.harga_item <= pivot.harga_item:
                    if left_head is None:
                        left_head = current
                        left_tail = current
                    else:
                        current.next = left_head
                        left_head = current
                else:
                    if right_head is None:
                        right_head = current
                        right_tail = current
                    else:
                        right_tail.next = current
                        right_tail = current
            else: # Pengurutan secara descending
                if current.harga_item >= pivot.harga_item:
                    if left_head is None:
                        left_head = current
                        left_tail = current
                    else:
                        left_tail.next = current
                        left_tail = current
                else:
                    if right_head is None:
                        right_head = current
                        right_tail = current
                    else:
                        right_tail.next = current
                        right_tail = current
            current = next_node

        # Secara rekursif mengurutkan sublist lower dan higher
        left_head = self.quicksort_stok(left_head, order)
        right_head = self.quicksort_stok(right_head, order)

        # Menggabungkan kedua bagian
        if left_head is None:
            pivot.next = right_head
            return pivot
        else:
            left_tail.next = pivot
            pivot.next = right_head
            return left_head
    # Method Quicksort Harga
    def quicksort_harga(self, head, order):
        if head is None or head.next is None:
            return head

        # Memilih pivot
        pivot = head
        current = head.next
        pivot.next = None  # Pisahkan pivot

        # Inisialisasi list lower dan higher
        left_head = None
        left_tail = None
        right_head = None
        right_tail = None

        while current:
            next_node = current.next
            current.next = None  # Pisahkan node saat ini

            if order == "1":  # Pengurutan secara ascending
                if current.harga_item <= pivot.harga_item:
                    if left_head is None:
                        left_head = current
                        left_tail = current
                    else:
                        left_tail.next = current
                        left_tail = current
                else:
                    if right_head is None:
                        right_head = current
                        right_tail = current
                    else:
                        right_tail.next = current
                        right_tail = current
            else:  # Pengurutan secara descending
                if current.harga_item >= pivot.harga_item:
                    if left_head is None:
                        left_head = current
                        left_tail = current
                    else:
                        left_tail.next = current
                        left_tail = current
                else:
                    if right_head is None:
                        right_head = current
                        right_tail = current
                    else:
                        right_tail.next = current
                        right_tail = current
            current = next_node

        # Untuk mengurutkan bagian secara berulang
        left_head = self.quicksort_stok(left_head, order)
        right_head = self.quicksort_stok(right_head, order)

        # Menggabungkan kedua bagian
        if left_head is None:
            pivot.next = right_head
            return pivot
        else:
            left_tail.next = pivot
            pivot.next = right_head
            return left_head
        
    # Metode Jumpsearch Kode Barang
    def jumpsearch_kode(self, cari_kode):
        hasil_pencarian = []
        # Apabila node kosong
        if self.head is None: 
            print("List barang kosong.")
            return hasil_pencarian

        # Menghitung panjang node
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next

        jump = int(math.sqrt(length))
        current = self.head

        # Mencari node
        while current is not None:
            if current.kode_item >= cari_kode or current.next is None:  
                break
            for node in range(jump - 1):
                if current.next is None:
                    break
                current = current.next

        # Linear search 
        while current is not None:
            # Apabila ketemu
            if current.kode_item == cari_kode:
                barang_ketemu = NodeProdukPanasonic(current.nama_item, current.kode_item, current.harga_item, current.stok_item, current.keterangan_item)
                hasil_pencarian.append(barang_ketemu)
            current = current.next
        return hasil_pencarian

    # Metode Jumpsearch Nama Barang
    def jumpsearch_nama(self, cari_nama):
        hasil_pencarian = []
        # Apabila node kosong
        if self.head is None: 
            return False

        # Menghitung panjang node
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next

        jump = int(math.sqrt(length))
        current = self.head

        # Mencari node
        while current is not None:
            if current.nama_item >= cari_nama or current.next is None:  
                break
            for node in range(jump - 1):
                if current.next is None:
                    break
                current = current.next

        # Linear search 
        while current is not None:
            # Apabila ketemu
            if current.nama_item == cari_nama:
                barang_ketemu = NodeProdukPanasonic(current.nama_item, current.kode_item, current.harga_item, current.stok_item, current.keterangan_item)
                hasil_pencarian.append(barang_ketemu)
            current = current.next
        return hasil_pencarian



# Class Stack
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, deleted_node):
        if not self.top:
            self.top = deleted_node
        else:
            deleted_node.next = self.top
            self.top = deleted_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped = self.top
            self.top = self.top.next
            self.size -= 1
            return popped

    def peek(self):
        if self.is_empty():
            return None
        return self.top.nama_item



# Function Main Program
def main():
    try: 
        linked_list = SingleLinkedList()
        stack = Stack()
        
        barang1 = NodeProdukPanasonic("Kulkas", "E-12", 90000, 20, "Kulkas Oppenheimer")
        barang2 = NodeProdukPanasonic("TV", "TH-1", 30000, 100, "TV Barbie")
        linked_list.tambah_node_awal(node_baru=barang1)
        linked_list.tambah_node_akhir(node_baru=barang2)

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
                    5. Sorting Produk
                    6. Searching Produk
                    7. Undo {stack.peek()}
                    8. Keluar
                """)

            pilih_menu = input(">")
            if pilih_menu == "1":
                linked_list.menampilkan_produk()
            elif pilih_menu == "2":
                # Inisialisasi node baru
                node_baru = NodeProdukPanasonic("", "", 0, 0, "")
                linked_list.tambah_produk(node_baru, pilih_letak="3", tambah=True)
            elif pilih_menu == "3":
                deleted_node = linked_list.hapus_produk()
                if deleted_node:
                    stack.push(deleted_node)   
            elif pilih_menu == "4":
                linked_list.manajemen_stok()
            elif pilih_menu == "5":
                
                order = input("Pilih urutan \n1. Ascending \n2.Descending \n >")
                if order not in ["1", "2"]:
                    print("Pilihan tidak valid.")
                    continue
                
                atribut = input("Pilih atribut yang diinginkan \n 1. Stok \n 2. Harga \n >")
                # Sorting Stok
                if atribut == "1":
                    linked_list.head = linked_list.quicksort_stok(linked_list.head, order)
                # Sorting Harga
                elif atribut == "2":
                    linked_list.head = linked_list.quicksort_harga(linked_list.head, order)
                else:
                    print("Pilihan tidak valid.")
                    return
                
                # Menampilkan produk setelah pengurutan
                linked_list.menampilkan_produk()
            
            elif pilih_menu == "6":
                
                pilihan_searching = input(
                    "Pilihan searching yang tersedia: \n 1. Kode Barang \n 2. Nama Barang \n >"
                )

                if pilihan_searching == "1":
                    cari_id = input("Masukkan Kode barang yang ingin dicari: ")
                    hasil_pencarian = linked_list.jumpsearch_kode(cari_id)
                elif pilihan_searching == "2":
                    cari_nama = input("Masukkan Nama barang yang ingin dicari: ")  
                    hasil_pencarian = linked_list.jumpsearch_nama(cari_nama)
                else:
                    print("Pilihan tidak ada di daftar menu.")

                # Menampilkan hasil pencarian
                if hasil_pencarian:
                    table = PrettyTable()
                    table.title = "Hasil Pencarian Barang"
                    table.field_names = ["Kode Item", "Nama Item", "Harga Item", "Stok Item", "Keterangan"]

                    for barang in hasil_pencarian:
                        table.add_row([barang.kode_item, barang.nama_item, barang.harga_item, barang.stok_item, barang.keterangan_item])
                    print(table)
                else:
                    print("""
                        +=============================+
                        |   Barang tidak ditemukan.   |
                        +=============================+
                        """)
                    
            elif pilih_menu == "7":
            
                # Undo function
                if not stack.is_empty():
                    undo_barang = stack.pop()
                    if undo_barang:
                        linked_list.tambah_node_awal(undo_barang)
                        print("""
                        +============================+
                        |   Barang berhasil diundo   |
                        +============================+
                        """)
                    else:
                        print("""
                            +===================================+
                            |   Tidak ada barang untuk diundo   |
                            +===================================+
                            """)
                else:
                    print("""
                        +===================================+
                        |   Tidak ada barang untuk diundo   |
                        +===================================+
                        """)
                    
            elif pilih_menu == "8":
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
            |     Mohon masukkan sesuai yang diminta.    |
            +=============================================+
            """)     


# Memanggil function main_program() untuk menjalankan program        
if __name__== "__main__":
    main()



