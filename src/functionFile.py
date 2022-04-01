#import dependency yang dibutuhkan
import numpy as np

#fungsi untuk mengeksport console ke puzzle
def consoleToPuzzle():
    puzzle = [[0] * 4 for _ in range(4)]
    for i in range(4):
        lines = list(map(int, input().split()))
        for j in range(4):
            puzzle[i][j] = lines[j]
    puzzles = np.reshape(puzzle,(4,4)).astype('int32')
    #Mengembalikan puzzle
    return puzzles

#fungsi untuk membaca file
def readFile(filename):
    f = open(filename,"r") 
    return f

#fungsi untuk mengubah file ke puzzle
def fileToPuzzle(filename):
    text = readFile(filename)
    temp = text.read().split()
    puzzle = np.reshape(temp,(4,4)).astype('int32')
    return puzzle

#fungsi untuk mencetak path
def cetakPath(simpul):
    if(simpul.parent == None):
        return
    cetakPath(simpul.parent)
    print("\033[35m\n==============================\033[0m")
    print("\033[31mLangkah ke - "+str(simpul.dalam)+" : "+"\033[0m")
    #cetak puzzle
    cetakPuzzle(simpul.puzzle)

#fungsi untuk mencetak puzzle
def cetakPuzzle(puzzle):
    print("\033[34m╔═══╦═══╦═══╦═══╗\033[0m")
    for i in range(4):
        for j in range(4):
            print("\033[34m║\033[0m ",end="")
            print(puzzle[i][j], end="")
            if(puzzle[i][j] < 10):
                print(" ", end="")
        print("\033[34m║\033[0m")
        if(i != 3):
            print("\033[34m╠═══╬═══╬═══╬═══╣\033[0m")
    print("\033[34m╚═══╩═══╩═══╩═══╝\033[0m")

#fungsi untuk mengecek apakah puzzle kosong
def cekApakahKosong(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 0):
                row = i
                column = j
    return row,column

#fungsi untuk mengubah angka 0 menjadi posisi yang seharusnya
def ubahAngka0(puzzle):
    x,y = cekApakahKosong(puzzle)
    puzzle[x][y] = 16
    return puzzle       

#fungsi untuk mencari nilai x
def temukanX(puzzle):
    puzzle_temp = puzzle.copy()
    x,y = cekApakahKosong(puzzle_temp)
    sum = x+y
    return (sum % 2)

#fungsi untuk menghitung cost
def hitungCost(dalam,puzzle,mat):
    hitung = 0
    for i in range(4):
        for j in range(4):
            if((puzzle[i][j] != mat[i][j]) and puzzle[i][j] != 0):
                hitung += 1
    return (dalam+hitung)

#fungsi untuk mencari nilai fungsi kurang setiap ubin
def fungsiKurang(puzzle):
    hitung = 0
    puzzle_temp = puzzle.copy()
    puzzle_temp = ubahAngka0(puzzle_temp)
    puzzle_temp = np.reshape(puzzle_temp,(16,))
    for i in range(16):
        temp = puzzle_temp[i]
        for j in range(i,16):
            if(temp > puzzle_temp[j]):
                hitung += 1
    return hitung

#fungsi untuk mencetak fungsi kurang setiap ubin
def cetakFungsiKurang(puzzle):
    puzzle_temp = puzzle.copy()
    puzzle_temp = ubahAngka0(puzzle_temp)
    puzzle_temp = np.reshape(puzzle_temp,(16,))
    for i in range(16):
        hitung = 0
        temp = puzzle_temp[i]
        for j in range(i,16):
            if(temp > puzzle_temp[j]):
                hitung += 1
        print("Fungsi Kurang("+ str(temp)+") = "+ str(hitung))

#fungsi untuk mencari nilai sum
def result(puzzle):
    sum = temukanX(puzzle)
    sum += fungsiKurang(puzzle)
    return sum

#fungsi untuk menentukan apakah puzzle dapat diselesaikan
def solvable(puzzle):
    sum = result(puzzle)
    if(sum % 2 == 0):
        return True
    else:
        return False

#fungsi untuk menukar posisi puzzle
def swap(puzzle,row,column):
    x,y = cekApakahKosong(puzzle)
    puzzle[x][y] = puzzle[row][column]
    puzzle[row][column] = 0
    return puzzle

#fungsi untuk mencari nilai pindah
def move(puzzle,pindah):
    puzzle_temp = puzzle.copy()
    x,y = cekApakahKosong(puzzle_temp)
    if(pindah == "left"):
        if(y != 0):
            y -= 1
    elif(pindah == "right"):
        if(y != 3):
            y += 1
    elif(pindah == "up"):
        if(x != 0):
            x -= 1
    elif(pindah == "down"):
        if(x != 3):
            x += 1
    puzzle_temp = swap(puzzle_temp,x,y)
    return puzzle_temp

#fungsi untuk mencari lawan dari move
def move_mirror(pindah):
    if(pindah == "left"):
        return "right"
    elif(pindah == "right"):
        return "left"
    elif(pindah == "up"):
        return "down"
    elif(pindah == "down"):
        return "up"

#fungsi untuk mengecek apakah kedua puzzle sama
def apakahSama(puzzle,mat):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] != mat[i][j]):
                return False
    return True

