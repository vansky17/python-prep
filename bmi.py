class BMICalculator:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.weight = float(input("Enter your weight: "))
        self.height = float(input("Enter your height: "))

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)
    
    def show_bmi_results(self):
        print(f"BMI of {self.name} is: {self.calculate_bmi():.2f}")
    
person = BMICalculator()
person.show_bmi_results()
