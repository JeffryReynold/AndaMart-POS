# Import library yang akan digunakan
global dataf, pd, np
import pandas as pd
import numpy as np

"""
    Transaction class yang menyimpan data belanja seorang customer.
    
    Attributes:
        item_list (list): list item barang yang dibeli oleh customer.
        item_jumlah (list): jumlah item barang yang dibeli oleh customer.
        item_harga (list): harga item barang yang dibeli oleh customer.
        item_total (list): total harga item barang yang dibeli oleh customer.
    
    Methods:
        __init__: Method yang dipanggil saat membuat objek baru dari class 
        Transaction. Menambahkan data baru yang berisi nama, jumlah, harga, 
        dan total harga barang yang dibeli.
        reset_transaction: Method yang menghapus semua item dari list item_list.
        check_order: Method yang menampilkan data belanja dalam bentuk tabel.
        update_item: Method yang mengubah nama item barang.
        update_jumlah: Method yang mengubah jumlah item barang.
        update_harga: Method yang mengubah harga item barang.
        delete_item: Method yang menghapus item barang dari list item_list.
        total_price: Method yang menghitung dan menampilkan total harga belanja.
    """
# Membuat Class Transaction   
class Transaction():
    item_list = []
    item_jumlah =[]
    item_harga = []
    item_total = []

    # Inisialisasi objek transaksi baru
    # dengan nama barang, jumlah, harga, dan total harga
    def __init__(self, nama, jumlah, harga, totalharga):
        Transaction.item_list.append(nama)
        Transaction.item_jumlah.append(jumlah)
        Transaction.item_harga.append(harga)
        Transaction.item_total.append(totalharga)

    # Fungsi untuk mereset daftar transaksi
    def reset_transaction():
        Transaction.item_list.clear()

    # Fungsi untuk menampilkan daftar transaksi        
    def check_order():
        print("")
        print("----------------------------------------------")
        # Menggunakan pandas untuk membuat DataFrame dari daftar transaksi
        dataf = pd.DataFrame(
            list(zip(Transaction.item_list,Transaction.item_jumlah,
                     Transaction.item_harga,Transaction.item_total)),
                     columns=['Item','Jumlah','Harga/Item','Harga Total'])
        print(dataf)

    # Fungsi untuk mengubah nama item pada daftar transaksi
    def update_item(namaitem,namabaru):

        # Menggunakan pandas untuk membuat DataFrame dari daftar transaksi
        dataf = pd.DataFrame(
            list(zip(Transaction.item_list,Transaction.item_jumlah,
                     Transaction.item_harga,Transaction.item_total)),
                     columns=['Item','Jumlah','Harga/Item','Harga Total'])
        
        # Menggunakan np.where untuk mengubah nama item pada daftar transaksi
        dataf['Item']=np.where(dataf['Item'] == namaitem,namabaru,dataf['Item'])
        print(dataf)

    # Fungsi untuk mengubah jumlah item pada daftar transaksi
    def update_jumlah(namaitem,jumlahbaru):

        # Menggunakan pandas untuk membuat DataFrame dari daftar transaksi        
        dataf = pd.DataFrame(
            list(zip(Transaction.item_list,Transaction.item_jumlah,
                     Transaction.item_harga,Transaction.item_total)),
                     columns=['Item','Jumlah','Harga/Item','Harga Total'])
        
        # Menggunakan np.where untuk mengubah jumlah item pada daftar transaksi
        dataf['Jumlah']=np.where(dataf['Item'] == namaitem,int(jumlahbaru),
                      dataf['Jumlah'])
        
        # Menghitung harga total setelah jumlah item diubah
        dataf['Harga Total']=dataf['Jumlah']*dataf['Harga/Item'] 
        print(dataf)

    # Fungsi untuk mengubah harga item pada daftar transaksi
    def update_harga(namaitem,hargabaru):
        
         # Menggunakan pandas untuk membuat DataFrame dari daftar transaksi
        dataf = pd.DataFrame(
            list(zip(Transaction.item_list,Transaction.item_jumlah,
                     Transaction.item_harga,Transaction.item_total)),
                     columns=['Item','Jumlah','Harga/Item','Harga Total'])
        
        # Menggunakan np.where untuk mengubah harga item pada daftar transaksi
        dataf['Harga/Item']=np.where(dataf['Item'] == namaitem,int(hargabaru),
                     dataf['Harga/Item'])
        
        # Menghitung harga total setelah harga item diubah
        dataf['Harga Total']=dataf['Jumlah']*dataf['Harga/Item'] 
        print(dataf)

    # Fungsi untuk menghapus item dari data transaksi
    def delete_item(namaitem):

         # membuat dataframe dari data transaksi  
        dataf = pd.DataFrame(
            list(zip(Transaction.item_list,Transaction.item_jumlah,
                     Transaction.item_harga,Transaction.item_total)),
                     columns=['Item','Jumlah','Harga/Item','Harga Total'])
        
        # mencari index dari item yang ingin dihapus
        indexItem = dataf[dataf['Item']==namaitem].index

        # menghapus item dari dataframe
        dataf.drop(indexItem,inplace=True)

        # mencetak hasil dataframe setelah item dihapus
        print(dataf)

    # Fungsi untuk menghitung total harga dan diskon
    def total_price():
            
            # membuat dataframe dari data transaksi
            dataf = pd.DataFrame(
                list(zip(Transaction.item_list,Transaction.item_jumlah,
                         Transaction.item_harga,Transaction.item_total)),
                         columns=['Item','Jumlah','Harga/Item','Harga Total'])
            
            # menghitung total harga
            totalprice = dataf['Harga Total'].sum()
            
            # menentukan diskon berdasarkan total harga
            if (200000<= totalprice <300000):
                netprice = totalprice-(totalprice*0.05)
            elif(300000 <= totalprice <500000):
                netprice = totalprice-(totalprice*0.08)
            elif(totalprice >=500000 ):
                netprice = totalprice-(totalprice*0.10)
            else:
                netprice = totalprice

            # mencetak hasil total harga setelah diskon
            print("==============================================")
            print('  Total Price (Rp): ',netprice)
            print("----------------------------------------------")
            print("  Terima Kasih Telah Berbelanja di Andamart   ")
            print("----------------------------------------------")
