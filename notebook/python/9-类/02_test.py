class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("The restaurant cuisine's type is " + self.cuisine_type + ".")
        print(str(self.number_served) + " people came to the restaurant in all.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def open_restaurant(self):
        print("The restaurant is open now!")

restaurant = Restaurant("Malaxiaolongxia", "HuNan")
restaurant.set_number_served(300)
restaurant.increment_number_served(20)

restaurant.describe_restaurant()
restaurant.open_restaurant()

