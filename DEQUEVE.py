#NIM : TI20230017
#NAMA: LALU
#simulasi parkir kendaraan bermotor
class parkir:
    def _init_(self):
        self.kendaraan = deque()

    def masuk(self, jenis, waktu_masuk):
        self.kendaraan.append((jenis, waktu_masuk))
 
    def keluar(self, waktu_masuk):
        jenis, waktu_masuk = self.kendaraan.popleft()
        lama = waktu_keluar - waktu_masuk
        if jenis == 'mobil':
            biaya = 5000 if lama <= 2 else 5000 + (lama - 2) * 3000
        else: #motor
            biaya = 3000 if lama <= 2 else 3000 + (lama - 2) * 2000
            return jenis, lama, biaya,

            parkir = parkir()
            parkir.masuk('mobiil', 8)
            print(parkir.keluar(10))
            parkir.masuk('motor', 9)
            print(parkir.keluar(15))