#Tugas Projek ALgo TM (E)
#Program Pertanian Rumahan
#Prodi : Informatika
#Anggota: 
# 1. Alvio Damayanti        (222410103032)
# 2. Lu'lu'un Fifalaqisa    (222410103038)

import pandas as pd
import os
import time
from csv import writer

path = os.path.realpath('List Tanaman Singkat.csv')
path_new = path.replace("\\", "/") 

def splashscreen():
    os.system("cls")
    print("SELAMAT DATANG DI".center(40, "="))
    print("HOME FARM".center(40))

def login():
    print("""
Masuk ke akun :
[1] Masuk Sebagai Admin
[2] Masuk Sebagai User
    """)
    akun = int(input("Pilih Opsi Untuk Login Ke Akun (1/2) : "))
    if akun == 1:
        namaadmin = input("\nMasukkan Username : ")
        pwadmin = "admin"
        pw = input("Masukkan Password : ")
        pw = pw.lower()
        while pw != pwadmin:
            print("\nPassword yang anda masukkan bukan password admin")
            print("Silahkan masukkan password admin yang sesuai")
            pw = input("\nMasukkan Password : ")
            pw = pw.lower()
        if pw == pwadmin:
            os.system("cls")
            print("Hi! Admin", namaadmin)
            datatanaman()
            menuadmin()
    elif akun == 2:
        namauser = input("\nMasukkan Username : ")
        pw = input("Masukkan Password : ")
        os.system("cls")
        print("Hi! Selamat Datang di Home Farm", namauser)
        datatanaman()
        menuuser()
    else:
        print("\nERROR! Halaman Tidak Ditemukan")
        os.system("cls")
        login()

def kembali_menuadmin():
    print(input("\nKembali Ke Pilihan Menu, Tekan Enter"))
    menuadmin()

def kembali_menuuser():
    print(input("\nKembali Ke Pilihan Menu, Tekan Enter"))
    menuuser()

def datatanaman():
    print("Data Keseluruhan Tanaman Akan Muncul")
    hitung = ["3..","2..","1.."]
    print("Mohon Ditunggu...")
    for i in hitung:
        print(i)
        time.sleep(1)
    print("\nMemunculkan Data Tanaman...\n")
    df = pd.read_csv(path_new)
    dfx = df.dropna()
    print(dfx.to_string())
    print("\nJumlah Data Tanaman :", len(dfx))
    print("Ukuran Data Frame :", dfx.shape)

def menuadmin():
    df = pd.read_csv(path_new)
    dfx = df.dropna()
    print("\nAda yang bisa kami bantu?")
    print("""
Pilihan :
[1] Mengganti Data yang Ada
[2] Menghapus Beberapa Data
[3] Keluar
            """)
    menuadmin = int(input("Pilih Nomor Berapa? (1/2/3): "))
    if menuadmin == 1:
        print("Data dengan nomor index berapa yang ingin Anda ganti?")
        no_index = int(input("Nomor Index :"))
        print("Apakah Benar Data Berikut Yang Ingin Anda Ubah?")
        print(dfx.iloc[no_index])
        print("""Data apa yang ingin Anda ubah?
[0] Tanaman
[1] Nama
[2] Lama Panen
[3] Penyiraman
[4] Jarak Tanam
[5] Modal/bibit
[6] Musim
[7] Penyemaian
[8] Bibit/Lubang
[9] Harga/kg""")
        index_ubah = int(input("Masukkan Nomor Data yang Ingin Diubah : "))
        data_ubah = input("Inputkan Data Terbaru : ")
        dfx.iloc[no_index,index_ubah] = data_ubah
        print("Data Telah Diubah")
        print(dfx)
        kembali_menuadmin()
    elif menuadmin == 2:
        print("Data dengan nomor index berapa yang ingin Anda hapus?")
        index_hapus = int(input("Nomor Index :"))
        print(dfx.iloc[index_hapus])
        jawab = input("Apakah Benar Data Tersebut Yang Ingin Anda Hapus (Ya/Tidak) : ")
        jawab = jawab.lower()
        while jawab == "tidak":
            print("Masukkan Kembali Index Data yang Ingin Anda Hapus")
            index_hapus = int(input("Nomor Index :"))
            print(dfx.iloc[index_hapus])
            jawab = input("Apakah Benar Data Tersebut Yang Ingin Anda Hapus (Ya/Tidak) : ")
        if jawab == "ya":
            dfx = dfx.drop(index_hapus)
            print("Data Telah terhapus")
        print(dfx)
        kembali_menuadmin()
    elif menuadmin == 3:
        logoutadmin()
    else:
        print("Pilihan Tidak Tersedia")
        print("Harap Pilih Kembali Menu yang Sesuai")
        kembali_menuadmin()

def newrow1 (csvFileName, tambahan1):
    with open(csvFileName, 'a', newline='') as f:
        append_writer = writer(f)
        append_writer.writerow(tambahan1)

def menuuser():
    df = pd.read_csv(path_new)
    dfx = df.dropna()
    print("\nAda yang bisa kami bantu?")
    print("""Pilihan :
[1] Mencari Data Berdasarkan Kriteria
[2] Melihat Data Tanaman Saya
[3] Keluar
    """)
    menuuser = int(input("Pilih Nomor Berapa? (1/2): "))
    if menuuser == 1:
        print("""Kriteria Data :
[0] Tanaman
[1] Nama""")
        kolom = int(input("\nAnda Ingin Mencari Data Berdasarkan Kriteria Nomor Berapa? : "))
        if kolom == 0 :
            print("""Jenis Tanaman :
[1] Sayur
[2] Pangan
[3] Rempah""")
            jenis_tanaman = int(input("Masukkan Jenis Tanaman (1/2/3) : "))
            if jenis_tanaman == 1:
                sayur = dfx.loc[dfx['Tanaman'].isin(['Sayur'])]
                print(sayur)
                index_sayur = int(input("Masukkan Index Tanaman Sayur yang Ingin Anda Tanam : "))
                print("Berikut Data Tanaman Yang Anda Inginkan")
                datauser = dfx.iloc[index_sayur]
                print(datauser)
                tanggal = input("Masukkan Tanggal Mulai Menanam (dd/mm/yyyy) :")
                penanaman = [tanggal]
                for i in datauser:
                    penanaman.append(i)
                newrow1('DataPenanaman.csv', penanaman)
                print("Data Telah Tersimpan! Lanjutkan Penginputan Ukuran Lahan")
                jumlah_bibit()
            elif jenis_tanaman == 2:
                pangan = dfx.loc[dfx['Tanaman'].isin(['Pangan'])]
                print(pangan)
                index_pangan = int(input("Masukkan Index Tanaman Pangan yang Ingin Anda Tanam : "))
                print("Berikut Data Tanaman Yang Anda Inginkan")
                datauser = dfx.iloc[index_pangan]
                print(datauser)
                tanggal = input("Masukkan Tanggal Mulai Menanam (dd/mm/yyyy) :")
                penanaman = [tanggal]
                for i in datauser:
                    penanaman.append(i)
                newrow1('DataPenanaman.csv', penanaman)
                print("Data Telah Tersimpan! Lanjutkan Penginputan Ukuran Lahan")
                jumlah_bibit()
            elif jenis_tanaman == 3:
                rempah = dfx.loc[dfx['Tanaman'].isin(['Rempah'])]
                print(rempah)
                index_rempah = int(input("Masukkan Index Tanaman Rempah yang Ingin Anda Tanam : "))
                print("Berikut Data Tanaman Yang Anda Inginkan")
                datauser = dfx.iloc[index_rempah]
                print(datauser)
                tanggal = input("Masukkan Tanggal Mulai Menanam (dd/mm/yyyy) :")
                penanaman = [tanggal]
                for i in datauser:
                    penanaman.append(i)
                newrow1('DataPenanaman.csv', penanaman)
                print("Data Telah Tersimpan! Lanjutkan Penginputan Ukuran Lahan")
                jumlah_bibit()
            else:
                print("ERROR... Masukkan Data yang Benar")
                menuuser()
        elif kolom == 1 : 
            nama = input("Masukkan Nama Tanaman yang Anda Cari : ")
            nama1 = df.loc[df['Nama'].isin([nama])]
            dfx = df['Nama']
            list_nama = []
            for i in dfx:
                list_nama.append(i)
            if nama in list_nama:
                print(nama1)
                df = pd.read_csv(path_new)
                dfx = df.dropna()
                index_nama = int(input("Masukkan Index Tanaman Rempah yang Ingin Kamu Tanam : "))
                print("Berikut Data Tanaman Yang Anda Inginkan")
                datauser = dfx.iloc[index_nama]
                print(datauser)
                tanggal = input("Masukkan Tanggal Mulai Menanam (dd/mm/yyyy) :")
                penanaman = [tanggal]
                for i in datauser:
                    penanaman.append(i)
                newrow1('DataPenanaman.csv', penanaman)
                print("Data Telah Tersimpan! Lanjutkan Penginputan Ukuran Lahan")
                jumlah_bibit()
            else:
                print("Nama Tanaman Tidak Terdapat di List, Cari Data Lainnya")
                kembali_menuuser()
        else:
            print("Pilihan Tidak Tersedia, Harap Pilih Kembali")
            kembali_menuuser()
    elif menuuser == 2:
        print(pd.read_csv('DataPenanaman.csv'))
        print()
        print(pd.read_csv('Datamodal.csv'))
        kembali_menuuser()
    elif menuuser == 3:
        logoutuser()
    else:
        print("Pilihan Tidak Tersedia")
        print("Harap Pilih Kembali Menu yang Sesuai")
        kembali_menuuser()

def Jumlah_lubang(panjang, lebar, jarak): 
        a = (int((panjang)/(jarak)) + 1 )
        b = (int((lebar)/(jarak)) + 1 )
        lubang = a * b
        print("Jumlah_lubang:", lubang)
        return lubang

def jumlah_bibit():
    panjang = int(input("Masukkan panjang lahan yang Anda miliki (cm) : "))
    lebar = int(input("Masukkan lebar lahan yang Anda miliki (cm) : "))
    jarak = int(input("Masukkan jarak tanam yang ada pada data (cm) : "))
    path = os.path.realpath('DataPenanaman.csv')
    path_new = path.replace("\\", "/")
    df = pd.read_csv(path_new)
    print(df)
    index = int(input("Masukkan Index Tanaman Tersebut Sesuai yang Tertera Pada Data Penanaman : "))
    modal = df.loc[index,'Modal Bibit']
    jmlbibit = df.loc[index,'Jml Bibit']
    perlubang = df.loc[index,'Bibit/lubang']
    jual = df.loc[index,'Harga jual/kg']
    tanggal = df.loc[index,'Tanggal']
    nama = df.loc[index,'Nama']
    a = modal
    b = jmlbibit
    c = perlubang
    d = jual
    e = tanggal
    f = nama
    totalbibit = Jumlah_lubang(panjang, lebar, jarak) * c
    totalmodal = totalbibit * (a/b)
    print("Jumlah Bibit yang Dibutuhkan adalah :",int(totalbibit),"Bibit")
    print("Total Modal yang Dibutuhkan adalah : Rp",int(totalmodal))
    print("Dengan Harga Jual/kg : Rp", d)
    print("Data Modal Awal Telah Dibuat!")
    datamodal = [e,panjang,lebar,f,totalbibit,totalmodal,d]
    newrow1('Datamodal.csv', datamodal)
    kembali_menuuser()

def logoutadmin():
    pilihan = input("Apakah Anda yakin ingin keluar? (Ya/Tidak) : ").lower()
    a = ("Tidak").lower()
    if pilihan == a:
        print("\nPilih opsi kembali: ")
        return menuadmin()
    else:
        print("Terima kasih telah berkunjung")
        exit()

def logoutuser():
    pilihan = input("Apakah Anda yakin ingin keluar? (Ya/Tidak) : ")
    a = ("Tidak").lower()
    if pilihan == a:
        print("\nPilih opsi kembali: ")
        return menuuser()
    else:
        print("Terima kasih telah berkunjung")
        exit()

## Memulai Pemanggilan def

splashscreen()
login()