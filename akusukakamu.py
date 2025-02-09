import math
jumlahdeposito = 400
jumlahuang = 200
bungatahunan = 0.10
waktu = math.log(jumlahdeposito / jumlahuang) / math.log(1 + bungatahunan)
print("waktu yang dibutuhkan:", round(waktu, 3), "tahun")
