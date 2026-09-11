class Pyramid:
    def __init__(self, rows):
        self.rows = rows
    
    def pyramid(self):
        """Pyramid Pattern"""
        print("\nPyramid Pattern\n")
        for i in range(1, self.rows + 1):
            # " " * (self.rows - i) creates the leading spaces for centering
            # "* " * i creates the stars with spaces between them
            print(" " * (self.rows - i) + "* " * i)


    def inverted_pyramid(self):
        """Inverted Pyramid Pattern"""
        print("\nInverted Pyramid Pattern\n")
        for i in range(self.rows, 0, -1):
            # " " * (self.rows - i) creates the leading spaces for centering
            # "* " * i creates the stars with spaces between them
            print(" " * (self.rows - i) + "* " * i)


    def diamond(self):
        """Diamond Pattern"""
        print("\nDiamond Pattern\n")
        # Upper part
        for i in range(1, self.rows + 1):
            # " " * (self.rows - i) creates the leading spaces for centering
            # "* " * i creates the stars with spaces between them
            print(" " * (self.rows - i) + "* " * i)
        # Lower part
        for i in range(self.rows - 1, 0, -1):
            # " " * (self.rows - i) creates the leading spaces for centering
            # "* " * i creates the stars with spaces between them
            print(" " * (self.rows - i) + "* " * i)


if __name__ == "__main__":
    while True:
        rows = int(input("Enter the number of rows: "))
        if rows == 0:
            break
        pyramid = Pyramid(rows)
        pyramid.pyramid()
        pyramid.inverted_pyramid()
        pyramid.diamond()

