class Chivo:

    def __init__(self, vector):
        self._vector = vector
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

