import mysql.connector
from mysql.connector import Error

from L200250256 import *
from L200250257 import *

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='gudang'
        )
        return connection

    except Error as e:
        print(f"Error : {e}")
        return None


# ==========================
# MENU SUPPLIER
# ==========================

def menu_supplier(conn):

    while True:

        print("\n===== MENU SUPPLIER =====")
        print("1. Tambah Supplier")
        print("2. Update Supplier")
        print("3. Hapus Supplier")
        print("0. Kembali")

        pilih = input("Pilih : ")

        if pilih == "1":

            nama = input("Nama Supplier : ")
            alamat = input("Alamat : ")
            telp = input("No Telepon : ")

            create_supplier(
                conn,
                nama,
                alamat,
                telp
            )

        elif pilih == "2":

            supplier_id = int(input("ID Supplier : "))
            nama = input("Nama Baru : ")
            alamat = input("Alamat Baru : ")
            telp = input("No Telepon Baru : ")

            update_supplier(
                conn,
                supplier_id,
                nama,
                alamat,
                telp
            )

        elif pilih == "3":

            supplier_id = int(input("ID Supplier : "))

            delete_supplier(
                conn,
                supplier_id
            )

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid")


# ==========================
# MENU KATEGORI
# ==========================

def menu_kategori(conn):

    while True:

        print("\n===== MENU KATEGORI =====")
        print("1. Tambah Kategori")
        print("2. Update Kategori")
        print("3. Hapus Kategori")
        print("0. Kembali")

        pilih = input("Pilih : ")

        if pilih == "1":

            nama = input("Nama Kategori : ")

            create_kategori(
                conn,
                nama
            )

        elif pilih == "2":

            kategori_id = int(input("ID Kategori : "))
            nama = input("Nama Baru : ")

            update_kategori(
                conn,
                kategori_id,
                nama
            )

        elif pilih == "3":

            kategori_id = int(input("ID Kategori : ")

            )

            delete_kategori(
                conn,
                kategori_id
            )

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid")


# ==========================
# MENU GUDANG
# ==========================

def menu_gudang(conn):

    while True:

        print("\n===== MENU GUDANG =====")
        print("1. Tambah Gudang")
        print("2. Update Gudang")
        print("3. Hapus Gudang")
        print("0. Kembali")

        pilih = input("Pilih : ")

        if pilih == "1":

            kode = input("Kode Gudang : ")
            lokasi = input("Lokasi : ")
            kapasitas = int(input("Kapasitas : "))

            create_gudang(
                conn,
                kode,
                lokasi,
                kapasitas
            )

        elif pilih == "2":

            gudang_id = int(input("ID Gudang : "))

            kode = input("Kode Baru : ")
            lokasi = input("Lokasi Baru : ")
            kapasitas = int(input("Kapasitas Baru : "))

            update_gudang(
                conn,
                gudang_id,
                kode,
                lokasi,
                kapasitas
            )

        elif pilih == "3":

            gudang_id = int(input("ID Gudang : "))

            delete_gudang(
                conn,
                gudang_id
            )

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid")


# ==========================
# MENU USER
# ==========================

def menu_user(conn):

    while True:

        print("\n===== MENU USER =====")
        print("1. Tambah User")
        print("2. Update User")
        print("3. Hapus User")
        print("0. Kembali")

        pilih = input("Pilih : ")

        if pilih == "1":

            nama = input("Nama User : ")
            email = input("Email : ")

            create_user(
                conn,
                nama,
                email
            )

        elif pilih == "2":

            user_id = int(input("ID User : "))
            nama = input("Nama Baru : ")
            email = input("Email Baru : ")

            update_user(
                conn,
                user_id,
                nama,
                email
            )

        elif pilih == "3":

            user_id = int(input("ID User : "))

            delete_user(
                conn,
                user_id
            )

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid")


# ==========================
# MENU MASTER
# ==========================

def menu_master(conn):

    while True:

        print("\n===== DATA MASTER =====")
        print("1. Supplier")
        print("2. Kategori")
        print("3. Gudang")
        print("4. User")
        print("0. Kembali")

        pilih = input("Pilih : ")

        if pilih == "1":
            menu_supplier(conn)

        elif pilih == "2":
            menu_kategori(conn)

        elif pilih == "3":
            menu_gudang(conn)

        elif pilih == "4":
            menu_user(conn)

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid")


# ==========================
# MENU JOIN
# ==========================

def menu_join(conn):

    while True:

        print("\n===== MENU JOIN =====")
        print("1. Barang - Kategori - Gudang")
        print("2. User Mengeluarkan Barang")
        print("0. Kembali")

        pilih = input("Pilih : ")

        if pilih == "1":
            tampil_barang_kategori_gudang(conn)

        elif pilih == "2":
            tampil_user_mengeluarkan(conn)

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid")

# ==========================
# MAIN PROGRAM
# ==========================

def main():

    conn = create_connection()

    if not conn:
        return

    while True:

        print("\n===================================")
        print(" APLIKASI INVENTARIS KELOMPOK D5 ")
        print("===================================")
        print("1. Tabel Master")
        print("2. Transaksi")
        print("3. Data Query")
        print("4. Join")
        print("0. Keluar")

        pilihan = input("Pilih Menu : ")

        if pilihan == "1":
            menu_master(conn)

        elif pilihan == "2":
            print("Menu Transaksi belum dibuat")

        elif pilihan == "3":
            print("Menu Query belum dibuat")

        elif pilihan == "4":
            menu_join(conn)

        elif pilihan == "0":
            print("Terima kasih")
            break

        else:
            print("Pilihan tidak valid")

    conn.close()


if __name__ == "__main__":
    main()