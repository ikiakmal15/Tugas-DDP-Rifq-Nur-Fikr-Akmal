import math

# Fungsi untuk menghitung Luas Permukaan Kubus
def luas_permukaan_kubus(sisi):
    # Luas permukaan kubus = 6 * (sisi^2)
    return 6 * (sisi ** 2)

# Fungsi untuk menghitung Luas Permukaan Balok
def luas_permukaan_balok(panjang, lebar, tinggi):
    # Luas permukaan balok = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Fungsi untuk menghitung Luas Permukaan Tabung
def luas_permukaan_tabung(radius, tinggi):
    # Luas permukaan tabung = 2 * pi * radius * (radius + tinggi)
    return 2 * math.pi * radius * (radius + tinggi)

# Fungsi untuk menghitung Luas Permukaan Limas Segiempat
def luas_permukaan_limas(panjang_alas, lebar_alas, tinggi_segitiga):
    # Luas permukaan limas = luas alas + 4 * (luas segitiga samping)
    luas_alas = panjang_alas * lebar_alas
    luas_segitiga_samping = (panjang_alas * tinggi_segitiga) / 2
    return luas_alas + 4 * luas_segitiga_samping

# Fungsi untuk menghitung Luas Permukaan Prisma Segitiga
def luas_permukaan_prisma(alas, tinggi, panjang):
    # Luas permukaan prisma = 2 * luas alas + keliling alas * panjang
    luas_alas = (alas * tinggi) / 2
    # Misalkan alas segitiga memiliki panjang sisi alas = 'alas', dan tinggi segitiga = 'tinggi'
    keliling_alas = 3 * alas  # Jika segitiga sama sisi, keliling = 3 * sisi
    return 2 * luas_alas + keliling_alas * panjang
