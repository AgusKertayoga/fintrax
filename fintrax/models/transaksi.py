from abc import ABC, abstractmethod

class Transaksi(ABC):
    """
    Abstract class transaksi
    """

    def __init__(self, tanggal, deskripsi, jumlah):
        self.tanggal = tanggal
        self.deskripsi = deskripsi
        self.jumlah = jumlah

    @abstractmethod
    def jenis(self):
        pass


class Pemasukan(Transaksi):

    def jenis(self):
        return "pemasukan"


class Pengeluaran(Transaksi):

    def jenis(self):
        return "pengeluaran"