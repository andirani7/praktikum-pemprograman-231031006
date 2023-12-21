password = '123'
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_input = input('masukkan password')

    if user_input == password:
     print ('selamat anda login!')
     break
else:
    attempts += 1
    remaining_attempts = max_attempts-attempts
    print ('password salah!')
    if remaining_attempts > 0:
        print ('kesempatan anda tersisa',remaining_attempts,'kali')
    else:
        print ('anda kehabisan kesempatan')
    
