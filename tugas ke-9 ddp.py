# print()
# print('## Nomor 1 ##')
# def celcius_ke_fahrenheit(celcius):
#     konversi=(celcius*9/5)+32
#     return konversi

# print(celcius_ke_fahrenheit(0))
# print(celcius_ke_fahrenheit(100))

# print()
# print('## Nomor 2 ##')
# def ganjil_genap(bilangan):
#     penentu= bilangan % 2 == 0
#     return penentu

# print(ganjil_genap(4))
# print(ganjil_genap(7))

#nomor 3
print()
def nilai(keterangan):
    if keterangan >= 80:
        print('Lulus')
    elif keterangan <= 60:
        print('Tidak Lulus')
    else:
        print('Tidak valid')
    
    nilai(80)
    nilai(60)
    
# print()
# print('## Nomor 4 ##')
# def bilangan_ganjil(cihuy):
#     return[i for i in range(1,cihuy,2)]
# print(bilangan_ganjil(30))