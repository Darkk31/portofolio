import math
from tabulate import tabulate

# Daftar barangnya
daftar_barang = {
    1 : "Wallpaper Roll Kecil",
    2 : "Wallpaper Roll Besar",
    3 : "Wallpaper Custom",
    4 : "Wallfoam",
    5 : "Wallsticker",
    6 : "PVC 3D Wall Panel",
    7 : "Vinyl",
    8 : "Kaca Film"
}

# Daftar Wallpaper Roll Kecil 0.5 x 10
daftar_wallkecil = {
    1 : {"nama": "RONA 6", "harga": 200000},
    2 : {"nama": "RONA 7", "harga": 200000},
    3 : {"nama": "LULU", "harga": 220000},
    4 : {"nama": "ALASKA", "harga": 230000},
    5 : {"nama": "DYNASTY", "harga": 230000},
    6 : {"nama": "ECO", "harga": 230000},
    7 : {"nama": "OLOKKI", "harga": 230000},
    8 : {"nama": "CAPITAL", "harga": 240000},
    9 : {"nama": "M6", "harga": 240000},
    10: {"nama": "ALEXANDER", "harga": 250000},
    11: {"nama": "CHIVAS REGAS", "harga": 250000},
    12: {"nama": "ELITE", "harga": 250000},
    13: {"nama": "KENSHO", "harga": 250000},
    14: {"nama": "MINESOTA", "harga": 250000},
    15: {"nama": "NEW DREAM 3", "harga": 250000},
    16: {"nama": "NORDICA", "harga": 250000},
    17: {"nama": "PLUS 2", "harga": 250000},
    18: {"nama": "PLUS 3", "harga": 250000},
    19: {"nama": "PLUS 4", "harga": 250000},
    20: {"nama": "SAPPHIRE VOL 2", "harga": 250000},
    21: {"nama": "SIENA", "harga": 250000},
    22: {"nama": "CASSANOVA", "harga": 280000},
    23: {"nama": "CLASSICO", "harga": 280000},
    24: {"nama": "EXECUTIVE", "harga": 280000},
    25: {"nama": "GOOD IDEA CENDANA", "harga": 280000},
    26: {"nama": "GOOD IDEA PRIVATE", "harga": 280000},
    27: {"nama": "HOME DECO", "harga": 280000},
    28: {"nama": "LA VIDA", "harga": 280000},
    29: {"nama": "NEW PAVILION 2", "harga": 280000},
    30: {"nama": "NOTABENE", "harga": 280000},
    31: {"nama": "SEVILLA", "harga": 280000},
    32: {"nama": "SKYFALL", "harga": 280000},
    33: {"nama": "STARKIDS", "harga": 280000},
    34: {"nama": "JADE", "harga": 300000},
}

#Daftar Wallpaper Roll Besar 1 x 15
daftar_wallbesar = {
    1 : {"nama": "T.O.P", "harga":          750000},
    2 : {"nama": "MONO", "harga":           800000},
    3 : {"nama": "HERA VOL 5", "harga":     800000},
    4 : {"nama": "ARTIST", "harga":         850000},
    5 : {"nama": "BELLA VISTA", "harga":    850000},
    6 : {"nama": "CASABLANCA", "harga":     850000},
    7 : {"nama": "E-ROOM", "harga":         850000},
    8 : {"nama": "FAVORITA", "harga":       850000},
    9 : {"nama": "GOLDWIN", "harga":        850000},
    10: {"nama": "LEGEND", "harga":         850000},
    11: {"nama": "MAVERICK", "harga":       850000},
    12: {"nama": "WINTER SONATA", "harga":  850000},
    13: {"nama": "ANDO", "harga":           880000},
    14: {"nama": "DESIGN PLUS", "harga":    880000},
    15: {"nama": "M & G", "harga":          880000},
    16: {"nama": "MOMENT", "harga":         880000},
    17: {"nama": "PLATINUM", "harga":       880000},
    18: {"nama": "C'EST LA VIE", "harga":   900000},
    19: {"nama": "DARAE VOL 4", "harga":    900000},
    20: {"nama": "IKON", "harga":           900000},
    21: {"nama": "LUMINAIRE", "harga":      950000},
    22: {"nama": "VELUCE", "harga":         950000},
}

daftar_vinyl = {
    1 : {"nama": "Vinyl Taco 2mm", "harga":          800000},
    2 : {"nama": "Vinyl Taco 3mm", "harga":          850000},
    3 : {"nama": "Vinyl Taco 5mm", "harga":          900000},
    4 : {"nama": "Vinyl Teka 2mm", "harga":          750000},
    5 : {"nama": "Vinyl Toka 2mm", "harga":          750000},
    6 : {"nama": "Vinyl Daedong 2mm", "harga":          750000},
    7 : {"nama": "Vinyl Sooku 3mm", "harga":          750000},
    8 : {"nama": "Vinyl Rona 3mm", "harga":          750000},
    9 : {"nama": "SPC Taco 5mm", "harga":          750000},
    10: {"nama": "SPC de lux 3mm", "harga":          750000},
    11: {"nama": "SPC Rona 4mm", "harga":          750000}
}

daftar_kacafilm = {

}

# Tampilkan daftar barang
print("Daftar Barang")
print("=============================================")
for i, barang in daftar_barang.items():
    print(f"{i}. {barang}")

# Input nomor barang
nomor_barang = input("Masukkan nomor barang: ")
while not nomor_barang.isdigit() or int(nomor_barang) < 1 or int(nomor_barang) > len(daftar_barang):
    nomor_barang = input("Nomor barang tidak valid. Silakan masukkan nomor barang yang benar: ")

# Proses data berdasarkan nomor barang yang dimasukkan
nama_barang = daftar_barang[int(nomor_barang)]
print(f"Barang yang dipilih: {nama_barang}")

if nomor_barang == "1":
    # Tampilkan daftar wallpaper roll kecil
    print("Daftar Wallpaper Roll Kecil")
    print("=============================================")
    print(tabulate([(k, v['nama'], v['harga']) for k, v in daftar_wallkecil.items()], headers=['No', 'Nama', 'Harga'], tablefmt='fancy_grid'))

    # Input nomor wallpaper roll kecil
    nomor_wallkecil = input("Masukkan Nomor Wallpaper Yang Mau Dihitung: ")
    while not nomor_wallkecil.isdigit() or int(nomor_wallkecil) < 1 or int(nomor_wallkecil) > len(daftar_wallkecil):
        nomor_wallkecil = input("Nomor wallpaper roll kecil tidak valid. Silakan masukkan nomor yang benar: ")

    # Proses data
    if nomor_wallkecil in ("1","2"):
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (10 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 0.5
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 200000

        # Menampilkan hasil perhitungan
        print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (10 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 0.5
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 200000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_wallkecil == "3":
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (10 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 0.5
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 220000

        # Menampilkan hasil perhitungan
        print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (10 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 0.5
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 220000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_wallkecil in ("4","5","6","7"):
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (10 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 0.5
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 230000

        # Menampilkan hasil perhitungan
        print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (10 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 0.5
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 230000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_wallkecil in ("8","9"):
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (10 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 0.5
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 240000

        # Menampilkan hasil perhitungan
        print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (10 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 0.5
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 240000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_wallkecil in ("10","11","12","13","14","15","16","17","18","19","20","21"):
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (10 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 0.5
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 250000

        # Menampilkan hasil perhitungan
        print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (10 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 0.5
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 250000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")


    elif nomor_wallkecil in ("22","23","24","25","26","27","28","29","30","31","32","33"):
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (10 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 0.5
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 280000

        # Menampilkan hasil perhitungan
        print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (10 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 0.5
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 280000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_wallkecil == "34" :
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (10 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 0.5
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 300000

        # Menampilkan hasil perhitungan
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (10 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 0.5
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 300000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    else:
        print("Masukkan ulang!")

elif nomor_barang == "2":
    # Tampilkan daftar wallpaper roll kecil
    print("Daftar Wallpaper Roll Besar")
    print("=============================================")
    print(tabulate([(k, v['nama'], v['harga']) for k, v in daftar_wallbesar.items()], headers=['No', 'Nama', 'Harga'], tablefmt='fancy_grid'))

    # Input nomor Wallpaper Roll Besar
    nomor_wallbesar = input("Masukkan Nomor Wallpaper Yang Mau Dihitung: ")
    while not nomor_wallbesar.isdigit() or int(nomor_wallbesar) < 1 or int(nomor_wallbesar) > len(daftar_wallbesar):
        nomor_wallbesar = input("Nomor wallpaper roll besar tidak valid. Silakan masukkan nomor yang benar: ")

    if nomor_wallbesar == "1":
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (15 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 1
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 750000

        # Menampilkan hasil perhitungan
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (15 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 1
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 750000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_wallbesar == "2" and "3":
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (15 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 1
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 800000

        # Menampilkan hasil perhitungan
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (15 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 1
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 800000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_wallbesar in ("4", "5", "6","7","8","9","!0","11", "12"):
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (15 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 1
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 850000

        # Menampilkan hasil perhitungan
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (15 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 1
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 850000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_wallbesar in ("13","14","15","16","17"):
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (15 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 1
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 880000

        # Menampilkan hasil perhitungan
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (15 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 1
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 880000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_wallbesar in ("18", "19", "20"):
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (15 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 1
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 900000

        # Menampilkan hasil perhitungan
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (15 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 1
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 900000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_wallbesar == "21" and "22":
        tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
        lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
        keping = (15 / tinggi)
        pembulatan_keping = math.floor(keping)
        meter = pembulatan_keping * 1
        jumlah_roll = lebar / meter
        pembulatan_jumlah_roll = math.ceil(jumlah_roll)

        harga = pembulatan_jumlah_roll * 950000

        # Menampilkan hasil perhitungan
        print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
        print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
                lebar = int(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
                keping = (15 / tinggi)
                pembulatan_keping = math.floor(keping)
                meter = pembulatan_keping * 1
                jumlah_roll = lebar / meter
                pembulatan_jumlah_roll = math.ceil(jumlah_roll)

                harga = pembulatan_jumlah_roll * 950000

        # Menampilkan hasil perhitungan
                print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
                print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
                print("HARGANYA ADALAH ", harga)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    else:
        print("Masukkan Ulang")

elif nomor_barang == "3":
    L = float(input("Masukkan Lebarnya = "))
    T = float(input("Masukkan Tingginya = "))
    WC = L * T
    print("Meter perseginya = ", WC)
    print("Harganya = ", "METER PERSEGI x 250.000")
    print("         = ", WC * 250000)

elif nomor_barang == "4":
    L = float(input("Masukkan lebarnya = "))
    T = float(input("Masukkan Tingginya = "))
    WF = L * T
    print("Untuk luas persegi dindingnya ",WF, "Meter persegi")
    JWF = WF / 0.539
    jwf = math.ceil(JWF)
    print("Butuh Wallfoam sebanyak", jwf, "Lembar")
    print("Untuk perlembarnya 50.000")
    print("Totalnya adalah ",jwf * 50000)

elif nomor_barang == "5":
    tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
    lebar = float(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
    keping = (10 / tinggi)
    pembulatan_keping = math.floor(keping)
    meter = pembulatan_keping * 0.45
    jumlah_roll = lebar / meter
    pembulatan_jumlah_roll = math.ceil(jumlah_roll)

    harga = pembulatan_jumlah_roll * 50000

        # Menampilkan hasil perhitungan
    print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
    print("HARGANYA ADALAH ", harga)

        # Meminta input ulang jika ada kesalahan
    while True:
        pilihan = input("Apakah ada yang salah? (ya/tidak) ")
        if pilihan.lower() == "ya":
            tinggi = float(input("MASUKKAN TINGGI DINDINGNYA = "))
            lebar = float(input("MASUKKAN LEBAR DINDINGNYA = "))

        # Menghitung jumlah roll wallpaper yang dibutuhkan
            keping = (10 / tinggi)
            pembulatan_keping = math.floor(keping)
            meter = pembulatan_keping * 0.45
            jumlah_roll = lebar / meter
            pembulatan_jumlah_roll = math.ceil(jumlah_roll)

            harga = pembulatan_jumlah_roll * 50000

        # Menampilkan hasil perhitungan
            print("ANDA DAPAT {0} KEPING".format(pembulatan_keping))
            print("MEMERLUKAN {0} ROLL".format(pembulatan_jumlah_roll))
            print("HARGANYA ADALAH ", harga)
        elif pilihan.lower() == "tidak":
            break
        else:
            print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

elif nomor_barang == "6":
    L = float(input("Masukkan lebarnya = "))
    T = float(input("Masukkan Tingginya = "))
    WF = L * T
    print("Untuk luas persegi dindingnya ",WF, "Meter persegi")
    JWF = WF / 0.25
    jwf = math.ceil(JWF)
    print("Butuh Wallfoam sebanyak", jwf, "Keping ")
    print("Untuk perkepingnya 50.000")
    print("Totalnya adalah ",jwf * 50000)

elif nomor_barang == "7":
    # Tampilkan daftar Vinyl
    print("Daftar Vinyl")
    print("=============================================")
    print(tabulate([(k, v['nama'], v['harga']) for k, v in daftar_vinyl.items()], headers=['No', 'Nama', 'Harga'], tablefmt='fancy_grid'))

    # Input nomor Vinyl
    nomor_vinyl = input("Masukkan Nomor Vinyl Yang Mau Dihitung: ")
    while not nomor_vinyl.isdigit() or int(nomor_vinyl) < 1 or int(nomor_vinyl) > len(daftar_vinyl):
        nomor_vinyl = input("Nomor Vinyl Tidak Valid. Silakan masukkan nomor yang benar: ")

    if nomor_vinyl == "1":
        Lebar = float(input("Masukkan lebar lantainya : "))
        Panjang = float(input("Masukkan panjang lantainya : "))
        Luas = Lebar * Panjang
        lUas = Luas * (10/100)
        lulu = lUas + Luas
        LuAs = lulu / 3.76
        luas = math.ceil(LuAs)
        print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
        print("Harga perkotaknya adalah 650.000")
        print("Total biayanya adalah ",luas*650000)
        print("Harga perkotak beserta upah pasangnya adalah 800.000")
        print("Total biayanya beserta upah pasang adalah ", luas*800000)
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                Lebar = float(input("Masukkan lebar lantainya : "))
                Panjang = float(input("Masukkan panjang lantainya : "))
                Luas = Lebar * Panjang
                lUas = Luas * (10/100)
                lulu = lUas + Luas
                LuAs = lulu / 3.76
                luas = math.ceil(LuAs)
                print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
                print("Harga perkotaknya adalah 650.000")
                print("Total biayanya adalah ",luas*650000)
                print("Harga perkotak beserta upah pasangnya adalah 800.000")
                print("Total biayanya beserta upah pasang adalah ", luas*800000)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_vinyl == "2":
        Lebar = float(input("Masukkan Lebar lantainya : "))
        Panjang = float(input("Masukkan panjang lantainya : "))
        Luas = Lebar * Panjang
        lUas = Luas * (10/100)
        lulu = lUas + Luas
        LuAs = lulu / 3.34
        luas = math.ceil(LuAs)
        print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
        print("Harga perkotaknya adalah 700.000")
        print("Total biayanya adalah ",luas*700000)
        print("Harga perkotak beserta upah pasangnya adalah 850.000")
        print("Total biayanya beserta upah pasang adalah ", luas*850000)
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                Lebar = float(input("Masukkan Lebar lantainya : "))
                Panjang = float(input("Masukkan panjang lantainya : "))
                Luas = Lebar * Panjang
                lUas = Luas * (10/100)
                lulu = lUas + Luas
                LuAs = lulu / 3.34
                luas = math.ceil(LuAs)
                print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
                print("Harga perkotaknya adalah 700.000")
                print("Total biayanya adalah ",luas*700000)
                print("Harga perkotak beserta upah pasangnya adalah 850.000")
                print("Total biayanya beserta upah pasang adalah ", luas*850000)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")
    elif nomor_vinyl == "3":
        Lebar = float(input("Masukkan Lebar lantainya : "))
        Panjang = float(input("Masukkan panjang lantainya : "))
        Luas = Lebar * Panjang
        lUas = Luas * (10/100)
        lulu = lUas + Luas
        LuAs = lulu / 2.13
        luas = math.ceil(LuAs)
        print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
        print("Harga perkotaknya adalah 850.000")
        print("Total biayanya adalah ",luas*850000)
        print("Harga perkotak beserta upah pasangnya adalah 1.000.000")
        print("Total biayanya beserta upah pasang adalah ", luas*1000000)
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                Lebar = float(input("Masukkan Lebar lantainya : "))
                Panjang = float(input("Masukkan panjang lantainya : "))
                Luas = Lebar * Panjang
                lUas = Luas * (10/100)
                lulu = lUas + Luas
                LuAs = lulu / 2.13
                luas = math.ceil(LuAs)
                print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
                print("Harga perkotaknya adalah 850.000")
                print("Total biayanya adalah ",luas*850000)
                print("Harga perkotak beserta upah pasangnya adalah 1.000.000")
                print("Total biayanya beserta upah pasang adalah ", luas*1000000)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")
    elif nomor_vinyl == "4":
        Lebar = float(input("Masukkan Lebar lantainya : "))
        Panjang = float(input("Masukkan panjang lantainya : "))
        Luas = Lebar * Panjang
        lUas = Luas * (10/100)
        lulu = lUas + Luas
        LuAs = lulu / 2.29
        luas = math.ceil(LuAs)
        print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
        print("Harga perkotaknya adalah 800.000")
        print("Total biayanya adalah ",luas*800000)
        print("Harga perkotak beserta upah pasangnya adalah 950.000")
        print("Total biayanya beserta upah pasang adalah ", luas*950000)

        print("")
        print("VARIAN STONE")
        LuAs = lulu / 2.16
        luas = math.ceil(LuAs)
        print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
        print("Harga perkotaknya adalah 800.000")
        print("Total biayanya adalah ",luas*800000)
        print("Harga perkotak beserta upah pasangnya adalah 950.000")
        print("Total biayanya beserta upah pasang adalah ", luas * 950000)
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                Lebar = float(input("Masukkan Lebar lantainya : "))
                Panjang = float(input("Masukkan panjang lantainya : "))
                Luas = Lebar * Panjang
                lUas = Luas * (10/100)
                lulu = lUas + Luas
                LuAs = lulu / 2.29
                luas = math.ceil(LuAs)
                print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
                print("Harga perkotaknya adalah 800.000")
                print("Total biayanya adalah ",luas*800000)
                print("Harga perkotak beserta upah pasangnya adalah 950.000")
                print("Total biayanya beserta upah pasang adalah ", luas*950000)

                print("")
                print("VARIAN STONE")
                LuAs = lulu / 2.16
                luas = math.ceil(LuAs)
                print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
                print("Harga perkotaknya adalah 800.000")
                print("Total biayanya adalah ",luas*800000)
                print("Harga perkotak beserta upah pasangnya adalah 950.000")
                print("Total biayanya beserta upah pasang adalah ", luas * 950000)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")
    elif nomor_vinyl in ("5","7") :
        Lebar = float(input("Masukkan Lebar lantainya : "))
        Panjang = float(input("Masukkan panjang lantainya : "))
        Luas = Lebar * Panjang
        lUas = Luas * (10/100)
        lulu = lUas + Luas
        LuAs = lulu / 3.3
        luas = math.ceil(LuAs)
        print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
        print("Harga perkotaknya adalah 600.000")
        print("Total biayanya adalah ",luas*600000)
        print("Harga perkotak beserta upah pasangnya adalah 750.000")
        print("Total biayanya beserta upah pasang adalah ", luas*750000)
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                Lebar = float(input("Masukkan Lebar lantainya : "))
                Panjang = float(input("Masukkan panjang lantainya : "))
                Luas = Lebar * Panjang
                lUas = Luas * (10/100)
                lulu = lUas + Luas
                LuAs = lulu / 3.3
                luas = math.ceil(LuAs)
                print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
                print("Harga perkotaknya adalah 600.000")
                print("Total biayanya adalah ",luas*600000)
                print("Harga perkotak beserta upah pasangnya adalah 750.000")
                print("Total biayanya beserta upah pasang adalah ", luas*750000)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_vinyl == "6":
        Lebar = float(input("Masukkan Lebar lantainya : "))
        Panjang = float(input("Masukkan panjang lantainya : "))
        Luas = Lebar * Panjang
        lUas = Luas * (10/100)
        lulu = lUas + Luas
        LuAs = lulu / 3.3
        luas = math.ceil(LuAs)
        print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
        print("Harga perkotaknya adalah 600.000")
        print("Total biayanya adalah ",luas*600000)
        print("Harga perkotak beserta upah pasangnya adalah 750.000")
        print("Total biayanya beserta upah pasang adalah ", luas*750000)
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                Lebar = float(input("Masukkan Lebar lantainya : "))
                Panjang = float(input("Masukkan panjang lantainya : "))
                Luas = Lebar * Panjang
                lUas = Luas * (10/100)
                lulu = lUas + Luas
                LuAs = lulu / 3.3
                luas = math.ceil(LuAs)
                print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
                print("Harga perkotaknya adalah 600.000")
                print("Total biayanya adalah ",luas*600000)
                print("Harga perkotak beserta upah pasangnya adalah 750.000")
                print("Total biayanya beserta upah pasang adalah ", luas*750000)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")
    elif nomor_vinyl == "8":
        Lebar = float(input("Masukkan Lebar lantainya : "))
        Panjang = float(input("Masukkan panjang lantainya : "))
        Luas = Lebar * Panjang
        lUas = Luas * (10/100)
        lulu = lUas + Luas
        LuAs = lulu / 3.34
        luas = math.ceil(LuAs)
        print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
        print("Harga perkotaknya adalah TIDAK DIKETAHUI")
        print("Total biayanya adalah TIDAK DIKETAHUI ")
        print("Harga perkotak beserta upah pasangnya adalah TIDAK DIKETAHUI")
        print("Total biayanya beserta upah pasang adalah TIDAK DIKETAHUI")
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                Lebar = float(input("Masukkan Lebar lantainya : "))
                Panjang = float(input("Masukkan panjang lantainya : "))
                Luas = Lebar * Panjang
                lUas = Luas * (10/100)
                lulu = lUas + Luas
                LuAs = lulu / 3.34
                luas = math.ceil(LuAs)
                print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
                print("Harga perkotaknya adalah TIDAK DIKETAHUI")
                print("Total biayanya adalah TIDAK DIKETAHUI ")
                print("Harga perkotak beserta upah pasangnya adalah TIDAK DIKETAHUI")
                print("Total biayanya beserta upah pasang adalah TIDAK DIKETAHUI")
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")
    elif nomor_vinyl == "9":
        Lebar = float(input("Masukkan Lebar lantainya : "))
        Panjang = float(input("Masukkan panjang lantainya : "))
        Luas = Lebar * Panjang
        lUas = Luas * (10/100)
        lulu = lUas + Luas
        LuAs = lulu / 3.34
        luas = math.ceil(LuAs)
        print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
        print("Harga perkotaknya adalah TIDAK DIKETAHUI")
        print("Total biayanya adalah TIDAK DIKETAHUI")
        print("Harga perkotak beserta upah pasangnya adalah TIDAK DIKETAHUI")
        print("Total biayanya beserta upah pasang adalah TIDAK DIKETAHUI")
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                Lebar = float(input("Masukkan Lebar lantainya : "))
                Panjang = float(input("Masukkan panjang lantainya : "))
                Luas = Lebar * Panjang
                lUas = Luas * (10/100)
                lulu = lUas + Luas
                LuAs = lulu / 3.34
                luas = math.ceil(LuAs)
                print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
                print("Harga perkotaknya adalah TIDAK DIKETAHUI")
                print("Total biayanya adalah TIDAK DIKETAHUI")
                print("Harga perkotak beserta upah pasangnya adalah TIDAK DIKETAHUI")
                print("Total biayanya beserta upah pasang adalah TIDAK DIKETAHUI")
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")

    elif nomor_vinyl == "10":
        Lebar = float(input("Masukkan Lebar lantainya : "))
        Panjang = float(input("Masukkan panjang lantainya : "))
        Luas = Lebar * Panjang
        lUas = Luas * (10/100)
        lulu = lUas + Luas
        LuAs = lulu / 2.1
        luas = math.ceil(LuAs)
        print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
        print("Harga perkotaknya adalah 735.000")
        print("Total biayanya adalah ",luas*735000)
        print("Harga perkotak beserta upah pasangnya adalah 885.000")
        print("Total biayanya beserta upah pasang adalah ", luas*885000)
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                Lebar = float(input("Masukkan Lebar lantainya : "))
                Panjang = float(input("Masukkan panjang lantainya : "))
                Luas = Lebar * Panjang
                lUas = Luas * (10/100)
                lulu = lUas + Luas
                LuAs = lulu / 2.1
                luas = math.ceil(LuAs)
                print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
                print("Harga perkotaknya adalah 735.000")
                print("Total biayanya adalah ",luas*735000)
                print("Harga perkotak beserta upah pasangnya adalah 885.000")
                print("Total biayanya beserta upah pasang adalah ", luas*885000)
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")
    elif nomor_vinyl == "11":
        Lebar = float(input("Masukkan Lebar lantainya : "))
        Panjang = float(input("Masukkan panjang lantainya : "))
        Luas = Lebar * Panjang
        lUas = Luas * (10/100)
        lulu = lUas + Luas
        LuAs = lulu / 2.79
        luas = math.ceil(LuAs)
        print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
        print("Harga perkotaknya adalah TIDAK DIKEAHUI")
        print("Total biayanya adalah TIDAK DIKETAHUI")
        print("Harga perkotak beserta upah pasangnya adalah TIDAK DIKETAHUI")
        print("Total biayanya beserta upah pasang adalah TIDAK DIKETAHUI")
        while True:
            pilihan = input("Apakah ada yang salah? (ya/tidak) ")
            if pilihan.lower() == "ya":
                Lebar = float(input("Masukkan Lebar lantainya : "))
                Panjang = float(input("Masukkan panjang lantainya : "))
                Luas = Lebar * Panjang
                lUas = Luas * (10/100)
                lulu = lUas + Luas
                LuAs = lulu / 2.79
                luas = math.ceil(LuAs)
                print("Untuk penggunaan bahan vinylnya adalah ",luas," Kotak")
                print("Harga perkotaknya adalah TIDAK DIKEAHUI")
                print("Total biayanya adalah TIDAK DIKETAHUI")
                print("Harga perkotak beserta upah pasangnya adalah TIDAK DIKETAHUI")
                print("Total biayanya beserta upah pasang adalah TIDAK DIKETAHUI")
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Masukan salah, silakan masukkan 'ya' atau 'tidak'")
    else:
        print("Masukkan Ulang")
