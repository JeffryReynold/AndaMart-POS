"""
    Aplikasi Andamart
    Aplikasi ini menampilkan menu utama seperti pembelian item, memeriksa daftar
    transaksi, mengubah item transaksi, dan menampilkan harga total.

    1. User memasukkan input "Y" jika ingin berbelanja atau "T" jika tidak.
    2. User memasukkan nama item, jumlah, dan harga untuk setiap item yang 
    dibeli.
    3. User memilih untuk melihat daftar transaksi atau tidak.
    4. Jika user memilih untuk melihat daftar transaksi, user dapat memilih 
    untuk mengubah item transaksi.
    5. User dapat memilih untuk menghapus item transaksi, mengubah nama item, 
    mengubah jumlah item, atau mengubah harga item.
    6. Jika user tidak memilih untuk mengubah item transaksi, aplikasi akan 
    menampilkan daftar transaksi dan harga total.
    """

#from transaction import Transaction
print("----------------------------------------------")
print("         Selamat Datang di Andamart           ")
print("----------------------------------------------")

# Input dari user untuk mengetahui apakah mereka akan melakukan transaksi atau tidak.
awal = input("Apakah anda akan berbelanja?(Y/T)")
if awal =='Y' or awal=='y':
    pass
else:
    exit(1)

# Fitur reset transaksi
Transaction.reset_transaction() 
total_price = 0

while True:
    # Input item, Jumlah dan Harga
    item = input("Masukan Nama Item:")
    try:
        jumlah = int(input("Masukan Jumlah Item:"))
    except:
        print('Masukan Anda Salah!')
        exit(1)

    try:
        harga = int(input("Masukan Harga:"))
    except:
        print('Masukan Anda Salah!')
        exit(1)

    # Menghitung total harga
    totalharga = jumlah*harga
    total_price += totalharga
    Transaction(item,jumlah,harga,totalharga)

    # Input user untuk melakukan proses awal transaksi
    X = input('Masukan Data Belanjaan Lagi(Y/T)?')
    if(X=='T' or X=='t'):
        break

# Input user untuk melakukan check transaksi
print('----------------------------------------------')
menu = input('Apakah Anda akan check transaksi?(Y/T)')

if menu == 'y' or menu =='Y':
    
    # Melakukan check order
    Transaction.check_order()
    menu_a = input('Apakah Anda akan merubah item transaksi?(Y/T)')
    if menu_a == 'y' or menu_a=='Y':

        # Print pilihan untuk opsi perubahan transaksi
        print("--------------------------------------------------")
        print(" 1. Hapus Item                                ") 
        print(" 2. Ubah Nama Item                            ")
        print(" 3. Ubah Jumlah Item                          ") 
        print(" 4. Ubah Harga Item                           ")
        print(" 5. Reset Transaksi                           ") 
        print(" Tekan sembarang tombol untuk melihat Total Price ")
        print("--------------------------------------------------")

        menu_b = int(input('Masukan No menu yang akan dilakukan:'))

        # Proses menghapus item yang di pilih
        if menu_b == 1:
            nama_item = input('Masukan Nama Item yang akan dihapus:')
            if nama_item != None:

                try:
                    Transaction.delete_item(nama_item)
                except:
                    pass
            else:
                pass

        # Proses mengubah nama item yang di pilih
        elif menu_b == 2:

            nama_item = input('Masukan Nama Item yang akan diubah:')
            nama_item_baru = input('Masukan Nama Item baru:')
            if nama_item != None and nama_item_baru != None:
                try:
                    Transaction.update_item(nama_item,nama_item_baru)
                except:
                    pass
            else:
                pass

        # Proses mengubah jumlah item yang di pilih
        elif menu_b == 3:
    
            nama_item = input('Masukan Nama Item yang jumlahnya akan diubah:')
            try:
                jumlah_baru = int(input('Masukan jumlah baru:'))
            except:
                print('Masukan Anda Salah!')
                exit(1)

            if nama_item != None and jumlah_baru != None:
                try:
                  Transaction.update_jumlah(nama_item,jumlah_baru)
                except:
                    pass
            else:
                pass

        # Proses mengubah harga item yang di pilih         
        elif menu_b == 4:

            nama_item = input('Masukan Nama Item yang harganya akan diubah:')
            harga_baru = int(input('Masukan harga baru:'))
            if nama_item != None and harga_baru != None:
                try:
                    Transaction.update_harga(nama_item,harga_baru)
                except:
                    pass
            else:
                pass

        # Proses mereset transaksi
        elif menu_b == 5:
            Transaction.reset_transaction()
            print("Berhasil di reset")
        else:
            pass

    else:
        print("Total Price adalah: ", total_price)
