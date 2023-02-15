no_tlp = (input('masukan nomor telepon :'))

angka_akhir = int(no_tlp[-1])
if angka_akhir % 2 == 0:
    bilangan = 'genap'

else:
    bilangan = 'ganjil'

print('nomor akhir anda', bilangan)
