class Person:
    def __init__(self, name, age, address, personality):
        self.name = name
        self.age = age
        self.address = address
        self.personality = personality

    def display(self):
        print(f"My name is {self.name}, from {self.address} and I am {self.age} years old. I am mostly {self.personality}")

    def age(self):
        print(f" I am {self.age} years old")

    def __str__(self):
        return f"{self.name} is a Person"


class Favorites(Person):
    def __init__(self, name, age, address, personality, car, food, movie):
        super().__init__(name, age, address, personality)

        self.car = car
        self.food = food
        self.movie = movie

    def favorite_movie(self):
        return self.movie

    def favorite_car(self):
        print(f"My name is {self.name} and my favorite car is {self.car}")

    def favorite_food(self):
        print(f"My name is {self.name} and my favorite food is {self.food}")

    def __str__(self):
        return f"{self.name} Favorites"


class Toddler(Person):
    def age(self):
        print(f"{self.name} you are a toddler")


# Example usage
person_1 = Person("Ridwan", "age", "address", "personality")
person_2 = Favorites("Moses", "age", "address", "personality", "food", "movie", "Audi")
person_2.favorite_car()
toddler = Toddler("Ridwan", "age", "address", "personality")

# person_1.favorite_movie()
# person_1.favorite_food()

favorite_cr_2 = person_2.favorite_movie()
toddler.age()
print(favorite_cr_2)
