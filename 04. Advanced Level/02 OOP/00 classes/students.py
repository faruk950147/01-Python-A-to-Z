class Students:
    def __init__(self, name, phy, chem, math):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
    @property 
    def calculate_percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
        
if __name__ == "__main__":
    s1 = Students("John", 90, 80, 70)
    print(s1.name, s1.calculate_percentage)
    s1.phy = 50 # it is not possible to change the value of phy when we use property can change the value of phy
    print(s1.name, s1.calculate_percentage)