from datetime import datetime

tahunSekarang = datetime.now().year

nama = input("Masukkan nama Anda: ")
tahunLahir = int(input("Masukkan tahun lahir Anda: "))

umur = tahunSekarang - tahunLahir

print(f"Halo, {nama}! Anda berusia {umur} tahun.")
