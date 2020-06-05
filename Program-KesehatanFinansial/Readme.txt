Berikut ini adalah program dari Kelompok 2 Kelas C

nama file program: kesehatan_finansial_kelompok2C.py
===================================================================
			KesehatanFinansial v1.1
===================================================================

Dibuat oleh Kelompok 2 Kelas C

Yustika Kusuma Putri            I0318096
Rudolf Sahat Marisi Marpaung    I0319091
Satrio Fachri Chaniago          I0319096
Yunia Nur Afrasaniy Afina       I0319111
Zahra Humaida Rahman            I0319112
Foncio Flormoy De Jesus Moreira I0319115

Mahasiswa S1 Teknik Industri UNS

LIST FITUR:
   v1.0
	+Penggunaan CSV module untuk menyimpan data input di file .csv
	+Penggunaan Datetime module sebagai sistem penanggalan
	+Penggunaan Time module agar mempermudah saat dijalankan langsung dari klik programnya
	+Penggunaan Operator module untuk mengurutkan data sesuai tanggal input dengan fungsi sorted()
	+Penggunaan Getpass module untuk proses Login yang lebih aman
	+Penggunaan system("cls") yang menghasilkan interface pada prompt lebih nyaman
	+Dapat dijalankan langsung dari file .py nya tanpa perlu starting prompt terlebih dahulu 
    dan program tidak autobreak sehingga memudahkan user apabila menggunakan tanpa melalui starting prompt
   
   v1.1
	+Ada opsi untuk melihat file bulanan yang dikelola oleh program

SYARAT JALANNYA PROGRAM(Requirements):
	+Terdapat python serta environmentnya terinstall di PC
	
CARA MENJALANKAN PROGRAM:
	+Melalui Command Prompt (cmd)
		Sebagai contoh, apabila program terletak di Local Disk D dalam Folder "Kesehatan Finansial"
		1. Ketik | d: ,kemudian klik ENTER
		2. Ketik | cd Kesehatan Finansial ,kemudian klik ENTER
		3. Ketik | python kesehatan_finansial_kelompok2C.py ,kemudian klik ENTER
		4. Masukkan Username dan Password
		5. Lalu program akan berjalan
	
	+Melalui Windows Powershell
		Sebagai contoh, apabila program terletak di Local Disk D dalam Folder "Kesehatan Finansial"
		1. Ketik | d: ,kemudian klik ENTER
		2. Ketik | cd ("Kesehatan Finansial") ,kemudian klik ENTER
		3. Ketik | python kesehatan_finansial_kelompok2C.py ,kemudian klik ENTER
		4. Masukkan Username dan Password
		5. Lalu program akan berjalan

	+Langsung Klik file program kesehatan_finansial_kelompok2C.py
		1. Layaknya membuka suatu aplikasi, yaitu dengan mengklik langsung file program
		2. Masukkan Username dan Password
		3. Lalu program akan berjalan

HAL YANG HARUS DIPERHATIKAN:
	+Program HARUS berada satu folder dengan financepass.txt
	+File Pembukuan tersimpan dalam file .csv yang dinamakan "Pembukuan (Tahun) (Bulan).csv"
	+File Pembukuan akan terbentuk secara otomatis apabila dalam satu folder tidak ada File berkaitan bulan ataupun tahun inputnya
	+File Pembukuan harus tersimpan dalam satu folder yang sama dengan program agar dapat terbaca oleh program


========================
Untuk Keperluan Review
========================
Terdapat file pendukung:
  +financepass.txt (HARUS DALAM SATU FOLDER DENGAN PROGRAM)
  +Pembukuan 2020 01 (Opsional) karena jika tidak ada ini maka akan otomatis membuat file csv baru
  +Pembukuan 2020 05 (Opsional) ---sama dengan atas---
  +Pembukuan 2020 06 (Opsional) ---sama dengan atas---

File pendukung tersebut disertakan untuk keperluan ujicoba program dan mereview jalannya program

Hanya satu file yaitu financepass.txt yang harus terus bersama dalam satu folder karena itu adalah kunci untuk login ke program
  Untuk ujicoba: Username = admin
                 Password = admin123

File Pembukuan yang disertakan merupakan keperluan ujicoba, hal ini dapat otomatis terbuat sendiri saat input apabila tidak dalam satu 
folder dengan Program
