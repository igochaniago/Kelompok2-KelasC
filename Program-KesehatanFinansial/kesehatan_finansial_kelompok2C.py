#===================================================================
#KesehatanFinansial v1.2
#===================================================================
#
#Dibuat oleh Kelompok 2 Kelas C
#
#Yustika Kusuma Putri            I0318096
#Rudolf Sahat Marisi Marpaung    I0319091
#Satrio Fachri Chaniago          I0319096
#Yunia Nur Afrasaniy Afina       I0319111
#Zahra Humaida Rahman            I0319112
#Foncio Flormoy De Jesus Moreira I0319115
#
#Mahasiswa S1 Teknik Industri UNS
#
#List Fitur:
#   v1.0
#   +Penggunaan CSV module untuk menyimpan data input di file .csv
#   +Penggunaan Datetime module sebagai sistem penanggalan
#   +Penggunaan Time module agar mempermudah saat dijalankan langsung dari klik programnya
#   +Penggunaan Operator module untuk mengurutkan data sesuai tanggal input dengan fungsi sorted()
#   +Penggunaan Getpass module untuk proses Login yang lebih aman
#   +Penggunaan system("cls") yang menghasilkan interface pada prompt lebih nyaman
#   +Dapat dijalankan langsung dari file .py nya tanpa perlu starting prompt terlebih dahulu 
#    dan program tidak autobreak sehingga memudahkan user apabila menggunakan tanpa melalui starting prompt
#   v1.1
#   +Ada opsi untuk melihat file bulanan yang dikelola oleh program
#   v1.2
#   +Bug Fixed: ValueError pada saat salah input
#
#Saran dan Masukan untuk pengembangan sangat diperlukan
#Terimakasih
#
#===================================================================
#Import os untuk keperluan file
import os
#Import csv untuk modifikasi csv
import csv
#Import math untuk fungsi matematika
import math
import operator
#Import Sistem Penanggalan
import datetime
import time
#Import getpass untuk keamanaan kata sandi
import getpass
#Import system untuk ("cls") atau terminal clear
from os import system

#======================================
#DEFINISI UNTUK "INPUT PEMBUKUAN"
#======================================
def inputpembukuan():
    try:
        bulanbuku = int(input("Bulan Pembukuan (1-12): "))
        tahunbuku = int(input("Tahun Pembukuan (yyyy): "))
        penanggalanfile = datetime.datetime(tahunbuku, bulanbuku, 1) 
        namafile = f'Pembukuan {penanggalanfile.strftime("%Y %m")}.csv'

        tanggalbuku = int(input("Masukkan TANGGAL (1-31): "))
        penanggalan = datetime.datetime(tahunbuku, bulanbuku, tanggalbuku)

        #Menu untuk input Keterangan Pembukuan
        system ("cls")
        print ("==============================================================================")
        print ("                      PROGRAM PEMBUKUAN FINANSIAL MANDIRI                     ")
        print ("==============================================================================")
        print ("                             KETERANGAN PEMBUKUAN                             ")
        print ("")
        print ("")
        print ("          Tahap ini adalah untuk menuliskan keperluan atau keterangan         ") 
        print ("               yang berkaitan dengan PEMASUKAN atau PENGELUARAN               ")
        print ("")
        print ("Masukkan Keterangan Pembukuan")
        ketbuku = input("> ")

        #Menu untuk memilih apakah mendata Pemasukan atau Pengeluaran
        system ("cls")
        print ("==============================================================================")
        print ("                      PROGRAM PEMBUKUAN FINANSIAL MANDIRI                     ")
        print ("==============================================================================")
        print ("                           PEMASUKAN atau PENGELUARAN                         ")
        print ("")
        print ("")
        print ("                                 Pilih Pembukuan                              ")
        print ("                          Klik (1) untuk data PEMASUKAN                       ")
        print ("                          Klik (2) untuk data PENGELUARAN                     ")
        print ("")
        pilihbuku = input("> ")
        if pilihbuku == ("1"):
            system ("cls")
            print ("==============================================================================")
            print ("                      PROGRAM PEMBUKUAN FINANSIAL MANDIRI                     ")
            print ("==============================================================================")
            print ("                                  PEMASUKAN                                   ")
            print ("")
            print ("")
            print ("Input nominal PEMASUKAN")
            kredit = 0
            debit = int(input("> "))
            print ("")
            print ("INPUT BERHASIL")
            
        elif pilihbuku == ("2"):
            system ("cls")
            print ("==============================================================================")
            print ("                      PROGRAM PEMBUKUAN FINANSIAL MANDIRI                     ")
            print ("==============================================================================")
            print ("                                 PENGELUARAN                                  ")
            print ("")
            print ("")
            print ("Input nominal PENGELUARAN")
            kredit = (int(input("> ")))
            debit = 0
            print ("")
            print ("INPUT BERHASIL")
            
        totalbuku = debit - kredit

        csvheader = ['Tanggal', 'Keterangan Pembukuan', 'Debit', 'Kredit', 'Total']

        #Membuka file csv dalam mode append
        with open(namafile, 'a', newline='\n') as filecsv:

            #dictnilai adalah dictionary digunakan untuk writerow.
            #Mengubah data menjadi dictionary untuk dimasukkan per row
            dictbuku = {'Tanggal': penanggalan.strftime("%d/%m/%Y"), 'Keterangan Pembukuan': ketbuku, 'Debit': debit, 'Kredit': kredit, 'Total': totalbuku}

            writer = csv.DictWriter(filecsv, fieldnames = csvheader)

            #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
            if os.stat(namafile).st_size == 0:
                writer.writeheader()
            else:
                None

            writer.writerow(dictbuku)
            
    except ValueError:
        print ("")
        print ("==============================================================================")
        print ("                      PROGRAM PEMBUKUAN FINANSIAL MANDIRI                     ")
        print ("==============================================================================")
        print ("")
        print ("                          Input yang dimasukkan SALAH                         ")
        print ("")
        print ("                   NOTE: Masukkan Nominal Uang dengan ANGKA                   ") 
        print ("                   NOTE: Masukkan Bulan dan Tahun dengan ANGKA                ")        
        print ("")
        print ("Apakah ingin mengulangi INPUT PEMBUKUAN?")
        print ("(1) YA")
        print ("(2) TIDAK")
        
        lanjut = input ("> ")
        if lanjut == ("1"):
            system ("cls")
            inputpembukuan()
        
        else:
            system ("cls")
            print ("")
            print ("KEMBALI KE MENU AWAL")
            print ("")   
#====================================
#DEFINISI UNTUK OPSI "CEK PEMBUKUAN"
#====================================
def cekpembukuan():
    try:
        bulanbuku = int(input("Bulan Pembukuan (1-12): "))
        tahunbuku = int(input("Tahun Pembukuan (yyyy): "))
        penanggalanfile = datetime.datetime(tahunbuku, bulanbuku, 1) 
        namafile = f'Pembukuan {penanggalanfile.strftime("%Y %m")}.csv'
    
        with open (namafile) as filecsv:
            readCSV = csv.reader (filecsv,delimiter = ',')
            line_count = 0
            header = next (readCSV)
            sortir = sorted (readCSV, key = operator.itemgetter (0))
            print (header)
            totalsaldo = 0
            totaldebit = 0
            totalkredit = 0
            
            if header != None:
                for row in sortir:
                    debit, kredit = float(row[2]), float(row[3])
                    totalpembukuan = debit - kredit
                
                    totaldebit += debit
                    totalkredit += kredit
                    totalsaldo += totalpembukuan 
                
                    line_count += 1
                    jmldata = line_count
                    print (row)
                    
        if totalkredit > 0.8*totaldebit:
            print ("")
            print ("Jumlah Data Pembukuan dalam sebulan: ", jmldata)
            print ("Jumlah PEMASUKAN    : ", totaldebit)
            print ("Jumlah PENGELUARAN  : ", totalkredit)
            print ("Total SALDO saat ini: ", totalsaldo)
            print ("Kesehatan Finansial : BURUK")
                        
        elif totalkredit <= 0.8*totaldebit:
            print ("")
            print ("Jumlah Data Pembukuan dalam sebulan: ", jmldata)
            print ("Jumlah PEMASUKAN    : ", totaldebit)
            print ("Jumlah PENGELUARAN  : ", totalkredit)
            print ("Total SALDO saat ini: ", totalsaldo)
            print ("Kesehatan Finansial : BAIK")
        filecsv.close()  
        kembalimenuawal()
        
    except FileNotFoundError:
        print ("")
        print ("==============================================================================")
        print ("                      PROGRAM PEMBUKUAN FINANSIAL MANDIRI                     ")
        print ("==============================================================================")
        print ("")
        print ("                         Belum ada data yang dimasukkan                       ")
        print ("                                      ATAU                                    ")
        print ("                            Tidak ada File Pembukuan                          ")         
        print ("")
        print ("Apakah ingin mengulangi CEK PEMBUKUAN?")
        print ("(1) YA")
        print ("(2) TIDAK")
        
        lanjut = input ("> ")
        if lanjut == ("1"):
            system ("cls")
            cekpembukuan()
        
        else:
            system ("cls")
            print ("")
            print ("KEMBALI KE MENU AWAL")
            print ("")
            
    except ValueError:
        print ("")
        print ("==============================================================================")
        print ("                      PROGRAM PEMBUKUAN FINANSIAL MANDIRI                     ")
        print ("==============================================================================")
        print ("")
        print ("                          Input yang dimasukkan SALAH                         ")
        print ("")
        print ("                   NOTE: Masukkan Bulan dan Tahun dengan ANGKA                ")         
        print ("")
        print ("Apakah ingin mengulangi CEK PEMBUKUAN?")
        print ("(1) YA")
        print ("(2) TIDAK")
        
        lanjut = input ("> ")
        if lanjut == ("1"):
            system ("cls")
            cekpembukuan()
        
        else:
            system ("cls")
            print ("")
            print ("KEMBALI KE MENU AWAL")
            print ("")
#======================================
#DEFINISI UNTUK CEK FILE YANG DIKELOLA
#======================================
def filedir():
    filelist = os.listdir()
    print ("")
    print ("==============================================================================")
    print ("                      PROGRAM PEMBUKUAN FINANSIAL MANDIRI                     ")
    print ("==============================================================================")
    print ("")
    print ("          Berikut ini adalah File Bulanan yang terdeteksi oleh Program        ")
    print ("             Format Penamaan File adalah: Pembukuan (Tahun) (Bulan)           ")
    print ("")
    print ("Daftar File:")
    for daftarfile in filelist:
        if daftarfile.endswith(".csv"):
            print(os.path.join(daftarfile))
            print ("")
    kembalimenuawal()   
  

#DEFINISI UNTUK PENGULANGAN INTERFACE
def kembalimenuawal():        
        print ("")
        print ("Tekan (1) lalu ENTER untuk Kembali ke MENU AWAL")
        
        lanjut = input ("> ")
        if lanjut == ("1"):
            system ("cls")
            print ("")
            print ("KEMBALI KE MENU AWAL")
            print ("")
        
        else:
            system ("cls")
            None
                       
#======
#Login
#======
def login():    
    system ("cls")
    print ("")
    print ("==============================================================================")
    print ("                      PROGRAM PEMBUKUAN FINANSIAL MANDIRI                     ")
    print ("==============================================================================")
    print ("")
    print ("NB: Saat memasukkan password, huruf yang diketik memang tidak terlihat")
    print ("")
    username = input("Masukkan Username: ")
    password = getpass.getpass("Masukkan Password: ")
    filepass = open("financepass.txt", "r")
    for line in filepass.readlines():
        us, pw = line.strip().split(",")
        if (username == us) and (password == pw):
            print ("")
            print ("Login Berhasil")
            time.sleep(1) 
            return True
    
    system ("cls")
    print ("")
    print ("==============================================================================")
    print ("                      PROGRAM PEMBUKUAN FINANSIAL MANDIRI                     ")
    print ("==============================================================================")
    print ("")
    print ("                             Username atau Password                           ")
    print ("                                      SALAH!                                  ")
    print ("                               PROGRAM TERHENTI!                              ")    
    print ("")
    time.sleep(1) #agar saat dijalankan langsung tanpa melalui prompt tidak langsung tertutup, sehingga menampilkan output terlebih dahulu
    return False


#===============================
#TAMPILAN MUKA AWAL (INTERFACE)
#===============================
def menu():
    system ("cls")
    while True:
        print ("")
        print ("==============================================================================")
        print ("                      PROGRAM PEMBUKUAN FINANSIAL MANDIRI                     ")
        print ("==============================================================================")
        print ("         Program ini digunakan untuk pembukuan finansial secara mandiri       ")
        print ("")
        print ("                     Dalam program ini, kita bisa memonitor:                  ")
        print ("                      +Pemasukan Bulanan                                      ")
        print ("                      +Pengeluaran Bulanan                                    ")
        print ("                      +Kesehatan Finansial Bulanan                            ")
        print ("")
        print ("           Jika terjadi ERROR, klik ctrl + c lalu mulai ulang program         ")
        print ("")
        print ("==============================================================================")
        print ("                                   MENU AWAL                                  ")
        print ("==============================================================================")
        print ("")
        print ("                     Klik (1) untuk INPUT data PEMBUKUAN                      ")
        print ("                     Klik (2) untuk CEK data PEMBUKUAN                        ")
        print ("                     Klik (3) untuk CEK file bulan yang SUDAH dimasukkan      ")
        print ("                     Klik (4) untuk KELUAR dari PROGRAM                       ")
        print ("")
        
        mulai = input("> ")
        if mulai == ("1"):
            system ("cls")
            inputpembukuan()
        
        elif mulai ==("2"):
            system ("cls")
            cekpembukuan()
            
        elif mulai ==("3"):
            system ("cls")
            filedir()   
            
        elif mulai == ("4"):
            system ("cls")
            print ("")
            print ("PROGRAM TERHENTI!")
            print ("")
            time.sleep(1)
            break
            
        else:
            system ("cls")
            print ("")
            print ("Input SALAH!")
            print ("PROGRAM TERHENTI!")
            print ("")
            time.sleep(1)
            break

def main():
    log = login()
    if log == True:
        menu()
        
#================================
#MENJALANKAN KESELURUHAN PROGRAM
#================================
main()
