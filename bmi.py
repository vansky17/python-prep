class BMICalculator:
    def __init__(self):
        self.name = input("What is your name? ")
        self.weight = 0.0
        self.height = 0.0

        try:
            self.weight = float(input("Enter your weight: "))
            self.height = float(input("Enter your height: "))
        except ValueError:
            print("Error: Please enter valid numbers for weight and height.")

    def calculate_bmi(self):

        if self.weight <= 0:
            print("Error: Weight must be a positive number.")
            return None
        if self.height <= 0:
            print("Error: Height must be a positive number.")
            return None

        return self.weight / (self.height ** 2)

    def show_bmi_results(self):
        self.calculate_bmi()        
        print(f"BMI of {self.name} is: {self.calculate_bmi():.2f}")

person = BMICalculator()
person.show_bmi_results()
# The code defines a BMICalculator class that prompts the user for their name, weight, and height. It includes error handling for invalid inputs and calculates the BMI using the formula weight divided by height squared. The results are displayed with two decimal places.

