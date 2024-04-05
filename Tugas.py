print("====================================")
print("|  SILAHKAN ISI DATA DI BAWAH INI  |")
print("====================================")

nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM Anda: ")
prodi = input("Masukkan program studi Anda: ")
absen=int(input("input jumlah absen:"))
uts=int(input("input nilai uts:"))
uas=int(input("input nilai uas:"))
jumlah = absen + uts + uas
rata=jumlah/3
nilai=100
print("___________________________________")
print(" Nama                      :", nama)
print(" NIM                       :", nim)
print(" Program Studi             :", prodi)
print(" Nilai absen anda          :", absen)
print(" Nilai uts anda            :", uts)
print(" Nilai uas anda            :", uas)
print(" Jumlah nilai keseluruhan  :", jumlah)
print(" jumlah nilai rata-rata    :", rata)
print("KETERANGAN : ")

if rata >= 85 and rata <= 100:
    print("NILAI ANDA ADALAH A")
elif rata >= 75 and rata <= 84:
    print("NILAI ANDA ADALAH B")
elif rata >= 65 and rata <= 74:
    print("NILAI ANDA ADALAH C")
elif rata >= 50 and rata <= 64:
    print("NILAI ANDA ADALAH D")
elif rata <= 49 and rata >= 0:
    print("NILAI ANDA ADALAH B")
else:
    print("Nilai anda tidak terdaftar")
