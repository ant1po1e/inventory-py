from mysql.connector import Error

# =========================
# SUPPLIER
# =========================

def create_supplier(conn, nama, alamat, nomor_telepon):
    try:
        cursor = conn.cursor()

        query = """
        INSERT INTO supplier (nama, alamat, nomor_telepon)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (nama, alamat, nomor_telepon))
        conn.commit()

        print("Supplier berhasil ditambahkan")

    except Error as e:
        print(f"Error: {e}")


def update_supplier(conn, supplier_id, nama, alamat, nomor_telepon):
    try:
        cursor = conn.cursor()

        query = """
        UPDATE supplier
        SET nama=%s,
            alamat=%s,
            nomor_telepon=%s
        WHERE id=%s
        """

        cursor.execute(
            query,
            (nama, alamat, nomor_telepon, supplier_id)
        )

        conn.commit()

        if cursor.rowcount:
            print("Supplier berhasil diupdate")
        else:
            print("Supplier tidak ditemukan")

    except Error as e:
        print(f"Error: {e}")


def delete_supplier(conn, supplier_id):
    try:
        cursor = conn.cursor()

        query = "DELETE FROM supplier WHERE id=%s"

        cursor.execute(query, (supplier_id,))
        conn.commit()

        if cursor.rowcount:
            print("Supplier berhasil dihapus")
        else:
            print("Supplier tidak ditemukan")

    except Error as e:
        print(f"Error: {e}")

# =========================
# KATEGORI
# =========================

def create_kategori(conn, nama):
    try:
        cursor = conn.cursor()

        query = """
        INSERT INTO kategori (nama)
        VALUES (%s)
        """

        cursor.execute(query, (nama,))
        conn.commit()

        print("Kategori berhasil ditambahkan")

    except Error as e:
        print(f"Error: {e}")


def update_kategori(conn, kategori_id, nama):
    try:
        cursor = conn.cursor()

        query = """
        UPDATE kategori
        SET nama=%s
        WHERE id=%s
        """

        cursor.execute(query, (nama, kategori_id))
        conn.commit()

        if cursor.rowcount:
            print("Kategori berhasil diupdate")
        else:
            print("Kategori tidak ditemukan")

    except Error as e:
        print(f"Error: {e}")


def delete_kategori(conn, kategori_id):
    try:
        cursor = conn.cursor()

        query = "DELETE FROM kategori WHERE id=%s"

        cursor.execute(query, (kategori_id,))
        conn.commit()

        if cursor.rowcount:
            print("Kategori berhasil dihapus")
        else:
            print("Kategori tidak ditemukan")

    except Error as e:
        print(f"Error: {e}")

# =========================
# GUDANG
# =========================

def create_gudang(conn, kode, lokasi, kapasitas):
    try:
        cursor = conn.cursor()

        query = """
        INSERT INTO gudang(kode, lokasi, kapasitas)
        VALUES(%s,%s,%s)
        """

        cursor.execute(
            query,
            (kode, lokasi, kapasitas)
        )

        conn.commit()

        print("Gudang berhasil ditambahkan")

    except Error as e:
        print(f"Error: {e}")


def update_gudang(conn, gudang_id, kode, lokasi, kapasitas):
    try:
        cursor = conn.cursor()

        query = """
        UPDATE gudang
        SET kode=%s,
            lokasi=%s,
            kapasitas=%s
        WHERE id=%s
        """

        cursor.execute(
            query,
            (kode, lokasi, kapasitas, gudang_id)
        )

        conn.commit()

        if cursor.rowcount:
            print("Gudang berhasil diupdate")
        else:
            print("Gudang tidak ditemukan")

    except Error as e:
        print(f"Error: {e}")


def delete_gudang(conn, gudang_id):
    try:
        cursor = conn.cursor()

        query = "DELETE FROM gudang WHERE id=%s"

        cursor.execute(query, (gudang_id,))
        conn.commit()

        if cursor.rowcount:
            print("Gudang berhasil dihapus")
        else:
            print("Gudang tidak ditemukan")

    except Error as e:
        print(f"Error: {e}")

# =========================
# USER
# =========================

def create_user(conn, nama, email):
    try:
        cursor = conn.cursor()

        query = """
        INSERT INTO user(nama, email)
        VALUES(%s,%s)
        """

        cursor.execute(query, (nama, email))
        conn.commit()

        print("User berhasil ditambahkan")

    except Error as e:
        print(f"Error: {e}")


def update_user(conn, user_id, nama, email):
    try:
        cursor = conn.cursor()

        query = """
        UPDATE user
        SET nama=%s,
            email=%s
        WHERE id=%s
        """

        cursor.execute(
            query,
            (nama, email, user_id)
        )

        conn.commit()

        if cursor.rowcount:
            print("User berhasil diupdate")
        else:
            print("User tidak ditemukan")

    except Error as e:
        print(f"Error: {e}")


def delete_user(conn, user_id):
    try:
        cursor = conn.cursor()

        query = "DELETE FROM user WHERE id=%s"

        cursor.execute(query, (user_id,))
        conn.commit()

        if cursor.rowcount:
            print("User berhasil dihapus")
        else:
            print("User tidak ditemukan")

    except Error as e:
        print(f"Error: {e}")
        
