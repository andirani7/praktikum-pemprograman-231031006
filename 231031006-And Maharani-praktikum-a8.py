def login():
    max_attempts = 3
    max_pages = 3
    password = ["ith", "ith2", "ith3"]

    for page in range(1, max_pages + 1):
        for attempt in range(1, max_attempts + 1):
            user_input = input(f"Masukkan password untuk Halaman {page}: ")

            if user_input == password[page - 1]:
                print(f"Password Benar, Selamat datang di Halaman {page}")
                break
            else:
                print(f"Password salah, Anda gagal pada Halaman {page}, percobaan ke-{attempt}")

        else:
            print(f"Anda telah mencapai batas percobaan pada Halaman {page}. Login gagal.")
            break
    else:
        print("Selamat Anda Berhasil Login!")

if __name__ == "__main__":
    login()
