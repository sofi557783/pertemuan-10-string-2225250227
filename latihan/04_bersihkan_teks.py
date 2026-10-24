# Latihan 4: Membersihkan Teks
# Input: Teks dengan spasi ganda dan spasi berlebih
# Proses: Menghapus spasi luar, mengganti spasi ganda dengan spasi tunggal, dan mengubah huruf pertama jadi kapital
# Output: Teks yang sudah bersih dan rapi

teks = "  ihsg  runtuh  karna  indonesia  tidak  takut  msci  "
teks = teks.strip()
while "  " in teks:
    teks = teks.replace("  ", " ")
print(teks.capitalize())