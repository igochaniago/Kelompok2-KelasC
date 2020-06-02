#===================================================================
#KesehatanFinansial v1.0
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
#Versi ini merupakan pengembangan awal
#
#List Fitur:
#   +Penggunaan CSV module untuk menyimpan data input di file .csv
#   +Penggunaan Datetime module sebagai sistem penanggalan
#   +Penggunaan Time module agar mempermudah saat dijalankan langsung dari klik programnya
#   +Penggunaan Operator module untuk mengurutkan data sesuai tanggal input dengan fungsi sorted()
#   +Penggunaan Getpass module untuk proses Login yang lebih aman
#   +Penggunaan system("cls") yang menghasilkan interface pada prompt lebih nyaman
#   +Dapat dijalankan langsung dari file .py nya tanpa perlu starting prompt terlebih dahulu 
#    dan program tidak autobreak sehingga memudahkan user apabila menggunakan 
#    tanpa melalui starting prompt
#
#Saran dan Masukan untuk pengembangan sangat diperlukan
#Terimakasih
#
#===================================================================
















#======================================
#DEFINISI UNTUK "INPUT PEMBUKUAN"
#======================================
def inputpembukuan():
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
                
                    #global totalsaldo
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
