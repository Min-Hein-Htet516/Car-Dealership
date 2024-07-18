class Employee:
    def __init__(self, name, position):
        self.cars_sold = 0
        self.revenue_generated = 0
        self.name = name
        self.position = position

    def set_position(self, position_name):
        self.position = position_name