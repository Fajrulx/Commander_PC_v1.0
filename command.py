import socket
import time

def Command():
    while True:
        try:
            minta_ip_node = input('''
    (>_o) Masukan ip address node yang akan diberikan perintah : ''').strip()
            ip_node = minta_ip_node.split('.')
            ip_node_fix = len(ip_node)
            if ip_node_fix != 4:
                print('''
    (!!!) Masukan ip address yang valid
___________________________________________________________________________________________''')
                continue
            if not minta_ip_node:
                print('''
    (!!!) Anda belum memasukan ip address | silahkan masukan ip address node
___________________________________________________________________________________________''')
                continue
            break
        except KeyboardInterrupt:
            print('''

    (!!!) Anda membatalkan program command for node secara paksa (-_-)
___________________________________________________________________________________________''')
            return
    print('''
    Perintah yang bisa di berikan kepada node :
    (1) SHUTDOWN
    (2) RESTART
    (3) SLEEP''')
    while True:
        try:
            minta_perintah = input('''
    (^_^) Masukan nomor pilihan program yang ingin dijalankan pada node (1/2/3) : ''')
            if minta_perintah == '1':
                minta_perintah = 'POWEROFF'
            elif minta_perintah == '2':
                minta_perintah = 'REBOOT'
            elif minta_perintah == '3':
                minta_perintah = 'SUSPEND'
            else:
                print('''
    (!!!) Anda memasukan nomor program yang tidak valid | harap masukan nomor yang benar
___________________________________________________________________________________________''')
                continue
            break
        except KeyboardInterrupt:
            print('''
    (!!!) Anda membatalkan program secara paksa, bye...
___________________________________________________________________________________________''')
            return
    print('''
    (^_^) Target dan perintah telah dilengkapi | Mengirimkan perintah ke node...''')
    mengirim_perintah_node = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mengirim_perintah_node.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    mengirim_perintah_node.sendto(minta_perintah.encode(), (minta_ip_node, 5005))
    mengirim_perintah_node.close()

    mendengarkan_respon_node = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mendengarkan_respon_node.bind(('', 5005))
    durasi_menunggu_respon = 30
    mendengarkan_respon_node.settimeout(durasi_menunggu_respon)
    print('''
    (>_<) Perintah terkirim ke node | menunggu balasan dari node selama 30 detik''')
    try:
        pesan_node, alamat_node = mendengarkan_respon_node.recvfrom(1024)
        pesan_node = pesan_node.decode()
        if pesan_node == 'Siap_laksanakan!':
            print('''
    (^o^) Node says : Perintah bakal dieksekusi dalam 10 detik''')
    except socket.timeout:
        print('''
    Waktu menunggu respon telah habis | Node gagal menerima perintah
___________________________________________________________________________________________''')
    except KeyboardInterrupt:
        print('''
    (!!!) Anda membatalkan proses secara paksa banget!!!
___________________________________________________________________________________________''')