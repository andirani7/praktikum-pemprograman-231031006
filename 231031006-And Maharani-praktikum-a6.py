#a = True
#while a:
#pilih = input('pilihan: ')
#if pilih == 'ya':
#print('Selamat Datang')
#elif pilih == 'tidak':
#print('Sampai Jumpa')
#break

#Penjelasan kode di atas:
#1. Variabel a diinisialisasi dengan nilai True. Ini akan digunakan sebagai kondisi untuk menjalankan loop while.
#2. Loop while akan terus berjalan selama nilai a adalah True.
#3. Pada setiap iterasi loop, program akan meminta input dari pengguna dengan menggunakan fungsi input() dan menyimpannya dalam variabel pilih.
#4. Jika nilai pilih adalah 'ya', program akan mencetak 'Selamat Datang'.
#5. Jika nilai pilih adalah 'tidak', program akan mencetak 'Sampai Jumpa' dan menghentikan loop dengan menggunakan pernyataan break.
#6. Jika nilai pilih tidak sama dengan 'ya' atau 'tidak', program akan tetap berjalan tanpa melakukan apa pun

a=True
while a:
 pilih = input ('pilihan')
 if pilih == 'ya':
     print ('selamat datang')
 elif pilih == 'tidak':
     print ('sampai jumpa')
     break
 else:
     print ('pilihan tidak valid. masukkan pilihan yang benar.')
