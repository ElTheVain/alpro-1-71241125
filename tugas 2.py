hargaawallemas = 650000
jumlahgramemas = 25
hargaemas2 = 685000
hargaawallemas = hargaawallemas  * jumlahgramemas
hargaemas2 = hargaemas2 * jumlahgramemas
untungnominal = hargaemas2 - hargaawallemas 
untungpersen = (untungnominal / hargaawallemas ) * 100
print("keuntunganpertama:")
print(f"keuntungandalamrupiah: Rp {untungnominal}")
print(f"keuntungandalampersen:  {untungpersen:.2f}%")
