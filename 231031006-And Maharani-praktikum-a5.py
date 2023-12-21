
#a= True
#while a:
#print ('menjalankan program')

#kode diatas menggunakan loop while untuk mencetak
#teks'menjalankan program' terus menerus selama variabel a bernilai true.
#ini berarti program akan terus berjalan tanpa henti
#mencetak teks tersebut secara berulang

#untuk membatasi jumlah pencetakan menjadi 5 kali, kita
#dapat menggunakan variabel hitung yang akan bertambah setiap kali teks dicetal
#ketika hitung mencapai 5, kita dapat mengubah nilai  variabel a menjadi false untuk menghentikan loop



a= True
hitung = 0
while a:
    print('menjalankan program')
    hitung += 1
    if hitung == 5:
        a = False

