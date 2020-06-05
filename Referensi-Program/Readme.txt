Berikut ini adalah referensi program yang digunakan untuk penyusunan program kelompok

Dalam penggunaan referensi program yang dicantumkan, kami tidak menggunakan satu program full yang kemudian dimodifikasi, melainkan 
menggunakan beberapa bagian dari berbagai program yang dianggap memenuhi keperluan kami untuk menyusun program

Dalam menyusun Program ini, bahan riset kami berasal dari website:
	StackOverflow
	W3School
	GeeksForGeeks
	PythonCentral
	RealPython
	
Referensi Program yang dicantumkan
1. Penggunaan fitur Login
	Tercantum dalam	: Definisi Login.png
					          Definisi Login(2).png
	Berasal dari	  : https://stackoverflow.com/questions/28483113/simple-login-function-in-python
	Keterangan		  : Dalam penggunaan referensi ini, kami memodifikasi bagian
                    +us, pw = line.strip().split("|") menjadi us, pw = line.strip().split(",")
                      Hal ini dilakukan untuk mempermudah dan menyederhanakan dalam karakter yang memisahkan us dan pw 
                      dari (|)garis menjadi menggunakan (,)koma

                    +if (user in us) and (passw in pw) menjadi if (username == us) and (password == pw)
                      Hal ini dilakukan agar Program dapat menyesuaikan apa yang ada dalam financepass.txt

                    +Mengubah isi dari def main()
                      Perubahan ini didasari pada Definisi Login(2).png yaitu menghilangkan tulisan login()
                      karena menyebabkan penumpukan definisi, dimana hal ini tidak diinginkan

2. Penggunaan module getpass
	Tercantum dalam	: Penggunaan getpass.png
	Berasal dari	  : https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/
	Keterangan		  : Dalam penggunaan referensi ini
                    +Hanya menggunakan bagian getpass.getpass saja
                      Dalam password = getpass.getpass("Masukkan Password: ") di def login() digunakan getpass.getpass
                      untuk menggunakan module getpass yang sebelumnya sudah diimport
                      Hal ini dilakukan agar saat user memasukkan Password maka tulisan tidak akan terlihat, dan ini meningkatkan 
                      keamanan penggunaan program karena program ini berkaitan dengan catatan personal yaitu catatan keuangan personal

3. Penggunaan listdir()
	Tercantum dalam : Penggunaan listdir() untuk listing file yang dikelola.png
	Berasal dari 	  : https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
	Keterangan		  : Dalam penggunaan referensi ini, kami memodifikasi bagian
                    +for file in os.listdir("/mydir") menjadi for daftarfile in filelist
                      Hal ini dilakukan karena pada line sebelumnya sudah terdapat definisi filelist = os.listdir()

                    +os.listdir("/mydir") menjadi os.listdir()
                      Hal ini dilakukan karena semua file yang berkaitan sudah ada dalam satu folder yang sama

                    +if file.endswith(".txt") menjadi if daftarfile.endswith(".csv")
                      Hal ini dilakukan karena file yang dimaksud memiliki ekstensi yang sama yaitu .csv bukan .txt

4. Penggunaan sorted() function
	Tercantum dalam	: Penggunaan sort pada csv.png
	Berasal dari	  : https://stackoverflow.com/questions/2100353/sort-csv-by-column
	Keterangan		  : Dalam penggunaan referensi ini, kami memodifikasi bagian
                    +Menambahkan header = next (readCSV)
                      Hal ini dilakukan agar data yang di sortir tidak ikut menyortir kolom header

                    +Mengganti key = operator.itemgetter () dari 3 menjadi 0
                      Hal ini karena kami ingin menyortir data pada kolom pertama, dimana dalam python csv module
                      kolom pertama dianggap sebagai index ke-0

5. Penggunaan time.sleep 
	Tercantum dalam : Penggunaan time sleep.png
	Berasal dari	  : https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
	Keterangan		  : Dalam penggunaan referensi ini
                    +Hanya menggunakan bagian time.sleep()
                      Hal ini dilakukan agar saat menjalankan program langsung dari kesehatan_finansial_kelompok2C.py tanpa 
                      melalui prompt terdapat jeda agar muncul keterangan hasil (output) yang terjadi
                      Kami atur menjadi time.sleep(1) agar terdapat jeda 1 detik
