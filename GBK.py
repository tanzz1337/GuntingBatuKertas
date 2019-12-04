# ================================ #
# GBK = Gunting Batu Kertas              #
# https://github.com/Baturaja1337  #
# ================================ #

import datetime
import os
import random
import time
from typing import Any

# Created Time
tgl = datetime.datetime.now()
match = 1  # type: Any

var_bel = ['GUNTING', 'BATU', 'KERTAS']
poin_com = []
poin_user = []
username = input('Nama Pemain : ')  # type: Any
print("=======================")
print('TIME : ', tgl.strftime("%d"), tgl.strftime("%B"), tgl.strftime("%Y"))
print("=======================")


def help_game():
    print(
        """[ Cara Bermain Gunting Batu Kertas ]
    1. Saat program akan meminta input dari pemain
       contoh : Enter Weapon : GUNTING / BATU / KERTAS
       maka senjata anda adalah Gunting
    2. Program akan secara acak mengeluarkan pilihan
    3. Pertandingan Akan Dimainkan Selama 5x
    4. Setiap Pertandingan memiliki 1 poin,jika anda menang akan mendapat 1 poin 
       namun jika anda kalah makan anda tidak mendapatkan poin atau 0
    5. Poin yang didapat akan di jumlahkan oleh sistem 
    6. Pemain yang mendapatkan skor terbanyak akan dinyatakan sebagai pemenang.""")
    input('Press any key to exit : ')
    os.system('exit')


def start():
    x = random.randint(0, 2)

    global match
    print("=" * 20)
    print('Pertandingan ke :', match)
    print("=" * 20)
    usr = input('Your Weapon : ')
    print("Com Weapon : ", var_bel[x])
    print()

    if usr == 'GUNTING' and x == 0:
        print('Hasil : DRAW')
        print()
        match += 1

    elif usr == 'GUNTING' and x == 1:
        print('HASIL : KALAH')
        poin_com.append(1)
        match += 1
        print()

    elif usr == 'GUNTING' and x == 2:
        print('HASIL : MENANG ')
        poin_user.append(1)
        print()
        match += 1

    elif usr == 'BATU' and x == 0:
        print('HASIL :  MENANG')
        poin_user.append(1)
        print()
        match += 1

    elif usr == 'BATU' and x == 1:
        print('HASIL :  DRAW')
        print()
        match += 1

    elif usr == 'BATU' and x == 2:
        print('HASIL : KALAH')
        poin_com.append(1)
        print()
        match += 1

    elif usr == 'KERTAS' and x == 0:
        print('HASIL : KALAH')
        poin_com.append(1)
        print()
        match += 1

    elif usr == 'KERTAS' and x == 1:
        print('HASIL : MENANG')
        poin_user.append(1)
        print()
        match += 1

    elif usr == 'KERTAS' and x == 2:
        print('HASIL : DRAW')
        print()
        match += 1

    else:
        print('Input Salah ! \n Pastikan Menggunakan Huruf Besar')
        os.system('cls')
        start()


def help():
    # type: () -> object
    print('[ SELAMAT DATANG ', username, ']')
    print('1. START')
    print('2. HELP')
    print('3. EXIT')
    cho = int(input('>>> '))
    if cho == 1:
        start()
        start()
        start()
        start()
        start()
    elif cho == 2:
        help_game()
    elif cho == 3:
        print('Please wait...')
        time.sleep(3)
        os.system('cls')
        os.system('exit')


help()

print()
print()
print("""
=====================
[ SKOR PERTANDINGAN ]
=====================
""")

print('SKOR ANDA     :', len(poin_user))
print('SKOR KOMPUTER :', len(poin_com))
print()

if len(poin_user) > len(poin_com):
    print('Selamat', username, 'Memenangkan Pertandingan ^_^')
elif len(poin_com) > len(poin_user):
    print("Maaf", username, "Kalah Dalam Permainan :( ")
else:
    print("Hasil Pertandingan Draw !")

time.sleep(5)
os.system('cls')
os.system('exit')
