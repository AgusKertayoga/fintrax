import sqlite3

def get_db():
    """
    Membuat koneksi ke database SQLite
    """
    conn = sqlite3.connect("fintrax.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Membuat tabel transaksi jika belum ada
    """
    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS transaksi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tanggal TEXT,
        deskripsi TEXT,
        jumlah INTEGER,
        jenis TEXT
    )
    """)

    conn.commit()
    conn.close()