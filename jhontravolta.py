''' TUGAS SQA KELOMPOK 12
Anggita Maharani 11190910000080
Yandi Sabjaya 11190910000079 '''

jam = int(input('Masukan jam kerja anda: '))
if jam < 40:
	gaji = jam * 15000
else:
	gaji = 40 * 15000 + (jam - 40) * 22500
print('gaji anda', gaji)

pengeluaran = int(input('Masukan pengeluaran anda: '))
if pengeluaran < gaji:
	print('Bisa menagbung')
elif pengeluaran == gaji:
	print('Tidak bisa menabung')
else:
	print('Cari tambahan')