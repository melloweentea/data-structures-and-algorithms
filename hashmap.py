#isn't this just equivalent to dictionaries tho LMFAOOOO
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)] #100 Nones 
    
    def get_hash(self, key):
        h = 0 
        for char in key:
            h += ord(char) 
            #return the unicode point for a one-character string
            #convert character back by using chr()
        return h % self.MAX 
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == '__main__':
    t = HashTable()
    t["march 9"] = 138 
    t["dec 17"] = 27 
    # print(t.get_hash('march 9'))
    del t["march 9"] # WTFFF HOW DOES THIS WORK
    print(t.arr) #everything is None except for 130 at index 9


