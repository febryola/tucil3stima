import copy

#kelas Matrix
class Matrix:
    # konstruk isi matrix dan nodes awal
    box = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
    totalNodes = 0
    
    #fungsi untuk konstruktor
    def __init__(puzzle):
        Matrix.totalNodes += 1
        puzzle.u = None #atas
        puzzle.l = None #kiri
        puzzle.d = None #bawah
        puzzle.r = None #kanan
        puzzle.path = ""        #inisialisasi awal path
        puzzle.hitungcost = 0   #inisialisasi awal fungsi cost
        puzzle.mat = [[0 for i in range(4)] for i in range(4)] #inisialisasi awal nilai matrix
        puzzle.basis = (0,0)    #inisialisasi basis

    #fungsi untuk mengenerate sumpul jika matrix yang kosong digeser ke atas
    def aturUp(puzzle):
        if (puzzle.basis[0] - 1 >= 0):
            Matrix.totalNodes += 1
            puzzle.u = copy.deepcopy(puzzle)
            puzzle.u.mat[puzzle.basis[0]][puzzle.basis[1]] = puzzle.u.mat[puzzle.basis[0] - 1][puzzle.basis[1]]
            puzzle.u.path  += "u"
            puzzle.u.hitungcost = puzzle.u.hitungCost() + len(puzzle.u.path)
            puzzle.u.mat[puzzle.basis[0] - 1][puzzle.basis[1]] = 0 
            puzzle.u.basis = (puzzle.basis[0] - 1 , puzzle.basis[1])

    #fungsi untuk mengenerate simpul jika Matrix yang kosong digeser ke bawah
    def aturDown(puzzle):
        if (puzzle.basis[0] + 1 <= 3):
            Matrix.totalNodes += 1
            puzzle.d = copy.deepcopy(puzzle)
            puzzle.d.mat[puzzle.basis[0]][puzzle.basis[1]] = puzzle.d.mat[puzzle.basis[0] + 1][puzzle.basis[1]]
            puzzle.d.path  += "d"
            puzzle.d.hitungcost = puzzle.d.hitungCost() + len(puzzle.d.path)            
            puzzle.d.mat[puzzle.basis[0] + 1][puzzle.basis[1]] = 0 
            puzzle.d.basis = (puzzle.basis[0] + 1 , puzzle.basis[1])

    #fungsi untuk mengenerate simpul jika matrix yang kosong digeser ke kiri
    def aturLeft(puzzle):
        if (puzzle.basis[1] - 1 >= 0):
            Matrix.totalNodes += 1
            puzzle.l = copy.deepcopy(puzzle)
            puzzle.l.mat[puzzle.basis[0]][puzzle.basis[1]] = puzzle.l.mat[puzzle.basis[0]][puzzle.basis[1] - 1]
            puzzle.l.path  += "l"
            puzzle.l.hitungcost = puzzle.l.hitungCost() + len(puzzle.l.path)            
            puzzle.l.mat[puzzle.basis[0]][puzzle.basis[1] - 1] = 0 
            puzzle.l.basis = (puzzle.basis[0] , puzzle.basis[1] - 1)

    #fungsi untuk mengenerate simpul jika Matrix yang kosong digeser ke kanan
    def aturRight(puzzle):
        if (puzzle.basis[1] + 1 <= 3):
            Matrix.totalNodes += 1
            puzzle.r = copy.deepcopy(puzzle)
            puzzle.r.mat[puzzle.basis[0]][puzzle.basis[1]] = puzzle.r.mat[puzzle.basis[0]][puzzle.basis[1] + 1]
            puzzle.r.mat[puzzle.basis[0]][puzzle.basis[1] + 1] = 0 
            puzzle.r.basis = (puzzle.basis[0] , puzzle.basis[1] + 1)
            puzzle.r.path  += "r"
            puzzle.r.hitungcost = puzzle.r.hitungCost() + len(puzzle.r.path)

    #fungsi untuk menghitung cost tiap simpul
    def hitungCost(puzzle):
        hitung  = 0
        for i in range(4):
            for j in range(4):
                if (puzzle.mat[i][j] != Matrix.box[i][j]):
                    hitung += 1
        return hitung;

    #fungsi untuk menerima input dari console
    def inputFromConsole(puzzle):
        for i in range(4):
            temp = str(input())
            puzzle.mat[i] = temp.split()
            for j in range(4):
                puzzle.mat[i][j] = int(puzzle.mat[i][j])
                if (puzzle.mat[i][j] == 0):
                    puzzle.basis = (i,j)
                if (puzzle.mat[i][j] != Matrix.box[i][j]):
                    puzzle.hitungcost += 1

    #fungsi untuk mengecek apakah puzzle dapat diselesaikan atau tidak
    def isSolve(puzzle):
        hitung = 0
        temp = []
        for i in range(4):
            for j in range(4):
                if (puzzle.mat[i][j] == 0):
                    temp.append(16)
                else :
                    temp.append(puzzle.mat[i][j])
        for i in range(len(temp)):
            for j in range(i+1, len(temp)):
                if (temp[i] > temp[j]):
                    hitung += 1
        if ((puzzle.basis[0] + puzzle.basis[1]) % 2 == 1):
            hitung += 1
        print("\nKurang(i): ", hitung)
        if (hitung % 2 == 0):
            return True
        else:
            return False

    #fungsi yang mengembalikan true jika matrix yang dimasukkan valid
    def isInputValid(puzzle):
        valid = [0 for i in range(16)]
        for i in range(4):
            for j in range(4):
                if (puzzle.mat[i][j] < 0 or puzzle.mat[i][j] > 15):
                    return False
                else :
                    valid[puzzle.mat[i][j]] += 1
        for i in valid:
            if (i == 0):
                return False
        return True

    #fungsi untuk membaca dari file
    def readFile(puzzle, filename):
        f = open(filename, "r")
        for i in range(4):
            isi = f.readline()
            puzzle.mat[i] = isi.split()
            for j in range(4):
                puzzle.mat[i][j] = int(puzzle.mat[i][j])
                if (puzzle.mat[i][j] == 0):
                    puzzle.basis = (i,j)
                if (puzzle.mat[i][j] != Matrix.box[i][j]):
                    puzzle.hitungcost += 1
        f.close()

    #fungsi untuk mencetak Matrix
    def printMatrix(puzzle):
        for i in puzzle.mat:
            for j in range(4):
                print(i[j], end = " ")
            print()
        print("Total Simpul : ", Matrix.totalNodes)
        print("Basis : ", puzzle.basis[0], puzzle.basis[1])
        print("Path : ", puzzle.path)
        print("Cost : ", puzzle.hitungcost)

    #fungsi untuk mencetak basis
    def printBasis(puzzle):
        print(puzzle.basis[0] , puzzle.basis[1])

    #fungsi untuk mencetak path
    def printPath(puzzle):
        print(puzzle.path)
    
    #fungsi untuk mencetak cost
    def printCost(puzzle):
        print(puzzle.hitungcost)

    #fungsi untuk mencetak total simpul
    def printTotalNodes(puzzle):
        print(Matrix.totalNodes)
    