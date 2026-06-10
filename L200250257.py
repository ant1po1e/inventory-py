def tampil_barang_kategori_gudang(conn):
    cursor = conn.cursor()

    sql = """
    SELECT b.id,
           b.nama,
           k.nama,
           g.kode,
           g.lokasi,
           b.jumlah,
           b.harga
    FROM barang b
    JOIN kategori k
        ON b.id_kategori = k.id
    JOIN gudang g
        ON b.id_gudang = g.id
    """

    cursor.execute(sql)
    data = cursor.fetchall()

    print("\n===================================================================================================")
    print("| ID | Nama Barang          | Kategori           | Gudang | Lokasi         | Jumlah | Harga      |")
    print("===================================================================================================")

    for row in data:
        print(
            f"| {row[0]:<2} "
            f"| {row[1]:<20} "
            f"| {row[2]:<18} "
            f"| {row[3]:<6} "
            f"| {row[4]:<14} "
            f"| {row[5]:<6} "
            f"| {row[6]:<10} |"
        )

    print("===================================================================================================")

    cursor.close()
    
def tampil_user_mengeluarkan(conn):
    cursor = conn.cursor()

    sql = """
    SELECT u.id,
           u.nama,
           m.tanggal_keluar,
           m.jumlah
    FROM user u
    JOIN mengeluarkan m
        ON u.id = m.id_user
    """

    cursor.execute(sql)
    data = cursor.fetchall()

    print("\n------------------------------------------------------------")
    print("| ID User | Nama User            | Tgl Keluar     | Jumlah |")
    print("------------------------------------------------------------")

    for row in data:
        print(f"| {row[0]:<7} | {row[1]:<20} | {str(row[2]):<14} | {row[3]:<6} |")

    print("------------------------------------------------------------")

    cursor.close()