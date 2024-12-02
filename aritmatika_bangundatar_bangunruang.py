import aritmatika
import bangun_datar
import bangun_ruang

def main():
    # Menggunakan modul aritmatika
    print("Operasi Aritmatika:")
    print(f"10 + 5 = {aritmatika.tambah(10, 5)}")
    print(f"10 - 5 = {aritmatika.kurang(10, 5)}")
    print(f"10 * 5 = {aritmatika.kali(10, 5)}")
    print(f"10 ** 5 = {aritmatika.pangkat(10, 5)}")
    print(f"10 / 5 = {aritmatika.bagi(10, 5)}")

    # Menggunakan modul bangun datar
    print("\nBangun Datar:")
    print(f"Luas Persegi (sisi 4) = {bangun_datar.luas_persegi(4)}")
    print(f"Keliling Persegi (sisi 4) = {bangun_datar.keliling_persegi(4)}")
    print(f"Luas Lingkaran (radius 5) = {bangun_datar.luas_lingkaran(5)}")
    print(f"Keliling Lingkaran (radius 5) = {bangun_datar.keliling_lingkaran(5)}")
    print(f"Luas Segitiga (alas 4, tinggi 5) = {bangun_datar.luas_segitiga(4, 5)}")
    print(f"Keliling Segitiga (sisi 4, sisi 5, sisi 6) = {bangun_datar.keliling_segitiga(4, 5, 6)}")
    print(f"Luas Persegi Panjang (panjang 40, lebar 2) = {bangun_datar.luas_persegi_panjang(40, 2)}")
    print(f"Keliling Persegi Panjang(panjang 40, lebar 2) = {bangun_datar.keliling_persegi_panjang(40, 2)}")
    print(f"Luas Jajargenjang (alas 4, tinggi 10) = {bangun_datar.luas_jajar_genjang(4, 10)}")
    print(f"Keliling Jajargenjang (sisi 4, sisi 5) = {bangun_datar.keliling_jajar_genjang(4, 5)}")

    # Menggunakan modul bangun ruang
    print("\nBangun Ruang:")
    print(f"luas permukaan limas segiempat (panjang alas 5, lebar alas 6, tinggi segitiga 6) = {bangun_ruang.luas_permukaan_limas(5, 6, 6)}")
    print(f"Luas Permukaan Kubus (sisi 3) = {bangun_ruang.luas_permukaan_kubus(3)}")
    print(f"Luas Permukaan Balok (panjang 3, lebar 4, tinggi 5) = {bangun_ruang.luas_permukaan_balok(3, 4, 5)}")
    print(f"Luas Permukaan Prisma Segitiga (alas 6, tinggi 6, panjang 6) = {bangun_ruang.luas_permukaan_prisma(6, 6, 6)}")
    print(f"Luas Permukaan Tabung (radius 3, tinggi 7) = {bangun_ruang.luas_permukaan_tabung(3, 7)}")

if __name__ == "__main__":
    main()