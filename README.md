# Person, Favorites, and Toddler Classes

This project demonstrates **Python OOP concepts** such as **inheritance, method overriding, constructors, and class methods** using three classes: `Person`, `Favorites`, and `Toddler`.

---

## 📌 Classes

### 1. `Person`
- Represents a basic person with attributes:
  - `name`, `age`, `address`, `personality`
- Methods:
  - `display()` → Prints a summary about the person.
  - `age()` → Prints the age of the person.
  - `__str__()` → String representation of the object.

---

### 2. `Favorites` (inherits from `Person`)
- Adds additional attributes:
  - `car`, `food`, `movie`
- Methods:
  - `favorite_movie()` → Returns the favorite movie.
  - `favorite_car()` → Prints the favorite car.
  - `favorite_food()` → Prints the favorite food.
  - `__str__()` → String representation.

---

### 3. `Toddler` (inherits from `Person`)
- Overrides the `age()` method to indicate that the person is a toddler.

---

## ▶️ Example Usage

```python
person_1 = Person("Ridwan", "age", "address", "personality")
person_2 = Favorites("Moses", "age", "address", "personality", "food", "movie", "Audi")
person_2.favorite_car()
toddler = Toddler("Ridwan", "age", "address", "personality")

favorite_cr_2 = person_2.favorite_movie()
toddler.age()
print(favorite_cr_2)

💡 Output Example
My name is Moses and my favorite car is Audi
Ridwan you are a toddler
movie

🛠️ Concepts Covered

Object-Oriented Programming

Class Inheritance

Method Overriding

Encapsulation of attributes

__str__ representation

🚀 How to Run

Save the code into a file main.py.

Run in terminal:

python main.py

📄 License

This project is for educational purposes only. Free to modify and reuse.