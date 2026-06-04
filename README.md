#  jadi pada tool kali ini hanya bekerja pada perangkat sesama linux, lebih bekerja optimal pada linux debian versi 12 dan    versi debian lainnya.

===========================================================================================================================
~ commander adalah perangkat yang bekerja mengontrol node melalui terminal
~ node adalah perangat yang bekerja mengikuti yang diberikan oleh commander
===========================================================================================================================

#  untuk penggunaan, pertama-tama kalian tentukan perangkat yang menjadi commander dan prangkat yang akan menjadi node
   setelah ditentukan. 
===========================================================================================================================
#   ambil file sesuai peran perangkat yang telah ditentukan
  ~ commander bakal mengambil file [Commander, main.py, scan.py, command.py]
  ~ node bakal mengambil file [System_node.py,System_node.service]
  
! saya ingatkan kembali kedua sistem tersebut hanya bekerja pada linux terutama debian

1. setelah mengunduh paket sesuai peran perangkat, kita mulai dari membangun tool ini pada perangkat commander
2. pada perangkat commander kalian perlu install paket python3, jelas karena tool ini dibuat dengan mengunakan python3
3. setelah itu, kelian buatlah sebuah direktory /Commander_PC
4. pada direktori /Commander_PC, letakan file [Commander, main.py, scan.py, command.py]
5. setelah di letakan, kalian ubah perizinan file menggunakan chmod, jadi jalankan chmod +x /Commander_PC -R
6. setelah itu, kalian jalankan command : root@Debian:/# ln -s /Commander_PC/Commander /usr/local/bin/Commander
7. pada perangkat commander telah bisa digunakan tool nya, untuk menggunakan toolnya, cukup ketikan perintah pada terminal 
   root@Debian:/# Commander
   secara otomatis tool commander pc bekerja

! sekarang kita konfigurasi sistemnya pada perangkat node :
1. pada perangkat node kalian perlu install python3 dan sudo
2. kemudian, kalian buat sebuah direktori pada folder /opt/System_node/
3. unduh file [System_node.py,System_node.service], dan letakan direktori tersebut dalam direktori /opt/System_node/          (kalian bisa langsung git clone untuk mengambil file [System_node.py,System_node.service] dari direktori                   /opt/System_node/ kalau tidak mau ribet)
4. jika hal tadi telah di lakukan, kalian edit code file pada System_node.py
5. pada baris 10, kalian ganti nilai pada Identitas_Node = 'Nama_Node = PC_Node_1 | ID_Node = 000001', fokus pada             'PC_Node_1' dan '000001', untuk bagian itu kalian bisa ganti terserah dengan kalian karena disini kalian memberikan        identitas pada node yang bakal kalian kontrol nantinya
6. setelah mengedit file .py tadi, kalian jalankan perintah pada terminal : root@Debian:/# chmod +x /opt -R
7. setelah itu kalian jalankan lagi perintah pada terminal :
   root@Debian:/# cp /opt/System_node/System_node.service /etc/systemd/system/
8. setelah itu kalian jalankan lagi perintah pada terminal : 
   root@Debian:/# systemctl daemon-reload
   root@Debian:/# systemctl enable System_node.service
   root@Debian:/# systemctl restart System_node.service
   root@Debian:/# systemctl status System_node.service
   pastikan hasilnya running atau tidak ada eror ketika di cek statusnya

! dan tool Commander_pc v1.0 telah terpasang dan siap untuk di gunakan pada perankat commander
  pada perangkat node, sistemnya otomatis berjalan di background sistem, jadi otomatis menyala saat node di nyalakan
  jadi admin tinggal menggunakn perintah Commander pada terminal perangkat Commander, setelah itu tinggal ikuti proses       yang berjalan otomatis pada tool tersebut selamat menggunakan :)
