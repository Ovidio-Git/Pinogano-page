class Chivo:

    def __init__(self, vector, start=None, finish=None):
        self._vector = vector
        self._start  = start
        self._finish = finish
        self.selectionSort()
       
    def _readfile(self):
        aux = self._vector.split()
        new =  aux[0].replace(',',' ')
        aux = new.split()
        setdata = [int(aux[i]) for i in range(0,len(aux))]
        return setdata
              
    def selectionSort(self):
        array = self._readfile()
        n = len(array)
        for i in range(n - 1):
            menor = i
            for j in range(i + 1, n):
                if array[j] < array[menor]:
                    menor = j
            array[i], array[menor] = array[menor], array[i]
        return array

    def Genders(self, data):
        self._data = data
        genders = ['Hembra' if self._data[i] <= 80 else 'Macho' for i in range(len(self._data))]
        return genders

    def Compare(self):
        target = self.selectionSort()
        base = [num for num in range(int(self._start),int(self._finish))]
        A = set(base)
        B = set(target)
        C = list(A.difference(B))
        return C
    
   