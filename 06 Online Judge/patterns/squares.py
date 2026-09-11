class Squares:
    def __init__(self, rows):
        self.rows = rows
        
    def numbered_square(self):
        """Numbered Square Pattern using nested loops"""
        print("\nNumbered Square Pattern using nested loops\n")
        for i in range(self.rows):
            for j in range(self.rows):
                # it numerically prints 1234
                # print(j + 1, end=" ") 
                print('*', end=" ")
            print()
    
    def square(self):
        """Square Pattern using simple loops"""
        print("\nSquare Pattern using simple loops\n")
        for i in range(self.rows):
            print("* " * self.rows)

if __name__ == "__main__":
    while True:
        rows = int(input("Enter the number of rows: "))
        if rows == 0:
            break
        squares = Squares(rows)
        squares.numbered_square()
        squares.square()
