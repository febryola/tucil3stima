# class utama yang diperlukan

#class Node untuk simpul dan menyimpan matrix dan parent
class Node:
    #constructor
    def __init__(self, data=None):
        self.puzzle = data
        self.parent = None
        self.dalam = 0

#class untuk mencari solusi puzzle
class Puzzle(object):
    #constructor
    def __init__(self):
        self.queue = []

    #method join untuk menggabungkan 2 matrix
    def __str__(self):
        return '\n'.join([str(i) for i in self.queue])

    #method enqueue untuk menambahkan simpul baru ke queue
    def enqueue(self, data):
        self.queue.append(data)

    #method dequeue untuk menghapus simpul terakhir dari queue
    def dequeue(self):
        index = 0
        #mencari simpul terakhir
        for i in range(len(self.queue)):
            if(self.queue[i][0] < self.queue[index][0]):
                index = i
        #menghapus simpul terakhir
        item = self.queue[index]
        del self.queue[index]
        #mengembalikan simpul terakhir
        return item

