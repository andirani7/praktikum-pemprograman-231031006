'''UTS
1. Buat variabel jenis list berikut.
    
    BIO =  ['Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir'
            'aktif'
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil'
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']

#(NOTED: sesuaikan dengan data anda)
            
2. Buat variabel jenis nested list berikut.

MK =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [2,3,3,2,3,3,3,2],
        ['Selasa','Senin','Rabu','Senin','Kamis','Kamis','Kamis','Kamis'],
        ['07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10']]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, waktu kuliah, dan jadwal)
        
3. Susun Kode dengan hasil runing seperti berikut.
           
            
             INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                             JURUSAN SAINS
                    KARTU RENCANA STUDI MAHASISWA
                           GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : 60022010
Program/prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023 Ganjil
Status          : Aktif
|--|--  10  --|--           26         --|--5--|-- 8  --|--    13   --|
-----------------------------------------------------------------------
No. Kode      |      Mata Kuliah         | SKS |  Hari  |    Jadwal   |
-----------------------------------------------------------------------
1   22A1209   | Matkul1                  |  2  | Senin  |  07.30-09.10|
2   22A1210   | Matkul2                  |  3  | Selasa |  07.30-09.10|
3   22A1211   | Matkul3                  |  3  | Rabu   |  07.30-09.10|
4   22A1212   | Matkul4                  |  2  | Senin  |  07.30-09.10|
5   22A1213   | Matkul5                  |  3  | Kamis  |  07.30-09.10|
6   22A1214   | Matkul6                  |  3  | Kamis  |  07.30-09.10|
7   22A1215   | Matkul7                  |  3  | Kamis  |  07.30-09.10|
8   22A1216   | Matkul8                  |  2  | Kamis  |  07.30-09.10|
-----------------------------------------------------------------------
                        TOTAL SKS           21                        |
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah       : 8
Jumlah Mata Kuliah 2 SKS : 3 Mata Kuliah
Jumlah Mata Kuliah 3 SKS : 5 Mata kuliah
Mata Kuliah hari Senin   : 2 Mata Kuliah
Mata Kuliah hari Selasa  : 1 Mata Kuliah
Mata Kuliah hari Rabu    : 1 Mata Kuliah
Mata Kuliah hari Kamis   : 1 Mata Kuliah
Mata Kuliah hari Jumat   : 0 Mata Kuliah
                                              Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''


# Tulis Kode Jawaban di bawah!

bio =  ['Andi Maharani',
        '231031006',
        '07 April 2005',
        'aktif',
        'S1',
        'Sistem Informasi A',
        '2023-2024',
        'ganjil',
        'Institut Teknologi Bacharuddin Jusuf Habibie',
        'Parepare',
        'Jurusan Sains',
        'kartu rencana studi mahasiswa']

MK =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['pemprograman','kalkulus','sains terpadu','bahasa','PTI','cinta','pancasila','agama islam'],
        [3,3,3,2,3,2,2,2],
        ['Selasa','Selasa','Rabu','Kamis','Kamis','Kamis','Jumat','Jumat'],
        ['07.30-09.10','13.30-15.10','13.30-15.10','07.30-09.10','13.30-15.10','15.20-17.00','09.20-11.00','13.30-15.10']]

print(bio[-4].upper().center(71))
print(bio[-2].upper().center(71))
print(bio[-1].upper().center(71))
strr = bio[-5]+' '+bio[-6].replace('-','/')
print(strr.upper().center(71))

print(f'''
Nama Lengkap    : {bio[0].upper()}
NIM             : {bio[1]}
Program/prodi   : {bio[3]}/{bio[4]}
Tahun Masuk     : {bio[5][:4]} {bio[6].title()}
Status          : {bio[3]}''')

print('-'*67)
print('No.  Kode'.ljust(10)+'|'+'Mata Kuliah'.center(26)+'|'+'SKS'.center(5)+'|'+'Hari'.center(8)+'|'+'Jadwal'.center(13)+'|')
print('-'*67)
print(f'1. {MK[0][0]}'.ljust(10)+'|'+f'{MK[1][0]}'.center(26)+'|'+f'{MK[2][0]}'.center(5)+'|'+f'{MK[3][0]}'.center(8)+'|'+f'{MK[4][0]}'.center(13)+'|')
print(f'2. {MK[0][1]}'.ljust(10)+'|'+f'{MK[1][1]}'.center(26)+'|'+f'{MK[2][1]}'.center(5)+'|'+f'{MK[3][1]}'.center(8)+'|'+f'{MK[4][1]}'.center(13)+'|')
print(f'3. {MK[0][2]}'.ljust(10)+'|'+f'{MK[1][2]}'.center(26)+'|'+f'{MK[2][2]}'.center(5)+'|'+f'{MK[3][2]}'.center(8)+'|'+f'{MK[4][2]}'.center(13)+'|')
print(f'4. {MK[0][3]}'.ljust(10)+'|'+f'{MK[1][3]}'.center(26)+'|'+f'{MK[2][3]}'.center(5)+'|'+f'{MK[3][3]}'.center(8)+'|'+f'{MK[4][3]}'.center(13)+'|')
print(f'5. {MK[0][4]}'.ljust(10)+'|'+f'{MK[1][4]}'.center(26)+'|'+f'{MK[2][4]}'.center(5)+'|'+f'{MK[3][4]}'.center(8)+'|'+f'{MK[4][4]}'.center(13)+'|')
print(f'6. {MK[0][5]}'.ljust(10)+'|'+f'{MK[1][5]}'.center(26)+'|'+f'{MK[2][5]}'.center(5)+'|'+f'{MK[3][5]}'.center(8)+'|'+f'{MK[4][5]}'.center(13)+'|')
print(f'7. {MK[0][6]}'.ljust(10)+'|'+f'{MK[1][6]}'.center(26)+'|'+f'{MK[2][6]}'.center(5)+'|'+f'{MK[3][6]}'.center(8)+'|'+f'{MK[4][6]}'.center(13)+'|')
print(f'8. {MK[0][7]}'.ljust(10)+'|'+f'{MK[1][7]}'.center(26)+'|'+f'{MK[2][7]}'.center(5)+'|'+f'{MK[3][7]}'.center(8)+'|'+f'{MK[4][7]}'.center(13)+'|')
print('-'*67)

totalsks=sum(MK[2])
print(f'\t\t        TOTAL SKS      21')
str1='67'
a=str1.center(67,'-')
print(a)
jumlah_matkul=len(MK[1])
matkul_2sks=MK[2].count(2)
matkul_3sks=MK[2].count(3)
matkul_selasa=MK[3].count('Selasa')
matkul_rabu=MK[3].count('Rabu')
matkul_kamis=MK[3].count('Kamis')
matkul_jumat=MK[3].count('Jumat')


print(f'''Summary:
Jumlah Mata Kuliah       : {len(MK[1])}
Jumlah Mata Kuliah 2 SKS : {matkul_2sks} Mata Kuliah
Jumlah Mata Kuliah 3 SKS : {matkul_3sks} Mata Kuliah
Mata Kuliah hari Selasa  : {matkul_selasa} Mata Kuliah
Mata Kuliah hari Rabu    : {matkul_rabu} Mata Kuliah
Mata Kuliah hari Kamis   : {matkul_kamis} Mata Kuliah
Mata Kuliah hari Jumat   : {matkul_jumat} Mata Kuliah''')

nama_kota = bio[9]
tanggal = bio[2]
gabung = (nama_kota+", "+tanggal).rjust(73)
print(gabung)
print("\n"*4)
nama = bio[0]
strip_akhir = "-"*12
print(nama.rjust(73))
print(strip_akhir.rjust(72))







