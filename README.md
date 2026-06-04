jadi pada tool kali ini hanya bekerja pada perangkat sesama linux, lebih bekerja optimal pada linux debian versi 12 dan versi debian lainnya
pada repository ini ada 2 folder berbeda, yang isinya adalah sistem untuk perangkat commander dan sistem untuk perangkat node

commander adalah perangkat yang bekerja mengontrol node melalui terminal
node adalah perangat yang bekerja mengikuti yang diberikan oleh commander

untuk penggunaan, pertama-tama kalian tentukan perangkat yang menjadi commander dan prangkat yang akan menjadi node
setelah ditentukan, unduh paket dari repositori ini, ambil sesuai perang perangkat yang telah ditentukan
commander bakal mengambil file COMMANDER_SYSTEM_1.0, node bakal mengambil file NODE_SYSTEM_1.0
saya ingatkan kembali kedua sistem tersebut hanya bekerja pada linux terutama debian
setelah mengunduh paket sesuai peran perangkat, kita mulai dari membangun tool ini pada perangkat commander
pada perangkat commander kalian perlu install paket python3, jelas karena tool ini dibuat dengan mengunakan python3
setelah itu, kelian buatlah sebuah direktory /Commander_PC
pada direktori /Commander_PC, letakan direktori COMMANDER_SYSTEM_1.0/
setelah di letakan, kalian ubah perizinan file menggunakan chmod, jadi jalankan chmod +x /Commander_PC -R
setelah itu, kalian jalankan command : ln -s /Commander_PC/COMMANDER_SYSTEM_1.0/Commander /usr/local/bin/Commander
pada perangkat commander telah bisa digunakan tool nya, untuk menggunakan toolnya, cukup ketikan perintah pada terminal :
root@Debian:/# Commander
secara otomatis tool commander pc bekerja

sekarang kita konfigurasi sistemnya pada perangkat node :
pada perangkat node kalian perlu install python3 dan sudo
kemudian, kalian buat sebuah direktori pada folder /opt/System_node/
unduh direktori NODE_SYSTEM_1.0, dan letakan direktori tersebut dalam direktori /opt/System_node/ (kalian bisa langsung git clone untuk mengambil direktori NODE_SYSTEM_1.0 dari direktori /opt/System_node/ kalau tidak mau ribet)
jika hal tadi telah di lakukan, kalian edit code file pada System_node.py
pada baris 10, kalian ganti nilai pada Identitas_Node = 'Nama_Node = PC_Node_1 | ID_Node = 000001', fokus pada 'PC_Node_1' dan '000001', untuk bagian itu kalian bisa ganti terserah dengan kalian
karena disini kalian memberikan identitas pada node yang bakal kalian kontrol nantinya
setelah mengedit file .py tadi, kalian jalankan perintah pada terminal : root@Debian:/# chmod +x /opt -R
setelah itu kalian jalankan lagi perintah pada terminal : root@Debian:/# cp /opt/System_node/NODE_SYSTEM_1.0/System_node.service /etc/systemd/system/
setelah itu kalian jalankan lagi perintah pada terminal : 
root@Debian:/# systemctl daemon-reload
root@Debian:/# systemctl enable System_node.service
root@Debian:/# systemctl restart System_node.service
root@Debian:/# systemctl status System_node.service
pastikan hasilnya running atau tidak ada eror ketika di cek statusnya

dan tool Commander_pc v1.0 telah terpasang dan siap untuk di gunakan pada perankat commander
pada perangkat node, sistemnya otomatis berjalan di background sistem, jadi otomatis menyala saat node di nyalakan
jadi admin tinggal menggunakn perintah Commander pada terminal perangkat Commander, setelah itu tinggal ikuti proses yang berjalan otomatis pada tool tersebut
selamat menggunakan :)
