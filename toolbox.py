class Chivo:


    def __init__(self, vector)
        self._vector=vector
    
    def readfile(self,file):
        self._file=file

        aux = file1.read().split()
        new =  aux[0].replace(',',' ')
        aux = new.split()
        setdata = [int(aux[i]) for i in range(0,len(aux))]
        return setdata
              
    def selectionSort(self,vector):
        self._vector=vector
        n = len(vector)
        for i in range(n - 1):
            menor = i
            for j in range(i + 1, n):
                if vector[j] < vector[menor]:
                    menor = j
            vector[i], vector[menor] = vector[menor], vector[i]

