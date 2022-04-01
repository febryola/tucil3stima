#import dependency yang dibutuhkan
from puzzle15 import Node, Puzzle
import functionFile
import numpy as np
import time 

#fungsi untuk mencetak header
def header():
    print(""" \033[36m
                     ▀███▀▀▀██▄                            ▀███
 ▄▄▄                   ██   ▀██▄                             ██
▀███   █▄▄▄▄▄▄         ██   ▄██▀███  ▀███  █▀▀▀███ █▀▀▀███   ██   ▄▄█▀██
  ██  ▄█               ███████   ██    ██  ▀  ███  ▀  ███    ██  ▄█▀   ██
  ██  █████▄▄   █████  ██        ██    ██    ███     ███     ██  ██▀▀▀▀▀▀
  ██       ▀██         ██        ██    ██   ███  ▄  ███  ▄   ██  ██▄    ▄
▄████▄█     ██       ▄████▄      ▀████▀███▄███████ ███████ ▄████▄ ▀█████▀
     ███  ▄██
      █████
\033[0m""")

#fungsi untuk mencetak welcoming message
def selamatDatang():
    print("\033[31m==========================================================\033[0m")
    print("\033[34m=========Selamat datang di program solver puzzle==========\033[0m")
    print("\033[31m==========================================================\033[0m")
    print()
    print("\033[33mProgram ini dibuat oleh Febryola Kurnia Putri-13520140 K02\033[0m")
    print("\033[37mProgram ini dibuat untuk memenuhi tugas mata kuliah IF2211\033[0m")
    print("\033[31m==========================================================\033[0m")

#fungsi untuk mencetak terima kasih
def terimakasih():
    print("""\033[36m
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄    ▄▄▄   ▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ ▄▄   ▄▄ 
█       █       █   ▄  █ █   █  █▄█  █      █  █   █ █ █      █       █   █  █ █  █
█▄     ▄█    ▄▄▄█  █ █ █ █   █       █  ▄   █  █   █▄█ █  ▄   █  ▄▄▄▄▄█   █  █▄█  █
  █   █ █   █▄▄▄█   █▄▄█▄█   █       █ █▄█  █  █      ▄█ █▄█  █ █▄▄▄▄▄█   █       █
  █   █ █    ▄▄▄█    ▄▄  █   █       █      █  █     █▄█      █▄▄▄▄▄  █   █   ▄   █
  █   █ █   █▄▄▄█   █  █ █   █ ██▄██ █  ▄   █  █    ▄  █  ▄   █▄▄▄▄▄█ █   █  █ █  █
  █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄█▄█   █▄█▄█ █▄▄█  █▄▄▄█ █▄█▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█▄▄█ █▄▄█

    \033[0m""")

#fungsi untuk menginputkan puzzle
def masukanPuzzle():
    print("\n\033[32mPilih opsi untuk memasukkan puzzle: \033[0m")
    print("1. Masukan dari console")
    print("2. Masukan dari file")
    x = int(input("\033[48mMasukkan nomor pilihan : \033[0m"))
    if (x == 1):
        print()
        print("""Masukkan 4 baris puzzle yang dipisahkan dengan spasi
contoh : \n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 0\n""")
        print("\033[33mMasukkan puzzle \033[0m: ")
        puzzle = functionFile.consoleToPuzzle()
    else :
        print("\033[36mfile testing dimasukkan ke folder test\033[0m")
        print("contoh masukan: test1.txt")
        filename = str(input("\033[36mMasukkan nama file \033[0m: "))
        sebelum = "./test/"
        puzzle = functionFile.fileToPuzzle(sebelum+filename)
    return puzzle

#fungsi utama
def main():
    #puzzle awal
    puzzleAwal = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]).reshape(4,4) 
    #inputkan puzzle
    puzzle = masukanPuzzle()
    print ("\033[35m\n\n=================== \033[33mInisialisasi Puzzle\033[0m \033[35m==================\033[0m")
    #inisialisasi puzzle
    a,b = functionFile.cekApakahKosong(puzzle)
    #jika puzzle kosong
    print("\033[31mUbin Kosong Berada Pada Koordinat ("+str(a)+","+str(b)+")\033[0m")
    #mencetak cost awal
    print("\033[31mCost : "+str(functionFile.hitungCost(0,puzzle,puzzleAwal))+"\033[0m")
    #mencetak puzzle
    functionFile.cetakPuzzle(puzzle)
    print("\033[33m==========================================================\033[0m")
    print("\033[35mBerikut Fungsi Kurang setiap Box\n\033[0m")
    functionFile.cetakFungsiKurang(puzzle)
    print("\033[31mSigma Kurang(i) + X = " + str(functionFile.result(puzzle))+"\033[0m")
    perpindahan = ("right","down", "left", "up")
    print("\n\033[33m==========================================================\033[0m")
    
    if(functionFile.solvable(puzzle)):#jika puzzle solvable
        Queue = Puzzle()#inisialisasi queue
        print("\033[32mPuzzle dapat diselesaikan :))\033[0m\n")
        simpul_yang_dibangkitkan = 0 #inisialisasi simpul yang dibangkitkan
        print("Puzzle Awal")
        simpul = Node(puzzle) #inisialisasi simpul awal

        start = time.time() #waktu mulai
        Queue.enqueue((functionFile.hitungCost(0,simpul.puzzle,puzzleAwal),simpul,"",0))
        #enqueue simpul awal
        Queue_temp = Queue.dequeue()
        simpul = Queue_temp[1] #inisialisasi simpul awal
        New_puzzle = simpul.puzzle #inisialisasi puzzle awal
        Move_balik = "" #inisialisasi move balik
        next_step = Queue_temp[3] + 1 #inisialisasi next step
        simpul_yang_dibangkitkan += 1 #simpul yang dibangkitkan

        while(not functionFile.apakahSama(New_puzzle, puzzleAwal)): #jika puzzle tidak sama dengan puzzle awal
            for mov in perpindahan: #mengulang perpindahan
                if(mov != Move_balik): #jika move tidak sama dengan move balik
                    after_move = functionFile.move(New_puzzle,mov) #pindahkan puzzle
                    if(not functionFile.apakahSama(after_move,New_puzzle)): #jika puzzle tidak sama dengan puzzle awal
                        new_simpul = Node(after_move) #inisialisasi simpul baru
                        new_simpul.parent = simpul #inisialisasi parent
                        new_simpul.dalam = simpul.dalam + 1 #inisialisasi dalam
                        simpul_yang_dibangkitkan += 1 #simpul yang dibangkitkan
                        Queue.enqueue((functionFile.hitungCost(next_step,new_simpul.puzzle,puzzleAwal),new_simpul,mov,next_step))      
            #jika sudah tidak ada simpul yang dapat dibangkitkan
            Queue_temp = Queue.dequeue()
            simpul = Queue_temp[1]
            New_puzzle = simpul.puzzle
            Move= Queue_temp[2]
            Move_balik = functionFile.move_mirror(Move)
            next_step = Queue_temp[3] + 1

        #jika sudah sama dengan puzzle awal
        end = time.time() #waktu selesai
        functionFile.cetakPuzzle(puzzle) #cetak puzzle
        functionFile.cetakPath(simpul) #cetak path
        waktu = end - start #waktu yang ditempuh
        print("\n\033[32mJumlah Langkah = " +str(next_step-1)+"\033[0m")  #jumlah langkah
        print("\033[33mWaktu Eksekusi = " +str(waktu) + " seconds" + "\033[0m")  #waktu eksekusi  
        print("\033[34mJumlah Simpul yang Dibangkitkan = " + str(simpul_yang_dibangkitkan)+ "\033[0m")
    else: #jika puzzle tidak solvable
        print("\033[34mPuzzle tidak dapat diselesaikan karena sigma Kurang(i) + X bernilai ganjil!\033[0m\n")
    
    lanjut = str(input("\n\033[35mApakah Anda ingin melanjutkan program \033[0m? (y/n) "))
    #jika lanjut
    if (lanjut == "Y" or lanjut == "y"):
        print()
        main() #panggil fungsi utama
    else:
        terimakasih() #terimakasih
        exit() #keluar

if __name__ == "__main__": #jika program dijalankan
    header() #cetak header
    selamatDatang() #cetak selamat datang
    main() #panggil fungsi utama
    terimakasih() #terimakasih