class car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def display_info(self):
        print(f'model: {self.model}, color: {self.color}')

car1 = car("toyota", "red")
car2 = car("tata","black")

car.display_info(car1)
car.display_info(car2)