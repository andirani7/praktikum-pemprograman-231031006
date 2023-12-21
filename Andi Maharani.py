Biodata={'Nama'   : 'Andi Maharani',
         'NIM'    : '231031006',
         'Kelas'  : 'SI23-A',
         'Prodi'  : 'Sistem Informasi',
         'Alamat' : 'BTN Sao Asri Blok E3/NO.3',
         'TTL'    : 'Parepare, 7 April 2005',
         'Agama'  : 'Islam',
         'No.HP'  : '085241379264'
         }
#nested dictionary
Sosmed={'Instagram':'@andiimaharanii',
        'Email'    :{'E1':'andiimaharanii005@gmail.com',
                     'E2':'maharaniandi06@gmail.com'}}
print(Biodata)
print()
print(Biodata.values())
print()
print(Biodata['Nama'])
print()
Biodata.update({'Jenis Kelamin' : 'Perempuan'})
print(Biodata)
print()
print(Biodata.get('Prodi'))
print()
print(len(Biodata['Alamat']))
print()
print()
print(Biodata.keys())
print()
print()
print(Sosmed['Email']['E2'])
print()
Sosmed['Email']['E3']='maharani@gmail.com'
print(Sosmed['Email'])
