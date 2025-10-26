## 🏦 Budget App

**Project type:** Part of freeCodeCamp’s Scientific Computing with Python Certification

**Certification duration:** ~300 hours (includes 5 projects)


---

## 📘 Project Description

This is an **object-oriented Python project** developed as part of the freeCodeCamp “Scientific Computing with Python” certification.  
It implements a complete budget management system and an ASCII bar chart visualizing category spending.


---

## ⚙️ Features

### 🏦 Core functionality

- Create and manage **budget categories** (e.g., Food, Clothing, Auto)
- Record **deposits**, **withdrawals**, and **category transfers**
- Calculate **balances** and **spending percentages**
- Generate a **text-based bar chart** showing spending distribution by category

### 🧾 Extra enhancements beyond the original requirements
- ✅ **Input validation:** Accepts both numeric and string amounts, with automatic conversion and error handling  
- ✅ **Negative number handling:** Ignores unnecessary minus signs in withdrawals  
- ✅ **Automatic trimming:** Removes leading and trailing spaces from text inputs  
- ✅ **Dynamic formatting:** Table column widths adapt automatically to the line width and amount length  
- ✅ **Unlimited precision:** Amount field not restricted to 7 characters as in the original project  
- ✅ **Scalable chart:** Works with **any number of categories**, not just four


---

## 🛠️ Skills & Technologies

- Python 3.x
- Object-oriented programming (OOP)
- Data structures: lists and dictionaries
- Input validation and error handling
- String formatting and dynamic text alignment
- Procedural and modular algorithm design
- Conditional logic and flow control
- Testing and debugging


---

## 🧩 Example

### Example usage:

```python
from budget import Category, create_spend_chart

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(30.15)
food.withdraw(25.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

clothing.withdraw(25.15, 'Dress')
clothing.withdraw(15.15, 'Belt')
print(clothing)

auto = Category('Auto')
auto.deposit(200, 'deposit')
auto.withdraw(100, 'insurance')
auto.withdraw(50, 'fuel')
print(auto)

print(create_spend_chart([food, clothing, auto]))
```
### Output:

<img width="275" height="323" alt="Screenshot 2025-10-23 at 9 12 57 PM" src="https://github.com/user-attachments/assets/3ef0fb4a-5f73-4a74-9302-2df4acc26593" />
<img width="266" height="365" alt="Screenshot 2025-10-23 at 9 13 25 PM" src="https://github.com/user-attachments/assets/539ad031-d4f0-4f40-8faf-4d3edf1e1d8c" />


---

## 🧩 Project Context

This project is one of five required for the **Scientific Computing with Python** certification by freeCodeCamp.
It demonstrates proficiency in object-oriented design and algorithmic problem-solving, focusing on creating a functional budget management class and a spending visualization chart using core Python functionality — without external libraries.

---

## 🧑‍💻 Author

Irina Evdokimova (FlaxSilk)

GitHub: https://github.com/FlaxSilk

freeCodeCamp Profile: https://www.freecodecamp.org/FlaxSilk


---

## 📄 License

© 2025 Irina Evdokimova. All rights reserved.  
This code is for personal and educational demonstration only.  
No part of this repository may be used, copied, modified, or distributed without the author’s explicit permission.
