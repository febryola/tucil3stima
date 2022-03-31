from puzzle import Matrix
from function import puzzleSolve
import time
from collections import deque

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

def selamatDatang():
    print("\033[31m==========================================================\033[0m")
    print("\033[34m=========Selamat datang di program solver puzzle==========\033[0m")
    print("\033[31m==========================================================\033[0m")
    print()
    print("\033[33mProgram ini dibuat oleh Febryola Kurnia Putri-13520140 K02\033[0m")
    print("\033[37mProgram ini dibuat untuk memenuhi tugas mata kuliah IF2211\033[0m")
    print("\033[31m==========================================================\033[0m")

def masukanInput(puzzlee):
    print("Pilih opsi untuk memasukkan puzzle: ")
    print("1. Masukan dari console")
    print("2. Masukan dari file")
    x = int(input("\033[48mMasukkan nomor pilihan : \033[0m"))
    if (x == 1):
        print()
        print("""Masukkan 4 baris puzzle yang dipisahkan dengan spasi
contoh : \n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 0\n""")
        print("\033[33mMasukkan puzzle \033[0m: ")
        puzzlee.inputFromConsole()
    else :
        print("\033[36mfile testing dimasukkan ke folder test\033[0m")
        print("contoh masukan: test1.txt")
        filename = str(input("\033[36mMasukkan nama file \033[0m: "))
        sebelum = "./test/"
        puzzlee.readFile(sebelum+filename)

#fungsi untuk mencetak matriks
def printMatriks(mat):
    for i in range(4):
        for j in range(4):
            print(mat[i][j], end = " ")
        print()

#fungsi untuk mencetak path
def printPath(res, puzzle):
    mat = puzzle.mat
    basis = puzzle.basis
    path = res.path
    for i in path:
        if (i == "u"):
            print("\n\033[33mLangkah yang dilakukan\033[0m : up")
            mat[basis[0]][basis[1]] = mat[basis[0] - 1][basis[1]]
            mat[basis[0] - 1][basis[1]] = 0
            basis = (basis[0] - 1, basis[1])
        elif (i == "d"):
            print("\n\033[33mLangkah yang dilakukan\033[0m : down")
            mat[basis[0]][basis[1]] = mat[basis[0] + 1][basis[1]]
            mat[basis[0] + 1][basis[1]] = 0
            basis = (basis[0] + 1, basis[1])
        elif (i == "l"):
            print("\n\033[33mLangkah yang dilakukan\033[0m : left")
            mat[basis[0]][basis[1]] = mat[basis[0]][basis[1] - 1]
            mat[basis[0]][basis[1] - 1] = 0
            basis = (basis[0], basis[1] - 1)
        elif (i == "r"):
            print("\n\033[33mLangkah yang dilakukan\033[0m : right")
            mat[basis[0]][basis[1]] = mat[basis[0]][basis[1] + 1]
            mat[basis[0]][basis[1] + 1] = 0
            basis = (basis[0], basis[1] + 1)
        printMatriks(mat)

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

def main():
    calon = []
    Q = deque()
    puzzlee = Matrix()
    masukanInput(puzzlee)
    print()
    if (not puzzlee.isInputValid()):
        print("\033[34mInputan tidak valid, silakan kembali masukkan Puzzle!\033[0m\n")
        masukanInput(puzzlee)
    print("Inputan Puzzle : ")
    printMatriks(puzzlee.mat)
    if (puzzlee.isSolve()):
        print("\033[33mPuzzle dapat diselesaikan :))\033[0m\n")
        now = time.time()
        Result = puzzleSolve(puzzlee, calon, Q)
        print("\033[36mjumlah langkah : ", len(Result.path))
        print("\033[31mjalur pencarian : ", Result.path)
        print("\033[32mWaktu eksekusi : ", time.time()-now," detik\033[0m\n")
        print("\033[33mjumlah simpul yang dibangkitkan : ", Matrix.totalNodes)
        print()
        cetak = str(input("\033[35mApakah Anda ingin mencetak matriks langkah \033[0m? (y/n) "))
        if (cetak == "Y" or cetak == "y"):
            printPath(Result, puzzlee)    
    else :
        print("\033[34mPuzzle tidak dapat diselesaikan karena fungsi kurang(i) bernilai ganjil!\033[0m\n")
    
    lanjut = str(input("\n\033[35mApakah Anda ingin melanjutkan program \033[0m? (y/n) "))
    if (lanjut == "Y" or lanjut == "y"):
        print()
        main()
    else:
        terimakasih()
        exit()
if __name__ == "__main__":
    header()
    selamatDatang()
    main()
    terimakasih()