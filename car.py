class Car:
    #this are attributes
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    #now methods
    def drive(self):
        print(f"you drive the {self.model}")

    def stop(self):
        print(f"{self.model} is stopped")


    def describe(self):
        print(f"This is the model {self.model} this is the color {self.color} yaer is {self.year} and is it for sale {self.for_sale}")