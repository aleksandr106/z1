class Matrix():
    a=[]
    def __init__(self, m, n=None):
        try:
            if n ==None:
                self.a=m
            else:
                self.a=[[0]*n for i in range(m)]
        except ValueError as e:
            print('')



    def get(self,i,j):
        return self.a[i][j]
    def get_m(self):
        return len(self.a)
    def get_n(self):
        return len(self.a[0])
    def get_size(self):
        return (self.get_m,self.get_n)
    def set(self,i,j,v):
        self.a[i][j]=v
        return self
    def __eq__(self, other):
        k=True
        if len(self.a)!=len(other.a) and len(self.a[0])!=len(other.a[0]):
            k=False
        else:
             for i in range(len(self.a)):
                for j in range(len (self.a[0])):
                    if self.a[i][j]!=other.a[i][j]:
                        k=False
        return k
    def __add__(self, other):
        b=Matrix(len(self.a),len (self.a[0]))
        for i in range(len(self.a)):
            for j in range(len (self.a[0])):
                 b.a[i][j]=self.a[i][j]+other.a[i][j]
        return b
    def  transpose(self):
        b=Matrix(len (self.a[0]),len(self.a))
        for i in range(len(self.a)):
            for j in range(len (self.a[0])):
                  b.a[j][i]= self.a[i][j]
        return b
    def __sub__(self, other):
        b=Matrix(len(self.a),len (self.a[0]))
        for i in range(len(self.a)):
            for j in range(len (self.a[0])):
                 b.a[i][j]=self.a[i][j]-other.a[i][j]
        return(b)
    def __mul__(self, other):
        b=Matrix(len(self.a),len (self.a[0]))
        if type(other)==Matrix:
            for i in range(len(self.a)):
                 for j in range(len (self.a[0])):
                    b.a[i][j]=self.a[i][j]*other.a[i][j]
        else:
            for i in range(len(self.a)):
                 for j in range(len (self.a[0])):
                    b.a[i][j]=self.a[i][j]*other
        return b
