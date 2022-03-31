from puzzle import Matrix

#mengembalikan true jika puzzle A sama dengan puzzle B
def apakahSama(puzzleA, puzzleB):
    for i in range(4):
        for j in range(4):
            if (puzzleA[i][j] != puzzleB[i][j]):
                return False
    return True

#mengembalikan true jika puzzle sesuai target
def apakahSelesai(matrix, box):
    return apakahSama(matrix, box)

#fungsi untuk sorting queue agar memenuhi priority queue
def sortingQueue(Queue):
    for i in range(len(Queue)):
        for j in range(i+1, len(Queue)):
            if (Queue[i].hitungcost > Queue[j].hitungcost):
                temp = Queue[i]
                Queue[i] = Queue[j]
                Queue[j] = temp

#mengembalikan true jika dalam array dalam puzzle terdapat dalam matrix
def apakahContain(puzzle, matrix):
    for i in puzzle:
        if (apakahSama(i, matrix)):
            return True
    return False

#fungsi untuk menemukan path puzzle
def puzzleSolve(Puzz, calon, Queue):
    awal = Puzz
    calon.append(Puzz.mat)
    end = apakahSelesai(awal.mat, Matrix.box)
    while(not(end)):
        #atur simpul atas
        awal.aturUp()
        if (awal.u != None):
            if (apakahContain(calon, awal.u.mat)):
                Matrix.totalNodes -= 1
                awal.u = None
            else :
                calon.append(awal.u.mat)
                Queue.append(awal.u)
                if (apakahSelesai(awal.u.mat, Matrix.box)):
                    awal = awal.u
                    break

        #atur bawah
        awal.aturDown()
        if (awal.d != None):
            if (apakahContain(calon, awal.d.mat)):
                Matrix.totalNodes -= 1
                awal.d = None
            else :
                calon.append(awal.d.mat)
                Queue.append(awal.d)
                if (apakahSelesai(awal.d.mat, Matrix.box)):
                    awal = awal.d
                    break

        #atur simpul kiri
        awal.aturLeft()
        if (awal.l != None):
            if (apakahContain(calon, awal.l.mat)):
                Matrix.totalNodes -= 1
                awal.l = None
            else :
                calon.append(awal.l.mat)
                Queue.append(awal.l)
                if (apakahSelesai(awal.l.mat, Matrix.box)):
                    awal = awal.l
                    break

        #atur kanan
        awal.aturRight()
        if (awal.r != None):
            if (apakahContain(calon, awal.r.mat)):
                Matrix.totalNodes -= 1
                awal.r = None
            else :
                calon.append(awal.r.mat)
                Queue.append(awal.r)
                if (apakahSelesai(awal.r.mat, Matrix.box)):
                    awal = awal.r
                    break
        sortingQueue(Queue)
        awal = Queue.popleft()
    return awal