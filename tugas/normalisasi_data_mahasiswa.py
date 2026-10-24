# Tugas 4: Normalisasi Data Mahasiswa

def normalisasi_nama(nama):
    # Menghapus spasi berlebih dan mengubah ke format Title Case
    return nama.strip().title()

def buat_inisial(nama):
    # Mengambil huruf pertama dari setiap kata dalam nama
    kata_list = nama.split()
    inisial = "".join([k[0].upper() for k in kata_list])
    return inisial

def normalisasi_kode(kode):
    # Mengubah ke uppercase, split spasi, lalu join dengan tanda hubung (-)
    kata_kode = kode.strip().upper().split()
    return "-".join(kata_kode)

# Input data
nama_input = input("Nama: ")
kode_input = input("Kode kelas: ")

# Proses normalisasi
nama_bersih = normalisasi_nama(nama_input)
kode_bersih = normalisasi_kode(kode_input)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama_bersih)

# Tampilkan hasil normalisasi
print(f"Nama bersih : {nama_bersih}")
print(f"Kode kelas  : {kode_bersih}")
print(f"Jumlah kata : {jumlah_kata}")
print(f"Inisial     : {inisial}")