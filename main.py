import mysql.connector
from mysql.connector import Error
from L200250256 import *

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
        print(f"Error: {e}")
        return None

def menu_master(conn):

    while True:
        print("\n===== DATA MASTER =====")
        print("1. Supplier")
        print("2. Kategori")
        print("3. Gudang")
        print("4. User")
        print("0. Kembali")

        pilih = input("Pilih: ")

        if pilih == "1":
            nama = input("Nama Supplier : ")
            alamat = input("Alamat : ")
            telp = input("No Telp : ")

            create_supplier(conn, nama, alamat, telp)

        elif pilih == "2":
            nama = input("Nama Kategori : ")

            create_kategori(conn, nama)

        elif pilih == "3":
            kode = input("Kode Gudang : ")
            lokasi = input("Lokasi : ")
            kapasitas = int(input("Kapasitas : "))

            create_gudang(conn, kode, lokasi, kapasitas)

        elif pilih == "4":
            nama = input("Nama User : ")
            email = input("Email : ")

            create_user(conn, nama, email)

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid")

def main():
    conn = create_connection()
    if not conn: return

    while True:
        print("\n===== APLIKASI INVENTARIS KELOMPOK D5 =====")
        print("1. Tabel Master")
        print("2. Transaksi")
        print("3. Data Query")
        print("4. Join  ")
        print("5. Keluar")

        pilihan = input("Pilih Menu : ")

        if pilihan == "1":
            menu_master(conn)

        elif pilihan == "5":
            break
    conn.close()

if __name__ == "__main__":
    main()