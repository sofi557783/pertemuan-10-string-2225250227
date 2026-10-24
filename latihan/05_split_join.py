# Latihan 5: Split dan Join
# Input: Kalimat string
# Proses: Memecah kalimat menjadi list kata dan menggabungkannya kembali dengan tanda hubung
# Output: List kata dan string terhubung tanda dash (-)

kalimat = "hai antek antek asing"
kata = kalimat.split()
print(kata)
print("-".join(kata))