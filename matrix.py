class Matrix:
    counter = 0
    def __init__(self, matrix):
        self.nrows = len(matrix) 
        self.ncols = len(matrix[0])
        self.matrix = matrix
        Matrix.counter += 1

    @classmethod
    def create_matrix(self, nrows : int , ncols : int , default_value = None):
        matrix = []
        
        if default_value is None:
            for i in range(nrows):
                print(f"row {i+1}:")
                row = []
                for j in range(ncols):
                    col = int(input(f"\tEnter Element of index {j+1}: "))                    
                    row.append(col)

                matrix.append(row)

        else:
            for i in range(nrows):
                row = []
                for j in range(ncols):
                    row.append(default_value)

                matrix.append(row)

        return Matrix(matrix)

    def __add__(self , other):
        matrix = []
        
        for i in range(min(self.nrows, other.nrows)):
            matrix.append([])
            for j in range(min(self.ncols, other.ncols)):
                matrix[i].append(self.matrix[i][j] + other.matrix[i][j])

        return Matrix(matrix)
    
    def __sub__(self, other):
        matrix = []
        
        for i in range(min(self.nrows, other.nrows)):
            matrix.append([])
            for j in range(min(self.ncols, other.ncols)):
                matrix[i].append(self.matrix[i][j] - other.matrix[i][j])

        return Matrix(matrix)
    
    def __mul__(self, other):
        matrix = []
        
        for i in range(min(self.nrows, other.nrows)):
            matrix.append([])
            for j in range(min(self.ncols, other.ncols)):
                matrix[i].append(self.matrix[i][j] * other.matrix[i][j])

        return Matrix(matrix)
    
    def __truediv__(self, other):
        matrix = []
        
        for i in range(min(self.nrows, other.nrows)):
            matrix.append([])
            for j in range(min(self.ncols, other.ncols)):
                matrix[i].append(self.matrix[i][j] / other.matrix[i][j])

        return Matrix(matrix)

    
    def __pow__(self, other):
        matrix = []
        
        for i in range(min(self.nrows, other.nrows)):
            matrix.append([])
            for j in range(min(self.ncols, other.ncols)):
                matrix[i].append(self.matrix[i][j] ** other.matrix[i][j])

        return Matrix(matrix)
    
    def __str__(self):
        rows = []
        max_len = [0] * len(self.matrix[0]) 
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                max_len[j] = max(max_len[j], len(str(self.matrix[i][j]))) 
        
        for i in range(len(self.matrix)):
            row = []
            
            for j in range(len(self.matrix[i])):
                s = str(self.matrix[i][j])
                l = len(s)
                d = max_len[j] - l 
                s = " " * ((d + 1) // 2) + s + " " * (d // 2) # add spaces before and after the number to make it centered
                row.append(s)
            rows.append("   ".join(row)) 
        
        return "\n".join(rows) 