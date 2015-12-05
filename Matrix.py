def set(self,i,j,v):
        self.a[i][j]=v
        return self
    def __eq__(self, other):
        k=True
        if len(self.a)!=len(other.a) and len(self.a[0])!=len(other.a[0]):
            raise RuntimeError
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
        if type(other)==Matrix and len(self.a[0])==len(other.a):
            b=Matrix(len(self.a),len (other.a[0]))
            for i in range(len(self.a)):
                 for j in range(len(other.a[0])):
                    for k in range (len(other.a)):
                        b.a[i][j]+=other.a[k][j]*self.a[i][k]

        elif type(other)==int or type(other)==float:
            for i in range(len(self.a)):
                 for j in range(len (self.a[0])):
                    b.a[i][j]=self.a[i][j]*other
        else:
            raise RuntimeError
        return b
    def __truediv__(self, other):
        b=Matrix(len(self.a),len (self.a[0]))
        for i in range(len(self.a)):
            for j in range(len (self.a[0])):
                 b.a[i][j]=self.a[i][j]/other
        return b
    def determinant(self):
        b=0
        if len(self.a)==len(self.a[0]):
            if len(self.a)==2:
                b=self.a[0][0]*self.a[1][1]-self.a[1][0]*self.a[0][1]
            if len(self.a)==3:
                  b=self.a[0][0]*self.a[1][1]*self.a[2][2]+self.a[0][1]*self.a[1][2]*self.a[2][0]+self.a[0][2]*self.a[1][0]*self.a[2][1]
                  b+=-self.a[0][2]*self.a[1][1]*self.a[2][0]-self.a[2][1]*self.a[1][2]*self.a[0][0]-self.a[2][2]*self.a[1][0]*self.a[0][1]
        else:
            raise RuntimeError
        return b
    def invert(self):
        if len(self.a)==len(self.a[0]):
            b=Matrix(len(self.a),len (self.a[0]))
            if len(self.a)==2:
                b.a[0][0]=-1*self.a[1][1]
                b.a[1][0]=1*self.a[1][0]
                b.a[0][1]=1*self.a[0][1]
                b.a[1][1]=-1*self.a[0][0]
        return b

