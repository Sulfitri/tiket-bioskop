def tampilkan_genre():
    print("Daftar Genre:")
    print("1. Action")
    print("2. Comedy")
    print("3. Drama")
    print("4. Horror")

def tampilkan_jenis_film(genre):
    if genre == "1":
        print("Jenis Film Action:")
        print("1. Avengers - Harga: Rp40")
        print("2. Fast & Furious - Harga: Rp40")
        print("3. Mission Impossible - Harga: Rp40")
    elif genre == "2":
        print("Jenis Film Comedy:")
        print("1. Hangover - Harga: Rp40")
        print("2. Superbad - Harga: Rp40")
        print("3. 21 Jump Street - Harga: Rp40")
    elif genre == "3":
        print("Jenis Film Drama:")
        print("1. The Notebook - Harga: Rp40")
        print("2. Forrest Gump - Harga: Rp40")
        print("3. Titanic - Harga: Rp40")
    elif genre == "4":
        print("Jenis Film Horror:")
        print("1. The Conjuring - Harga: Rp40")
        print("2. Insidious - Harga: Rp40")
        print("3. A Quiet Place - Harga: Rp40")
    else:
        print("Genre tidak valid.")

def hitung_harga(jumlah_tiket, hari):
    if hari.lower() == "minggu":
        harga_tiket = 50
    elif hari.lower() == "sabtu":
        harga_tiket = 35
    else:
        harga_tiket = 40
    total_harga = harga_tiket * jumlah_tiket
    return total_harga

def get_genre_name(genre):
    genre_dict = {"1": "Action", "2": "Comedy", "3": "Drama", "4": "Horror"}
    return genre_dict.get(genre, "Tidak valid")

def get_film_name(genre, film):
    film_dict = {
        "1": {"1": "Avengers", "2": "Fast & Furious", "3": "Mission Impossible"},
        "2": {"1": "Hangover", "2": "Superbad", "3": "21 Jump Street"},
        "3": {"1": "The Notebook", "2": "Forrest Gump", "3": "Titanic"},
        "4": {"1": "The Conjuring", "2": "Insidious", "3": "A Quiet Place"}
    }
    return film_dict.get(genre, {}).get(film, "Tidak valid")

print("Selamat datang di Program Pembelian Tiket Film")

tampilkan_genre()
genre = input("Pilih nomor genre film yang ingin ditonton: ")

tampilkan_jenis_film(genre)
film = input("Pilih nomor film yang ingin ditonton: ")

jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
hari = input("Hari apa Anda ingin menonton (minggu/senin/selasa/rabu/kamis/jumat/sabtu)? ")

total_harga = hitung_harga(jumlah_tiket, hari)

print("\nDetail Pembelian:")
print("1. Genre:", get_genre_name(genre))
print("2. Film:", get_film_name(genre, film))
print("3. Jumlah Tiket:", jumlah_tiket)
print("4. Total Harga: Rp", total_harga)

confirm = input("Apakah Anda ingin melanjutkan pembelian (y/n)? ")
if confirm.lower() == "n":
    exit()
else:
    nama = input("Masukkan nama Anda: ")
    umur = input("Masukkan umur Anda: ")
    print("\nDetail Lengkap:")
    print("1. Nama:", nama)
    print("2. Umur:", umur)
    print("3. Genre:", get_genre_name(genre))
    print("4. Film:", get_film_name(genre, film))
    print("5. Jumlah Tiket:", jumlah_tiket)
    print("6. Total Harga: Rp", total_harga)
