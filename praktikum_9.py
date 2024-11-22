print()
print('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    konversi=(celcius*9/5)+32
    return konversi


print(celcius_ke_fahrenheit(0)) #32
print(celcius_ke_fahrenheit(100))

print()
print('## Nomor2 ##')
def ganjil_genap(bilangan):
    penentu=bilangan %2 == 0
    return penentu

print(ganjil_genap(4)) #True
print(ganjil_genap(7)) #True

print()
print('## Nomor3 ##')
def nilai(keterangan):
    if keterangan >= 80:
        print("Lulus")
    elif keterangan <= 60:
        print("Gagal")
    else:
        print("tidal valid")

nilai(80)
nilai(60)

print()
print('## nomor4 ##')
def bilangan_ganjil(trilala):
    return[i for i in range(1,trilala,2)]
print(bilangan_ganjil(20))