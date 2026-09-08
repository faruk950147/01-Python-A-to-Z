class Point:
    '''
    how to calculate the distance between two points

    formula: d = √[(x2 - x1)² + (y2 - y1)²]
    x1 = 0
    y1 = 0
    x2 = 3
    y2 = 4

    (3 - 0) ** 2 + (4 - 0) ** 2
    (3) ** 2 + (4) ** 2
    9 + 16 = 25
    √25 = 5


    '''
    def __init__(self):
        pass
    
    def distance(self, x1, x2, y1, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

p1 = Point()
print(p1.distance(0, 3, 0, 4))
