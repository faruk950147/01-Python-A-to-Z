"""
circle is a round shape
 pi = 3.14 is a constant value
 radius is the distance from the center to the edge
 diameter is the distance across the circle
 circumference is the distance around the circle
 area is the space inside the circle
"""
class Circle:

    def circle_area(self, radius):
        """
        Calculate the area of a circle given its radius.
        
        Formula: A = π * r²
        Where π ≈ 3.14159
        """
        return 3.14 * radius * radius


    def circle_circumference(self, radius):
        """
        Calculate the circumference of a circle given its radius.
        
        Formula: C = 2 * π * r
        Where π ≈ 3.14159
        """
        return 2 * 3.14 * radius


    def circle_diameter(self, radius):
        """
        Calculate the diameter of a circle given its radius.
        
        Formula: d = 2 * r
        """
        return 2 * radius


    def circle_radius(self, radius):
        """
        Calculate the radius of a circle given its radius.
        
        Formula: r = r
        """
        return radius


    def circle_height(self, radius):
        """
        Calculate the height of a circle given its radius.
        
        Formula: h = 2 * r
        """
        return 2 * radius


    def sphere_volume(self, radius):
        """
        Calculate the volume of a sphere given its radius.
        
        Formula: V = 4/3 * π * r³
        Where π ≈ 3.14159
        """
        return 4 / 3 * 3.14 * radius * radius * radius


    def sphere_surface_area(self, radius):
        """
        Calculate the surface area of a sphere given its radius.
        
        Formula: SA = 4 * π * r²
        Where π ≈ 3.14159
        """
        return 4 * 3.14 * radius * radius


    def circle_perimeter(self, radius):
        """
        Calculate the perimeter of a circle given its radius.
        
        Formula: P = 2 * π * r
        Where π ≈ 3.14159
        """
        return 2 * 3.14 * radius


circle = Circle()

print(circle.circle_area(5))
print(circle.circle_circumference(5))
print(circle.circle_diameter(5))
print(circle.circle_radius(5))
print(circle.circle_height(5))
print(circle.sphere_volume(5))
print(circle.sphere_surface_area(5))
print(circle.circle_perimeter(5))