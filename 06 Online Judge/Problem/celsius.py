class TemperatureConverter:
    """
    A class to convert temperatures between Fahrenheit and Celsius.
    """
    def __init__(self):
        pass
    
    def fahrenheit_to_celsius(self, fahrenheit):
        """
            Convert Fahrenheit to Celsius
            Formula: (F - 32) * 5/9
            90.00 - 32 = 58 
            58 * 5 = 290
            290 / 9 = 32.22
        """
        return round((fahrenheit - 32) * 5/9, 2)
    
    def celsius_to_fahrenheit(self, celsius):
        """
            Convert Celsius to Fahrenheit
            Formula: (C * 9/5) + 32
            32.22 * 9 = 289.98
            289.98 / 5 = 57.996
            57.996 + 32 = 89.996
        """
        return round((celsius * 9/5) + 32, 2)

# Test the class

if __name__ == "__main__":
    converter = TemperatureConverter()
    print(converter.fahrenheit_to_celsius(90.00))  # Expected: 32.22
    print(converter.celsius_to_fahrenheit(32.22))  # Expected: 90.00
