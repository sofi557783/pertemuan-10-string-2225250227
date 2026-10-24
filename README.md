# Pertemuan 10 - String dan Pengolahan Teks

Nama: Sofi Silvia Putri
NIM: 2225250227
Kelas: 3E

## Tujuan
Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan
python tugas/normalisasi_data_mahasiswa.py

## Algoritma
1. Membaca input teks nama dan kode kelas dari pengguna.
2. Menghapus spasi berlebih di awal dan akhir string menggunakan `strip()`.
3. Mengubah format nama menjadi Title Case menggunakan `title()`.
4. Mengubah kode kelas menjadi huruf kapital menggunakan `upper()`, lalu memisahkan kata-katanya dan menggabungkan kembali dengan tanda hubung (`-`).
5. Menghitung jumlah kata pada nama menggunakan `split()` dan `len()`.
6. Membuat inisial nama dengan mengambil karakter pertama dari setiap kata.
7. Menampilkan hasil normalisasi ke layar.

## Test Case
- Input Nama: `aam hendrayana`, Kode: `pmat a 2026` -> Output: `Aam Hendrayana | PMAT-A-2026 | AH` (Status: Sesuai)
- Input Nama: `fATHIYYAH mUTHMAINNAH`, Kode: `kelas b` -> Output: `Fathiyyah Muthmainnah | KELAS-B | FM` (Status: Sesuai)
- Input Nama: `BUDI`, Kode: `pmtk 01` -> Output: `Budi | PMTK-01 | B` (Status: Sesuai)

## Refleksi
Saya memahami bahwa sifat string di Python bersifat case-sensitive dan immutable. Salah satu masalah yang ditemukan adalah perbedaan hasil pencarian akibat variasi huruf besar dan kecil, yang berhasil diperbaiki dengan melakukan normalisasi teks menjadi huruf kecil terlebih dahulu (`lower()`).

## Kuis Formatif
1. **Apa perbedaan string dan list pada Python?**
   String adalah kumpulan karakter yang bersifat *immutable* (tidak dapat diubah elemennya setelah dibuat), sedangkan list adalah kumpulan elemen (bisa berbagai tipe data) yang bersifat *mutable* (elemennya dapat diubah, ditambah, atau dihapus).

2. **Mengapa string disebut immutable?**
   Karena nilai karakter di dalam string tidak dapat diubah secara langsung setelah string tersebut dibuat.

3. **Apa hasil dari 'Python'[1:4]?**
   `'yth'`

4. **Apa fungsi strip()?**
   Untuk menghapus karakter spasi (atau karakter khusus lain) di awal dan di akhir string.

5. **Kapan lower() lebih tepat daripada title()?**
   Saat ingin melakukan pembandingan teks atau pencarian kata kunci (*case-insensitive search*) agar penulisan huruf tidak memengaruhi hasil.

6. **Apa perbedaan split() dan join()?**
   `split()` memecah sebuah string menjadi list kata berdasarkan pemisah tertentu, sedangkan `join()` menggabungkan elemen-elemen list string menjadi satu string utuh dengan pemisah tertentu.

7. **Bagaimana memeriksa apakah kata 'data' terdapat dalam suatu string?**
   Menggunakan operator `in`, contohnya: `'data' in teks`.

8. **Apa arti hasil -1 dari find()?**
   Menandakan bahwa substring atau kata yang dicari tidak ditemukan di dalam string tersebut.

9. **Mengapa normalisasi teks perlu dilakukan sebelum perbandingan?**
   Agar format teks menjadi seragam (misal: sama-sama huruf kecil dan tanpa spasi berlebih) sehingga proses perbandingan data memberikan hasil yang akurat.

10. **Perintah apa yang digunakan untuk mengirim commit ke GitHub?**
    `git push` (atau `git push origin main`).