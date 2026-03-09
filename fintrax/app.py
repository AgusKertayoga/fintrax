from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
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


init_db()


@app.route("/")
def index():

    conn = get_db()

    transaksi = conn.execute(
        "SELECT * FROM transaksi ORDER BY tanggal DESC"
    ).fetchall()

    total_pemasukan = conn.execute(
        "SELECT SUM(jumlah) FROM transaksi WHERE jenis='pemasukan'"
    ).fetchone()[0] or 0

    total_pengeluaran = conn.execute(
        "SELECT SUM(jumlah) FROM transaksi WHERE jenis='pengeluaran'"
    ).fetchone()[0] or 0

    saldo = total_pemasukan - total_pengeluaran

    conn.close()

    return render_template(
        "index.html",
        transaksi=transaksi,
        pemasukan=total_pemasukan,
        pengeluaran=total_pengeluaran,
        saldo=saldo
    )


@app.route("/tambah", methods=["POST"])
def tambah():

    tanggal = request.form["tanggal"]
    deskripsi = request.form["deskripsi"]
    jumlah = request.form["jumlah"]
    jenis = request.form["jenis"]

    conn = get_db()

    conn.execute(
        "INSERT INTO transaksi (tanggal,deskripsi,jumlah,jenis) VALUES (?,?,?,?)",
        (tanggal, deskripsi, jumlah, jenis)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM transaksi WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)