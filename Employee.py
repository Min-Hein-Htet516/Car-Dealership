class Employee:
    def __init__(self, name, position):
        self.cars_sold = 0
        self.revenue_generated = 0
        self.name = name
        self.position = position

    def set_position(self, position_name):
        self.position = position_name

    def get_position(self):
        return self.position
    
    def increment_cars_sold(self):
        self.cars_sold += 1 

    def get_cars_sold(self):
        return self.cars_sold
    
    def generate_revenue(self, amount):
        self.revenue_generated += amount

    def get_revenue_generated(self):
        return self.revenue_generated
        